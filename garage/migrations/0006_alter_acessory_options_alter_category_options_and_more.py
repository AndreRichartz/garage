# Generated by Django 5.0.3 on 2024-03-20 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0005_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acessory',
            options={'verbose_name': 'Acessory', 'verbose_name_plural': 'Acessories'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Color', 'verbose_name_plural': 'Colors'},
        ),
    ]
