from django.shortcuts import render, redirect
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse, JsonResponse
from easy_pdf.views import PDFTemplateView
from shopping.models import ProductDescription
from instamojo_wrapper import Instamojo
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
	API_KEY = "f395561c55eab6935baa28f23489d82a"
	AUTH_TOKEN = "339688dc1a623af0c019c7e528540e61"
	api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');

	response = api.payment_request_create(
		amount='3499',
		purpose='Hoody',
		send_email=True,
		email="msr.concordfly@gmail.com",
		redirect_url="http://www.example.com/handle_redirect.py"
		)
	# print the long URL of the payment request.
	print response['payment_request']['longurl']
	# print the unique ID(or payment request ID)
	print response['payment_request']['id']
	return redirect(response['payment_request']['longurl']+"?embed=form")

