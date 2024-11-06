from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from django.db import connection

from ..db_dataclasses import *


class ShowProductsView(UnicornView):
    brand = ""
    model = ""
    parts = []
    prices = []
    datablocks = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.brand = kwargs['brand']
        self.model = kwargs['model']
        parts_query = (f"SELECT parts.* FROM parts left join models on models.id = parts.model_id "
                       f"WHERE brand = '{self.brand}' and model = '{self.model}' ")
        cursor = connection.cursor()
        cursor.execute(parts_query)
        self.parts = cursor.fetchall()
        images_query = (f"SELECT images.* FROM parts left join models on models.id = parts.model_id "
                        f"left join images on images.part_id = parts.id "
                        f"WHERE brand = '{self.brand}' and model = '{self.model}' ")
        cursor.execute(images_query)
        self.images = cursor.fetchall()
        prices_query = (f"SELECT prices.* FROM parts left join models on models.id = parts.model_id "
                        f"left join prices on parts.pricing = prices.id "
                        f"WHERE brand = '{self.brand}' and model = '{self.model}' ")
        cursor.execute(prices_query)
        self.prices = cursor.fetchall()
        self.images = [Images(id=image[0], image_name=image[1], part_id=image[2]).__dict__ for image in self.images]
        self.prices = [Prices(id=price[0], uah=price[1]).__dict__ for price in self.prices]
        images = {}
        for part in self.parts:
            images[part] = []
            for image in self.images:
                if part[0] == image['part_id']:
                    images[part].append(image)
        prices = {}
        for part in self.parts:
            for price in self.prices:
                if part[5] == price['id']:
                    prices[part] = price

        self.parts = [Parts(id=part[0], model_id=part[1], name=part[2], description=part[3], available=part[4], pricing=prices[part], images=images[part]).__dict__ for part in self.parts]
        self.datablocks = {}
        for part in self.parts:
            self.datablocks[str(part['id'])] = {}
            self.datablocks[str(part['id'])]['part_details'] = part
            self.datablocks[str(part['id'])]['images'] = {}
            for price in self.prices:
                if price['id'] == part['pricing']:
                    self.datablocks[str(part['id'])]['prices'] = price
            id = 0
            for image in self.images:
                if image['part_id'] == part['id']:
                    self.datablocks[str(part['id'])]['images'][str(id)] = image['image_name']
                    id += 1

    def parts(self):
        return self.parts

    def display_part(self, part_id):
        return redirect("display", part_id=part_id)

    def bin(self):
        return redirect("bin")
