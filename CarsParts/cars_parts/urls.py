from django.urls import include, path
from .views import HomePage, ShowProducts, Display, Bin, Checkout, Payment

urlpatterns = [
    path('unicorn/', include('django_unicorn.urls')),
    path('', HomePage.as_view(), name="home"),
    path('catalogue/<brand>/<model>/', ShowProducts.as_view(), name='catalogue'),
    path('display/<part_id>/', Display.as_view(), name='display'),
    path('bin', Bin.as_view(), name='bin'),
    path('checkout/<grand_total>/', Checkout.as_view(), name='checkout'),
    path('payment/<grand_total>/', Payment.as_view(), name='payment'),
    path('success', HomePage.as_view(), name='finish_yes'),
    path('cancel', HomePage.as_view(), name='finish_no'),
]