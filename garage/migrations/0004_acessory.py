# Generated by Django 5.0.3 on 2024-03-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0003_rename_description_category_description_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_ace', models.CharField(max_length=100)),
            ],
        ),
    ]
