# Generated by Django 5.0.1 on 2024-05-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_deliverydetails_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverydetails',
            name='pincode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
