# Generated by Django 5.0.1 on 2024-04-08 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
