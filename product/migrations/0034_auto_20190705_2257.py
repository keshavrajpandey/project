# Generated by Django 2.1.7 on 2019-07-05 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
