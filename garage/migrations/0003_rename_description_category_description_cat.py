# Generated by Django 5.0.3 on 2024-03-19 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0002_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='description',
            new_name='description_cat',
        ),
    ]
