from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class testcases(models.Model):
    appname=models.CharField(max_length=100)
    testcase_desc=models.CharField(max_length=500)
    source_query=models.CharField(max_length=5000)
    target_query=models.CharField(max_length=5000)
    source_connection_name=models.CharField(max_length=500)
    target_connection_name=models.CharField(max_length=500)
    source_table_name=models.CharField(max_length=100)
    target_table_name=models.CharField(max_length=100)
    change_date=models.DateTimeField(auto_now=True)
    result_type=models.CharField(max_length=50)
    pk_column=models.CharField(max_length=250,blank=True, null=True)

class dbconnection(models.Model):
    connection_name=models.CharField(max_length=200,unique=True)
    db_name=models.CharField(max_length=500)
    db_user_name=models.CharField(max_length=100)
    db_password=models.CharField(max_length=500)
    db_host_name=models.CharField(max_length=500)
    db_type=models.CharField(max_length=200)
    change_date=models.DateTimeField(auto_now=True)

class application(models.Model):
    application_name=models.CharField(max_length=200,unique=True)
    application_domain=models.CharField(max_length=500)
    application_owner=models.CharField(max_length=100)
    application_team_dl=models.CharField(max_length=500)
    change_date=models.DateTimeField(auto_now=True)

class testresult(models.Model):
    testcases_id=models.IntegerField()
    source_result =models.CharField(max_length=500)
    target_result =models.CharField(max_length=500)
    change_date=models.DateTimeField(auto_now=True)


class tcresultview(models.Model):
    appname=models.CharField(max_length=100)
    testcase_desc=models.CharField(max_length=500)
    source_result =models.CharField(max_length=500)
    target_result =models.CharField(max_length=500)
    result_desc =models.CharField(max_length=500)
    change_date=models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'raindrop_testresult_view'


class testtype(models.Model):
    result_type =models.CharField(max_length=500)

class testrescompare(models.Model):
    testcases_id=models.IntegerField()
    result_column =models.CharField(max_length=50)
    pk_column =models.CharField(max_length=50)
    pk_value=models.CharField(max_length=500)
    result_desc=models.CharField(max_length=50)
    source_result =models.CharField(max_length=500,blank=True, null=True)
    target_result =models.CharField(max_length=500,blank=True, null=True)
    change_date=models.DateTimeField(auto_now=True)

class tcrescompareview(models.Model):
    appname=models.CharField(max_length=100)
    testcase_desc=models.CharField(max_length=500)
    result_column =models.CharField(max_length=500)
    pk_column =models.CharField(max_length=500)
    pk_value =models.CharField(max_length=500)
    source_result =models.CharField(max_length=500)
    target_result =models.CharField(max_length=500)
    result_desc =models.CharField(max_length=500)
    change_date=models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'raindrop_testrescompare_view'