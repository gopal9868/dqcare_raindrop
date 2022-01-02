from .tc_repo_config  import tc_repo_db
import mysql.connector
from mysql.connector import Error
import pandas as pd
import datetime
from sqlalchemy import create_engine
import numpy as np
def write_to_repo_db_compare_1(source_df,target_df,pk_column,id):
    pk_col='pk_id'
    #print(pk_column)
    #=pk_column.split(',')
    src_tgt_data=pd.merge(source_df,target_df,on=pk_col,how='outer')
    print(src_tgt_data)
    #print(source_df.columns)
    for col in source_df.columns:
        if col !=pk_col:
            check_col=col
            break
    #print(check_col)
    result_df = pd.DataFrame(columns = ['pk_value', 'target_result', 'source_result','testcases_id','pk_column','result_column','result_desc','change_date'])
    # identify missing records in source
    ts2=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    source_miss_df=src_tgt_data.loc[src_tgt_data[check_col+'_x'].isnull(),[pk_col]]
    #print(source_miss_df)
    source_miss_df.rename(columns = {pk_col:'target_result'}, inplace = True)
    source_miss_df['testcases_id'],source_miss_df['pk_column'],source_miss_df['result_column'],source_miss_df['result_desc'],source_miss_df['source_result'],source_miss_df['change_date']= [id, pk_column,pk_column,'missing_in_source',None,ts2]
    source_miss_df['pk_value']=source_miss_df['target_result']
    #print(source_miss_df)
    # identify missing records in target
    target_miss_df=src_tgt_data.loc[src_tgt_data[check_col+'_y'].isnull(),[pk_col]]
    target_miss_df.rename(columns = {pk_col:'source_result'}, inplace = True)
    ts1=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    target_miss_df['testcases_id'],target_miss_df['pk_column'],target_miss_df['result_column'],target_miss_df['result_desc'],target_miss_df['target_result'],target_miss_df['change_date']= [id, pk_column,pk_column,'missing_in_target',None,ts1]
    target_miss_df['pk_value']=target_miss_df['source_result']
    ts3=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #identify mismatch records
    #src_tgt_mismatch_df = pd.DataFrame(columns = ['testcases_id', 'pk_column','pk_value', 'result_column','result_desc','source_result','target_result','change_date'])
    column_list=list(source_df.columns)
    #pk_column_list=pk_column.split(',')
    #column_test=list(set(column_list) - set(pk_col))
    #print(column_list)
    column_list.remove(pk_col)
    #print(column_test)
    #print(src_tgt_data)
    #print(src_tgt_data[['score_y','id','score_x']].loc[(src_tgt_data['score_x'].notnull()) & (src_tgt_data['score_y'].notnull()) & (src_tgt_data['score_y']!=src_tgt_data['score_x'])])
    #print(np.where(src_tgt_data['name_x'].notnull()),src_tgt_data['name_x'])
    #print(src_tgt_data)
    #print(src_tgt_data[src_tgt_data['score_x'].notnull() & src_tgt_data['score_y'] & src_tgt_data['score_x']!=src_tgt_data['score_y'] ])
    for col in column_list:
          #print(col)
          mismatch_df=src_tgt_data[[pk_col,col+'_x',col+'_y']].loc[(src_tgt_data[col+'_x'].notnull()) & (src_tgt_data[col+'_y'].notnull()) & (src_tgt_data[col+'_y']!=src_tgt_data[col+'_x'])]
          mismatch_df.rename(columns = {pk_col:'pk_value',col+'_x':'source_result',col+'_y':'target_result'}, inplace = True)
          mismatch_df['testcases_id'],mismatch_df['pk_column'],mismatch_df['result_column'],mismatch_df['result_desc'],mismatch_df['change_date']= [id, pk_column,col,'source_target_mismatch',ts3]
          #print(mismatch_df['pk_column')
          result_df=result_df.append(mismatch_df,ignore_index=True)
          #src_tgt_mismatch_df=pd.concat(mismatch_df)
          #mismatch_df['pk_value'] = src_tgt_data.loc[src_tgt_data[col+'_x'] != src_tgt_data[col+'_y'] and src_tgt_data[col+'_x'].notna and src_tgt_data[col+'_y'].notna, [pk_column]]
          #print(mismatch_df)
    #result_df=result_df.append(source_miss_df,ignore_index=True)
    #result_df=result_df.append(target_miss_df,ignore_index=True)
    #print(result_df)     
    frames=[source_miss_df,target_miss_df,result_df]
    result_df=pd.concat(frames)
    print(result_df)
    conn=create_mysql_connect_tcrepo()
    delete_sql=f"delete from raindrop_testrescompare where testcases_id={id}"
    conn.execute(delete_sql)
    result_df.to_sql(con=conn, name='raindrop_testrescompare', if_exists='append',index=False)
    print(" compare data inserted")

def create_mysql_connect_tcrepo():
    db_connection_str = 'mysql+pymysql://'+tc_repo_db['user_name']+':'+tc_repo_db['password']+'@'+tc_repo_db['host']+'/'+tc_repo_db['db_name']
    mysql_db_connection = create_engine(db_connection_str)
    return mysql_db_connection

