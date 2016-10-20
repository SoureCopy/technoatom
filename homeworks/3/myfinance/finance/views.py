from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def start_page(request):
	return HttpResponse("finance/index.html")

def charge_page(request):
	return HttpResponse("finance/charges.html")