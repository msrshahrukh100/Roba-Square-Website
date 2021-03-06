from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
from django.http import HttpResponse, JsonResponse, Http404
from shopping.models import ProductDescription
from instamojo_wrapper import Instamojo
from django.conf import settings
from django.core.urlresolvers import reverse
from authentication.username import get_user_name
from django.views.decorators.csrf import csrf_exempt
from .models import OnlineTransactionsDetail, BuyingCart, Refund_requests
from django.contrib.auth.decorators import login_required
from easy_pdf.rendering import render_to_pdf_response
import uuid
from notifications.signals import notify
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

def send_email_to_user(message,receiver,user,url) :
	# msg_plain = render_to_string('email/email.txt', {'user': user,'url':url})
	# msg_html = render_to_string('email/email.html', {'user': user,'url':url})
	# send_mail(
	#     'test email',
	#     msg_plain,
	#     'care@robasquare.com',
	#     ['msr.concordfly@gmail.com'],
	#     fail_silently=True,
	#     html_message=msg_html,
	# )

	# from django.core.mail import EmailMultiAlternatives
	# from django.template.loader import render_to_string
	# from django.utils.html import strip_tags

	# subject, from_email, to = 'Thank You!', 'care@robasquare.com', 'msr.concordfly@gmail.com'

	# html_content = render_to_string('email/email.html', {'user': user,'url':url}) # ...
	# text_content = strip_tags(html_content) # this strips the html, so people will have the text as well.

	# # create the email, and attach the HTML version as well.
	# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	# msg.attach_alternative(html_content, "text/html")
	# msg.send()

	from django.core.mail import send_mail
	from django.template.loader import render_to_string
	msg_plain = render_to_string('email/email.txt', {'user': user,'url':url})
	msg_html = render_to_string('email/email.html', {'user': user,'url':url})
	send_mail(
	message,
	msg_plain,
	'care@robasquare.com',
	[receiver],
	html_message=msg_html,
	)




@login_required
def checkoutpage(request) :

	cart = request.session.get('products',None)
	products = []
	if cart :
		for i in cart :
			products.append(ProductDescription.objects.filter(id=int(i)).first())

	a = request.user.addresses.all()
	address = []
	for i in a :
		temp = i.address + ", " + i.city + " - " + str(i.pincode) + ", " + i.nearest_landmark + "."
		address.append(temp)
	context = {
	'products' : products,
	"cartcount":len(request.session.get('products',[])),
	"address" : address,
	}

	# for generating pdf
	# return render_to_pdf_response(request,"hello.html",{"data":"shahrukh"})

	return render(request,"checkoutpage.html",context)


@login_required
def generateinvoice(request) :
	t = request.GET.get('type')
	id = request.GET.get('id')
	if t == "cod" :
		cart = BuyingCart.objects.filter(cod_unique_id=id)
		total = 0
		for i in cart :
			total += int(i.price)
		
		cod = 40
		total += cod 
		context = {'cart':cart,'total':total,'cod':40}
		# return render_to_pdf('invoice/invoice.html',{'pagesize':'A4','cart': cart})
		return render_to_pdf_response(request,"invoice/invoice.html",context)

	else :
		cart = BuyingCart.objects.filter(instamojo_request_id=id)
		total = 0
		for i in cart :
			total += int(i.price)
		
		context = {'cart':cart,'total':total}
		# return render_to_pdf('invoice/invoice.html',{'pagesize':'A4','cart': cart})
		return render_to_pdf_response(request,"invoice/invoice.html",context)


	return JsonResponse({'sad':'asd'})



@login_required
def requestpayment(request) :
	data = dict(request.POST)
	productnames = data.get('productname')
	ids = data.get('id')
	size = data.get('size')
	quantity = data.get('quantity')
	price = data.get('productprice')
	if data.get('address')[0] == "0" :
		address = data.get('newaddress')[0]
	else :
		address = data.get('address')[0]
	phone = data.get('phonenumber')[0]

	a = data.get('grandtotal')
	amount = max(list(a))

	if request.user.email != "" :
		email = request.user.email
	else :
		email = "foo@example.com"

	t = data.get('type')
	if t[0] == "" :
		paymenttype = "online"
	else :
		paymenttype = t[0]

	if paymenttype == "cod" :
		cod_unique_id = uuid.uuid4()
		for i in range(len(ids)) :
			instance = ProductDescription.objects.get(id=ids[i])
			product = instance.prod.get(size=size[i])
			product.stockcount = product.stockcount - int(quantity[i])
			product.save()
			BuyingCart.objects.get_or_create(
				user=request.user,
				product=instance,
				size=size[i],
				quantity=quantity[i],
				price = price[i],
				method_of_payment="COD",
				address=address,
				phonenumber=phone,
				status="Done",
				cod_unique_id=cod_unique_id,
				invoice_url=request.build_absolute_uri(reverse("payment:generateinvoice"))[:-1] + "?type=cod&id=" + str(cod_unique_id),
				)
		url = request.build_absolute_uri(reverse("payment:generateinvoice"))[:-1] + "?type=cod&id=" + str(cod_unique_id)
		context = {"type" : 1,"url":url}
		try:
			send_email_to_user(message="Thank You!",receiver=request.user.email,user=get_user_name(request.user),url=url)
		except :
			pass
		return render(request,"paymentredirect.html",context)
		
	api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://www.instamojo.com/api/1.1/');
	purpose = " | ".join(ids)
	redirect_url = request.build_absolute_uri(reverse("payment:paymentredirect"))
	webhook = request.build_absolute_uri(reverse("payment:webhook"))
	response = api.payment_request_create(
		amount=amount,
		purpose=purpose,
		buyer_name=get_user_name(request.user),
		email=email,
		phone=phone,
		redirect_url=redirect_url,
		webhook=webhook,
		allow_repeated_payments=False,
		send_email=True,
		send_sms=True,
		)

	if response.get('success') :
		for i in range(len(ids)) :
			instance = ProductDescription.objects.get(id=ids[i])
			product = instance.prod.get(size=size[i])
			product.stockcount = product.stockcount - int(quantity[i])
			product.save()
			BuyingCart.objects.get_or_create(
				user=request.user,
				product=instance,
				size=size[i],
				quantity=quantity[i],
				price = price[i],
				method_of_payment="Online Payment",
				address=address,
				phonenumber=phone,
				instamojo_request_id=response['payment_request']['id']
				)
	else :
		return JsonResponse({'message' : response['message']})

	return redirect(response['payment_request']['longurl']+"?embed=form")


