from django_unicorn.components import UnicornView
from ..views import user_bin


class CheckoutView(UnicornView):
    bin = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
