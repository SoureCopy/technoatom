from django.conf.urls import url
from finance.views import start_page, charge_page

urlpatterns = [
    url(r'^$', start_page),
    url(r'^charges/$', charge_page),
]