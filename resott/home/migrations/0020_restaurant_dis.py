# Generated by Django 4.0.1 on 2022-06-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_feedback_rest'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='dis',
            field=models.IntegerField(default=0),
        ),
    ]
