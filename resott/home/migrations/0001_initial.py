# Generated by Django 4.0.1 on 2022-04-20 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crs', models.CharField(default='recommended', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('details', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('cimage', models.ImageField(upload_to='media/restro')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='restabts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=25)),
                ('localty', models.CharField(max_length=30)),
                ('timings', models.CharField(max_length=30)),
                ('costEstimate', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=25)),
                ('directions', models.CharField(max_length=100)),
                ('img1', models.ImageField(default='default/default restaurant.jpg', upload_to='media/restro')),
                ('img2', models.ImageField(default='default/default restaurant.jpg', upload_to='media/restro')),
                ('img3', models.ImageField(default='default/default restaurant.jpg', upload_to='media/restro')),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='FoodANDcombo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=25)),
                ('fimage', models.ImageField(upload_to='media/restro')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.restaurant')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.courses')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.foodandcombo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
