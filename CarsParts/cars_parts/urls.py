from django.urls import include, path
from .views import HomePage, Catalogue

urlpatterns = [
    path('unicorn/', include('django_unicorn.urls')),
    path('', HomePage.as_view()),
    path('product_catalogue.py/<brand>/<model>/', Catalogue.as_view(), name='show_category')
]