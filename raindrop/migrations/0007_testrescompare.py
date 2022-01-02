# Generated by Django 3.2.5 on 2021-12-20 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raindrop', '0006_remove_testresult_result_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='testrescompare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testcases_id', models.IntegerField()),
                ('pk_column', models.CharField(max_length=100)),
                ('result_column', models.CharField(max_length=50)),
                ('result_status', models.CharField(max_length=10)),
                ('source_result', models.CharField(max_length=500)),
                ('target_result', models.CharField(max_length=500)),
                ('change_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
