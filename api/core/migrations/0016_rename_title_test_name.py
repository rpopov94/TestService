# Generated by Django 4.1.4 on 2023-01-05 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_question_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='title',
            new_name='name',
        ),
    ]
