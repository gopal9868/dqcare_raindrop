from .script_creation_path import script_path,api_url
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
exe_api=f'response=requests.get({api_url}'
resprint="print (response)"

@csrf_exempt
def gen_schedule_script(request):
     script_name=script_path+'test_schedule_script.py'
     x=json.loads(request.body)
     #od = collections.OrderedDict(sorted(x.items()))
     od=dict(sorted(x.items()))
     print(od)
     restext='import requests'+'\n'
     for k,v in od.items():
       restext='\n'+restext+exe_api+str(v)+'")\n'+resprint+'\n'
     with open(script_name,'w') as f1:
      f1.write(restext)
     response = HttpResponse(script_name+' File created')
     return(response)
