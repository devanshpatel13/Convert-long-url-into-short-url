# Generated by Django 4.1.3 on 2022-12-28 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_remove_storeurl_longurl"),
    ]

    operations = [
        migrations.AddField(
            model_name="storeurl",
            name="longurl",
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
