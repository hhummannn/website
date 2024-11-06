from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from django.db import connection
from ..views import user_bin


class DisplayView(UnicornView):
    id = 0
    model_id = 0
    name = ""
    description = ""
    available = 0
    price = 0.0
    image = []
    current_image_index = 0
    quantity = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs['part_id']
        part_query = f"SELECT * FROM parts WHERE parts.id = {self.id};"
        cursor = connection.cursor()
        cursor.execute(part_query)
        part = cursor.fetchall()[0]
        self.model_id = part[1]
        self.name = part[2]
        self.description = part[3]
        self.available = part[4]
        price_query = (f"SELECT prices.uah FROM prices left join parts "
                       f"on parts.pricing = prices.id WHERE parts.id = {self.id};")
        cursor = connection.cursor()
        cursor.execute(price_query)
        self.price = cursor.fetchall()[0][0]
        price_query = (f"SELECT images.* FROM images left join parts on "
                       f"images.part_id = parts.id WHERE parts.id = {self.id};")
        cursor = connection.cursor()
        cursor.execute(price_query)
        self.images = [image[1] for image in cursor.fetchall()]

    def current_image(self):
        return f"images/{self.images[self.current_image_index]}"

    def next_image(self):
        print("next before change", self.current_image_index, len(self.images))
        if self.current_image_index + 1 >= len(self.images):
            self.current_image_index = 0
        else:
            self.current_image_index += 1
        print("next after change", self.current_image_index)
        return f"images/{self.images[self.current_image_index]}"

    def previous_image(self):
        print("next before change", self.current_image_index, len(self.images))
        if self.current_image_index - 1 < 0:
            self.current_image_index = len(self.images) - 1
        else:
            self.current_image_index -= 1
        print("previous after change", self.current_image_index)
        return f"images/{self.images[self.current_image_index]}"

    def add_part(self, quantity):
        bin = user_bin
        if int(quantity) <= 0:
            return
        if int(quantity) > self.available:
            quantity = self.available
        print(f"QUANTITY: {self.quantity}")
        bin.add_part(part_id=self.id, quantity=int(quantity), available=self.available,
                          price=self.price, title_image=self.images[0], name=self.name)

    def bin(self):
        return redirect("bin")