@login_required
def paymentredirect(request):
	api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://www.instamojo.com/api/1.1/');
	payment_id = request.GET.get('payment_id')
	payment_request_id = request.GET.get('payment_request_id')

	try:
		response = api.payment_request_payment_status(
			id=payment_request_id,
			payment_id=payment_id
			)
	except :
		response = None
	context = {}
	if response :
		success = response.get('success')
		if success :
			context['success'] = "Thank you for shopping with us.You can download your invoice here."
			context['payment_request'] = response.get('payment_request')
			buyingcart = BuyingCart.objects.filter(instamojo_request_id=context['payment_request']['id'])
			for i in buyingcart :
				i.status = "Done"
				i.paymentid = payment_id
				i.invoice_url = request.build_absolute_uri(reverse("payment:generateinvoice"))[:-1] + "?type=online&id=" + str(context['payment_request']['id'])
				i.save()
			context['type'] = 1
			context['url'] = request.build_absolute_uri(reverse("payment:generateinvoice"))[:-1] + "?type=online&id=" + str(context['payment_request']['id'])

			try:
				
				send_email_to_user(message="Thank You!",receiver=request.user.email,user=get_user_name(request.user),url=url)
			except :
				pass

		else :
			context['fail'] = response.get('message')
			context['type'] = 0
	else :
		context['fail'] = "Your transaction failed due to some technical issue like network error."
		context['type'] = 0

	return render(request,"paymentredirect.html",context)
	



@login_required
def myorders(request) :
	items = BuyingCart.objects.filter(user=request.user).filter(returned=False).order_by("-id")

	context = {"items":items}
	return render(request,"myorders.html",context)
	

@csrf_exempt
def webhook(request) :
	if request.method == 'POST' :
		amount = request.POST.get('amount')
		buyer = request.POST.get('buyer')
		buyer_name = request.POST.get('buyer_name')
		buyer_phone = request.POST.get('buyer_phone')
		currency = request.POST.get('currency')
		fees = request.POST.get('fees')
		longurl = request.POST.get('longurl')
		mac = request.POST.get('mac')
		payment_id = request.POST.get('payment_id')
		payment_request_id = request.POST.get('payment_request_id')
		purpose = request.POST.get('purpose')
		shorturl = request.POST.get('shorturl')
		status = request.POST.get('status')
		
		OnlineTransactionsDetail.objects.get_or_create(
			user = request.user,
			amount=amount,
			buyer=buyer,
			buyer_name=buyer_name,
			buyer_phone=buyer_phone,
			currency=currency,
			fees=fees,
			longurl=longurl,
			mac=mac,
			payment_id=payment_id,
			payment_request_id=payment_request_id,
			purpose=purpose,
			shorturl=shorturl,
			status=status)

	return JsonResponse({'msg':'Entry added!'})


@login_required
def returns(request,id=None) :
	if request.method == 'POST' :
		item = BuyingCart.objects.get(id=request.POST.get('id'))
		reason = request.POST.get('reason')
		Refund_requests.objects.get_or_create(user=request.user,refund_item=item,reason=reason)
		verb = "We have received your request for return. You can check the status in My Returns."
		url = reverse("payment:myorders")

		imageurl = item.product.get_image_url
		notify.send(request.user, recipient=request.user, verb=verb, url=url,imageurl=imageurl)
		item.returned = True
		item.save()
		return redirect("/")

	item = BuyingCart.objects.get(id=id)
	context = {"item":item, "id":id}
	return render(request, 'returnpage.html', context)


@login_required
def myreturns(request) :
	context = {"items" : Refund_requests.objects.filter(user=request.user)}
	return render(request,"myreturns.html", context)
	
