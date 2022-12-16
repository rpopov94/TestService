# Generated by Django 4.1.4 on 2022-12-16 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_testquestion_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='TestQuestion',
        ),
    ]
