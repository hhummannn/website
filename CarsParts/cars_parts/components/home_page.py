from django.shortcuts import render, redirect
from django_unicorn.components import UnicornView


class HomePageView(UnicornView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def catalogue(self, brand, model):
        print(f"Brand is {brand}, model is {model}")
        return redirect("catalogue", brand=brand, model=model)

    def bin(self):
        return redirect("bin")
