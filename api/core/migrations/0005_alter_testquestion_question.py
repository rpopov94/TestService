# Generated by Django 4.1.4 on 2022-12-15 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_testquestion_delete_testquesuion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='core.question'),
        ),
    ]