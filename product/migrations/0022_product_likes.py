# Generated by Django 2.1.7 on 2019-06-11 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_remove_product_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]