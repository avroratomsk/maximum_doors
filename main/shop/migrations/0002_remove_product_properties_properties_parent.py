# Generated by Django 5.1.3 on 2024-11-28 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='properties',
        ),
        migrations.AddField(
            model_name='properties',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='shop.product', verbose_name='Родитель'),
        ),
    ]
