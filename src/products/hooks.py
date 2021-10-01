from paypal.standard.models import ST_PP_COMPLETED
from django.conf import settings
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received


def check_ipn(sender, **kwargs):
    ipn_obj = sender
    print("obj", ipn_obj)
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != settings.SELLER_EMAIL:
            return

    else:
        pass


def register_signals():
    valid_ipn_received.connect(check_ipn)
    invalid_ipn_received.connect(check_ipn)
