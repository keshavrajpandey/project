# Generated by Django 2.2.12 on 2020-04-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_product_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
