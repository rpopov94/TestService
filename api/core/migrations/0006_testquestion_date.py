# Generated by Django 4.1.4 on 2022-12-15 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_testquestion_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='testquestion',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
