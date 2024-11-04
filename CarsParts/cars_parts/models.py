from django.db import models


# Create your models here.

class Parts(models.Model):
    id = models.IntegerField(primary_key=True)
    model_id = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    available = models.IntegerField()
    pricing = models.IntegerField()


class Models(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)


class Images(models.Model):
    id = models.IntegerField(primary_key=True)
    image_name = models.CharField(max_length=200)
    part_id = models.IntegerField()


class OrderedParts(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    part_id = models.IntegerField()
    quantity = models.IntegerField()


class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    order_number = models.IntegerField()
    customer_id = models.IntegerField()


class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    recipient_name = models.CharField(max_length=200)
    recipient_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


class Prices(models.Model):
    id = models.IntegerField(primary_key=True)
    uah = models.FloatField()
    usd = models.FloatField()
    eur = models.FloatField()
