from .tc_handler.mysql_handler import tc_mysql_handler,tc_mysql_handler_2
from .tc_handler.athena_handler import tc_athena_handler,tc_athena_handler_2
from .tc_repo.tc_repo_db_writer_1 import write_to_repo_db_1
from .tc_repo.tc_repo_db_writer_compare import write_to_repo_db_compare_1
def tc_capture_result(src_conn_dtl,tgt_conn_dtl,src_query,tgt_query,id,res_type,pk_column):
    if(src_conn_dtl['db_type']=='mysql' and res_type != 'compare'):
       data=tc_mysql_handler(src_conn_dtl,src_query,id)
       write_to_repo_db_1(data,id,'source')
    if(src_conn_dtl['db_type']=='Athena' and res_type != 'compare'):
       data=tc_athena_handler(src_conn_dtl,src_query,id)
       write_to_repo_db_1(data,id,'source')
    if(tgt_conn_dtl['db_type']=='mysql' and res_type != 'compare'):
       data=tc_mysql_handler(tgt_conn_dtl,tgt_query,id)
       write_to_repo_db_1(data,id,'target')
    if(tgt_conn_dtl['db_type']=='Athena' and res_type != 'compare'):
       data=tc_athena_handler(tgt_conn_dtl,tgt_query,id)
       write_to_repo_db_1(data,id,'target')
    if(src_conn_dtl['db_type']=='mysql' and res_type == 'compare'):
       source_df=tc_mysql_handler_2(src_conn_dtl,src_query,pk_column)
    if(tgt_conn_dtl['db_type']=='mysql' and res_type == 'compare'):
       tgt_df=tc_mysql_handler_2(tgt_conn_dtl,tgt_query,pk_column)
    if(src_conn_dtl['db_type']=='Athena' and res_type == 'compare'):
       source_df=tc_athena_handler_2(src_conn_dtl,src_query,pk_column)
       #print(source_df)
    if(tgt_conn_dtl['db_type']=='Athena' and res_type == 'compare'):
       tgt_df=tc_athena_handler_2(tgt_conn_dtl,tgt_query,pk_column)
    if(res_type=='compare'):
      write_to_repo_db_compare_1(source_df,tgt_df,pk_column,id)
       #print(source_df)
