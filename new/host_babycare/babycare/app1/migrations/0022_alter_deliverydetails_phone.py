# Generated by Django 5.0.1 on 2024-05-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_productdetails_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverydetails',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
