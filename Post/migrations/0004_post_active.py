# Generated by Django 3.0.8 on 2020-07-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20200728_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
