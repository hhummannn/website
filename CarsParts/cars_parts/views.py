from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePage(TemplateView):
    template_name = "home_page_load.html"


class ShowProducts(TemplateView):
    template_name = "show_products_load.html"
