# Generated by Django 5.0.1 on 2024-04-16 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_productdetails_sub_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetails',
            name='sub_categories',
        ),
    ]
