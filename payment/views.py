from django.shortcuts import render
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from easy_pdf.views import PDFTemplateView
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
	pass

