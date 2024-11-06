from dataclasses import dataclass


class UserBin:
    def __init__(self):
        """
        self.parts = {
            {
                "part_id": part_id,
                "quantity": quantity,
                "available": available,
                "price": price,
                "title_image": title_image,
                "name": name,
            },
        }
        """
        self.parts = []

    def add_part(self, part_id, quantity, available, price, title_image, name):
        title_image = f"images/{title_image}"
        to_add = {
            "part_id": int(part_id),
            "quantity": int(quantity),
            "available": int(available),
            "price": float(price),
            "total_price": float(price) * int(quantity),
            "title_image": title_image,
            "name": name,
        }
        for part in self.parts:
            if part['part_id'] == to_add['part_id']:
                to_add['quantity'] = to_add['quantity'] + part['quantity']
                if to_add['quantity'] > to_add['available']:
                    to_add['quantity'] = to_add['available']
                to_add["total_price"] = to_add["price"] * to_add["quantity"]
                for key, value in to_add.items():
                    part[key] = value
                return
        self.parts.append(to_add)


class Parts:
    def __init__(self, id, model_id, name, description, available, pricing, images):
        self.id = id
        self.model_id = model_id
        self.name = name
        self.description = description
        self.available = available
        self.pricing = pricing
        self.images = images
        self.title_image = f"/images/{images[0]['image_name']}"


class Models:
    def __init__(self, id, brand, model):
        self.id = id
        self.brand = brand
        self.model = model


class Images:
    def __init__(self, id, image_name, part_id):
        self.id = id
        self.image_name = image_name
        self.part_id = part_id


class OrderedParts:
    def __init__(self, id, order_id, part_id, quantity):
        self.id = id
        self.order_id = order_id
        self.part_id = part_id
        self.quantity = quantity


class Orders:
    def __init__(self, id, order_number, customer_id):
        self.id = id
        self.order_number = order_number
        self.customer_id = customer_id


class Customers:
    def __init__(self, id, recipient_name, recipient_address, phone, email):
        self.id = id
        self.recipient_name = recipient_name
        self.recipient_address = recipient_address
        self.phone = phone
        self.email = email


class Prices:
    # def __init__(self, id, uah, usd, eur):
    def __init__(self, id, uah):
        self.id = id
        self.uah = uah
        # self.usd = usd
        # self.eur = eur
