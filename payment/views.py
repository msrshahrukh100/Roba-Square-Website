from django.shortcuts import render, redirect
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse, JsonResponse
from easy_pdf.views import PDFTemplateView
from shopping.models import ProductDescription
from instamojo_wrapper import Instamojo
from django.conf import settings
from django.core.urlresolvers import reverse
from authentication.username import get_user_name
from django.views.decorators.csrf import csrf_exempt
from .models import OnlineTransactionsDetail
# Create your views here.


class viewinvoice(PDFTemplateView):

	template_name = 'hello.html'

	def get_context_data(self, **kwargs):
		return super(viewinvoice, self).get_context_data(
		pagesize="A4",
		title="Hi there!",
		data="thats really cool",
		**kwargs
		)


def checkoutpage(request) :

	cart = request.session.get('products',None)
	print cart
	products = []
	if cart :
		for i in cart :
			products.append(ProductDescription.objects.filter(id=int(i)).first())
	context = {
	'products' : products,
	"cartcount":len(request.session.get('products',[]))
	
	}

	return render(request,"checkoutpage.html",context)

def requestpayment(request) :
	api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');
	data = dict(request.POST)
	productnames = data.get('productname')
	ids = data.get('id')
	size = data.get('size')
	quantity = data.get('quantity')
	a = data.get('grandtotal')
	amount = max(list(a))
	p = " -- ".join(productnames)
	i = " -- ".join(ids)
	s = " -- ".join(size)
	q = " -- ".join(quantity)
	purpose = "'"+i + " | " + p + " | " + q + " | " + s + "'"
	redirect_url = request.build_absolute_uri(reverse("payment:paymentredirect"))
	webhook = request.build_absolute_uri(reverse("payment:webhook"))
	response = api.payment_request_create(
		amount=amount,
		purpose="purpose",
		buyer_name=get_user_name(request.user),
		email=request.user.email,
		phone=request.user.user_information.phonenumber,
		# redirect_url=redirect_url,
		# webhook=webhook,
		send_email=True,
		send_sms=True,
		)
	return redirect(response['payment_request']['longurl']+"?embed=form")



def paymentredirect(request):
	api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');
	payment_id = request.GET.get('payment_id')
	payment_request_id = request.GET.get('payment_request_id')

	try:
		response = api.payment_request_payment_status(
			id=payment_request_id,
			payment_id=payment_id
			)
	except :
		response = None

	if response :
		success = response.get('success')
		if success :
			context['success'] = "Thank you for shopping with us.You can download your invoice here."
			context['payment_request'] = response.get('payment_request')
		else :
			context['fail'] = response.get('message')
	else :
		context['fail'] = "Your transaction failed due to some technical issue like network error."

	return render(request,"paymentredirect.html",context)
	


	

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


