# Generated by Django 3.2.5 on 2021-12-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raindrop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='application_id',
        ),
        migrations.AddField(
            model_name='testresult',
            name='result_type',
            field=models.CharField(default='count', max_length=100),
            preserve_default=False,
        ),
    ]
