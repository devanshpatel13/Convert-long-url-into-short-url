# Generated by Django 4.1.3 on 2022-12-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_storeurl_longurl_alter_storeurl_shorturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeurl',
            name='shorturl',
            field=models.URLField(db_index=True, max_length=120, unique=True),
        ),
    ]