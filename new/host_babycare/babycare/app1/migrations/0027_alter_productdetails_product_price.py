# Generated by Django 5.0.1 on 2024-05-13 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_alter_deliverydetails_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='product_price',
            field=models.IntegerField(null=True),
        ),
    ]
