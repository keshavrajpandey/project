# Generated by Django 2.1.7 on 2019-06-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20190607_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_img/'),
        ),
    ]
