import os

from django_unicorn.components import UnicornView
import stripe


class PaymentView(UnicornView):
    amount = 0
    checkout_url = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.amount = kwargs['grand_total']
        self.create_checkout_session()

    def create_checkout_session(self):
        try:
            # Create a Stripe Checkout Session
            stripe.api_key = os.environ.get("stripe_api_key")
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'uah',
                        'product_data': {
                            'name': 'Payment',
                        },
                        'unit_amount': int(float(self.amount) * 100),  # amount in cents
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://127.0.0.1:8000/success',  # Customize success URL
                cancel_url='http://127.0.0.1:8000/cancel',  # Customize cancel URL
            )
            self.checkout_url = session.url
        except Exception as e:
            print(f"An error... {e}")
            self.errors["amount"] = str(e)
            self.checkout_url = None