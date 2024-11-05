from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from ..views import user_bin


class BinView(UnicornView):
    bin = []
    new_quantity = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_bin = user_bin
        self.bin = self.user_bin.parts
        print(self.bin)

    def update_quantity(self, new_quantity, part_id):
        new_quantity = int(new_quantity)
        part_id = int(part_id)
        remember_index = 0
        for index, part in enumerate(self.user_bin.parts):
            if part['part_id'] == part_id:
                remember_index = index
                break
        self.user_bin.parts[index]['quantity'] = new_quantity
        if self.user_bin.parts[index]['quantity'] > self.user_bin.parts[index]['available']:
            self.user_bin.parts[index]['quantity'] = self.user_bin.parts[index]['available']
        self.user_bin.parts[index]["total_price"] = (self.user_bin.parts[index]["price"] *
                                                     self.user_bin.parts[index]["quantity"])
        self.bin = self.user_bin.parts
        global user_bin
        user_bin = self.user_bin
        print(self.user_bin.parts[index])
        print(self.user_bin.parts)

    def grand_total(self):
        return sum([part['total_price'] for part in self.user_bin.parts])

    def checkout(self):
        return redirect("checkout")
