# Generated by Django 3.2.5 on 2021-12-20 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raindrop', '0005_testcases_result_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresult',
            name='result_type',
        ),
    ]
