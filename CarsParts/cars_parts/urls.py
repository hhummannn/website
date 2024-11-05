from django.urls import include, path
from .views import HomePage, ShowProducts, Display, Bin, Checkout

urlpatterns = [
    path('unicorn/', include('django_unicorn.urls')),
    path('', HomePage.as_view()),
    path('catalogue/<brand>/<model>/', ShowProducts.as_view(), name='catalogue'),
    path('display/<part_id>/', Display.as_view(), name='display'),
    path('bin', Bin.as_view(), name='bin'),
    path('checkout', Checkout.as_view(), name='checkout'),
]