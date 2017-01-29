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
		email="msr.concordfly@gmail.com",
		phone="8376061893",
		# redirect_url=redirect_url,
		# webhook=webhook,
		webhook="http://requestb.in/1ibyspq1",
		send_email=True,
		send_sms=True,
		)
	return redirect(response['payment_request']['longurl']+"?embed=form")



def paymentredirect(request):
	pass

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
		

	print request.POST
	return JsonResponse({'msg':'asd'})


