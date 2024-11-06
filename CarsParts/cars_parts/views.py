from django.shortcuts import render
from django.views.generic import TemplateView
from .db_dataclasses import UserBin

user_bin = UserBin()

# Create your views here.


class HomePage(TemplateView):
    template_name = "home_page_load.html"


class ShowProducts(TemplateView):
    template_name = "show_products_load.html"


class Display(TemplateView):
    template_name = "display_load.html"


class Bin(TemplateView):
    template_name = "bin_load.html"


class Checkout(TemplateView):
    template_name = "checkout_load.html"


class Payment(TemplateView):
    template_name = "payment_load.html"
