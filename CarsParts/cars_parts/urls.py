from django.urls import include, path
from .views import HomePage, ShowProducts

urlpatterns = [
    path('unicorn/', include('django_unicorn.urls')),
    path('', HomePage.as_view()),
    path('catalogue/<brand>/<model>/', ShowProducts.as_view(), name='catalogue'),
    path('display/part_id/', ShowProducts.as_view(), name='display'),
]