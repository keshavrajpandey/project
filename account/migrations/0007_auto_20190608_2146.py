# Generated by Django 2.1.7 on 2019-06-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20190608_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
