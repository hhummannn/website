# Generated by Django 5.1.2 on 2024-11-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars_parts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customers",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("recipient_name", models.CharField(max_length=200)),
                ("recipient_address", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Images",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("image_name", models.CharField(max_length=200)),
                ("part_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Models",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("brand", models.CharField(max_length=200)),
                ("model", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="OrderedParts",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("order_id", models.IntegerField()),
                ("part_id", models.IntegerField()),
                ("quantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("order_number", models.IntegerField()),
                ("customer_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Parts",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("model_id", models.IntegerField()),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("available", models.IntegerField()),
                ("pricing", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Prices",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("uah", models.FloatField()),
                ("usd", models.FloatField()),
                ("eur", models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name="CarPart",
        ),
    ]