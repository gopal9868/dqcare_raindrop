from rest_framework import viewsets
from . import models
from .serializer import testcasesserializer,dbconnectionserializer,applicationserializer,Appnameserializer,Connnameserializer,Tcresultviewserializer,Resulttypeserializer,Tcrescompareviewserializer
from raindrop import serializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class testcasesviewset(viewsets.ModelViewSet):
    queryset=models.testcases.objects.all()
    serializer_class=serializer.testcasesserializer
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    filter_fields=('appname','testcase_desc',)
    search_fields=['appname','testcase_desc']
class dbconnectionviewset(viewsets.ModelViewSet):
    queryset=models.dbconnection.objects.all()
    serializer_class=serializer.dbconnectionserializer
    #filter_backends=(DjangoFilterBackend,)
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    filter_fields=('connection_name','db_type',)
    search_fields=['connection_name','db_type']

class applicationviewset(viewsets.ModelViewSet):
    queryset=models.application.objects.all()
    serializer_class=serializer.applicationserializer
    filter_backends=[filters.SearchFilter]
    search_fields=['application_name']
class Appnameviewset(viewsets.ModelViewSet):
    queryset=models.application.objects.only('application_name')
    serializer_class=serializer.Appnameserializer
class Connnameviewset(viewsets.ModelViewSet):
    queryset=models.dbconnection.objects.only('connection_name')
    serializer_class=serializer.Connnameserializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('db_type',)
class tcresultviewset(viewsets.ModelViewSet):
    queryset=models.tcresultview.objects.all()
    serializer_class=serializer.Tcresultviewserializer
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    filter_fields=('appname',)
    search_fields=['testcase_desc']

class Resulttypeviewset(viewsets.ModelViewSet):
    queryset=models.testtype.objects.only('result_type')
    serializer_class=serializer.Resulttypeserializer

class Tcrescompareviewset(viewsets.ModelViewSet):
    queryset=models.tcrescompareview.objects.all()
    serializer_class=serializer.Tcrescompareviewserializer
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    filter_fields=('appname',)
    search_fields=['testcase_desc']


    