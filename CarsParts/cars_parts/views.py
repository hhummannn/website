from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePage(TemplateView):
    template_name = "index.html"


class Catalogue(TemplateView):
    template_name = "unicorn/product_catalogue.html"
