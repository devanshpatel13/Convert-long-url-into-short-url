# Generated by Django 4.1.3 on 2022-11-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.URLField()),
                ('shorturl', models.URLField()),
            ],
        ),
    ]