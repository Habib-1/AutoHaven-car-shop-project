# Generated by Django 5.1.2 on 2024-11-19 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_brand_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
    ]
