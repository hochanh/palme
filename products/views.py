from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from paypal.standard.forms import PayPalPaymentsForm

from .models import Product


payment_done = TemplateView.as_view(template_name="products/payment_done.html")
payment_canceled = TemplateView.as_view(template_name="products/payment_canceled.html")


def get_product_form(p, host):
    paypal_dict = {
        'business': settings.SELLER_EMAIL,
        'amount': p.price,
        'item_name': p.name,
        'invoice': f"{p.name} invoice",
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
    }
    return PayPalPaymentsForm(initial=paypal_dict)


def index(request):
    product_list = Product.objects.all()
    host = request.get_host()
    return render(request, 'products/index.html', {
        'product_list': [(p, get_product_form(p, host)) for p in product_list]
    })
