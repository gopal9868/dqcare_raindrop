from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import testcases,dbconnection,application,tcresultview,testtype,testrescompare,tcrescompareview
from rest_framework.validators import UniqueValidator
class testcasesserializer(serializers.ModelSerializer):
    class Meta:
        model=testcases
        fields='__all__'
class dbconnectionserializer(serializers.ModelSerializer):
    connection_name = serializers.CharField(validators=[
        UniqueValidator(
            queryset=dbconnection.objects.all(),
            message='This connection already exists'
        )]
    )
    class Meta:
        model=dbconnection
        fields='__all__'
class applicationserializer(serializers.ModelSerializer):
    application_name = serializers.CharField(validators=[
        UniqueValidator(
            queryset=application.objects.all(),
            message='This application already exists'
        )]
    )
    class Meta:
        model=application
        fields='__all__'
class Appnameserializer(serializers.ModelSerializer):
    class Meta:
        model=application
        fields=('application_name',)
class Connnameserializer(serializers.ModelSerializer):
    class Meta:
        model=dbconnection
        fields=('connection_name',)
class Tcresultviewserializer(serializers.ModelSerializer):
    class Meta:
        model=tcresultview
        fields='__all__'

class Resulttypeserializer(serializers.ModelSerializer):
    class Meta:
        model=testtype
        fields='__all__'

class Tcrescompare(serializers.ModelSerializer):
    class Meta:
        model=testrescompare
        fields='__all__'
class Tcrescompareviewserializer(serializers.ModelSerializer):
    class Meta:
        model=tcrescompareview
        fields='__all__'
