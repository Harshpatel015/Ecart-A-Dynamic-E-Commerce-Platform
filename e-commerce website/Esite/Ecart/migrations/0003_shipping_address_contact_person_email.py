# Generated by Django 4.2.16 on 2024-10-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecart', '0002_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping_address',
            name='Contact_Person_Email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
