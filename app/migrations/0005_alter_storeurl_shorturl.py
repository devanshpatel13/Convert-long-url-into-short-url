# Generated by Django 4.1.3 on 2022-12-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_storeurl_shorturl"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storeurl", name="shorturl", field=models.URLField(),
        ),
    ]