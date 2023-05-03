# Generated by Django 4.2 on 2023-05-02 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('bmi', models.IntegerField(default=0)),
                ('uploaded', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
