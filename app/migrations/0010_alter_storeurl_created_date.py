# Generated by Django 4.1.3 on 2022-12-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_storeurl_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeurl',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]
