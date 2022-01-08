
from raindrop.models import testcases
from django.shortcuts import render
from django.http import HttpResponse
from .get_db_conn_details import db_conn
from .tc_capture_handler import tc_capture_result
def get_conn_dtl(request,id):
    global src_conn_name
    global tgt_conn_name
    global src_query
    global tgt_query
    global res_type
    global pk_column
    global src_conn_name
    global src_conn_dtl
    global tgt_conn_name
    global tgt_conn_dtl
    #print(id)
    sqlqry=f"SELECT source_query,target_query,source_connection_name, target_connection_name,result_type,pk_column,id FROM raindrop_testcases where id={id}"
    for p in testcases.objects.raw(sqlqry):
      src_conn_name=p.source_connection_name
      tgt_conn_name=p.target_connection_name
      src_query=p.source_query
      tgt_query=p.target_query
      res_type=p.result_type
      pk_column=p.pk_column
    for key, value in db_conn.items():
           #print(key)
           if src_conn_name==key:
              #print(value)
              src_conn_dtl=value
           if tgt_conn_name==key:
             tgt_conn_dtl=value
    tc_capture_result(src_conn_dtl,tgt_conn_dtl,src_query,tgt_query,id,res_type,pk_column)
    response = HttpResponse('Testcase Executed')
    return response