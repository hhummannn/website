from django_unicorn.components import UnicornView
from CarsParts.cars_parts.models import *


class CatalogueView(UnicornView):
    def __init__(self, brand, model):
        self.brand = brand.capitalize()
        self.model = model.capitalize()

    def refresh(self):
        print("REFRESHING!")
        model_id = Models.objects.get(brand=self.brand, model=self.model)
        belonging_parts = Parts.objects.filter(model_id=model_id)
        print(belonging_parts)

