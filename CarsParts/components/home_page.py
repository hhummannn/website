from django.shortcuts import redirect
from django_unicorn.components import UnicornView


class HomePageView(UnicornView):
    def show_category(self, brand, model):
        print(f"Brand is {brand}, model is {model}")
        return redirect("show_category", brand=brand, model=model)
