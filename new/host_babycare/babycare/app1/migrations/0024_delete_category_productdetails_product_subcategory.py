# Generated by Django 5.0.1 on 2024-05-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='productdetails',
            name='product_subcategory',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
