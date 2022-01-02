
from django.shortcuts import render
from django.http import HttpResponse
import time
def create_file1(request,id):
    try:
        with open ('C:/web_development/code/python/test.txt','w') as f1:
            time.sleep(0)
            response = HttpResponse('File created')
    except Exception as e:
        response=HttpResponse(e)
    return response