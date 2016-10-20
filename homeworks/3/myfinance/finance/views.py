from django.shortcuts import render
from django.http import HttpResponse

from finance.utils import gen_headers, gen_charges

def start_page(request):
    return render(request, "finance/index.html")

# Create your views here.
def charge_page(request):
    context = {
        'headers': gen_headers(),
        'charges': gen_charges()
    }
    return render(request, "finance/charges.html", context)