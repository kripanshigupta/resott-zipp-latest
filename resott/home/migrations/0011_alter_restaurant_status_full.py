# Generated by Django 4.0.1 on 2022-05-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_restaurant_usr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='status_full',
            field=models.BooleanField(default=True),
        ),
    ]
