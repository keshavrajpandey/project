# Generated by Django 2.2.12 on 2020-04-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0048_product_bought_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='show_contact',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='show_location',
            field=models.BooleanField(),
        ),
    ]