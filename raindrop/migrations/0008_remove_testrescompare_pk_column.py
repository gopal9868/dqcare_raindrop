# Generated by Django 3.2.5 on 2021-12-21 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raindrop', '0007_testrescompare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testrescompare',
            name='pk_column',
        ),
    ]
