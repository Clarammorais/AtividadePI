# Generated by Django 4.2.1 on 2023-05-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locadora", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="filme",
            name="valor",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
