# Generated by Django 5.1.3 on 2025-05-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delivery_remove_gallery_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='description_two',
            field=models.TextField(blank=True, null=True, verbose_name='Второй текст на странице'),
        ),
    ]
