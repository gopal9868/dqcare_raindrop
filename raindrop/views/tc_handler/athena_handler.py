
from pyathena import connect
import pandas as pd
from pyathena.pandas.cursor import PandasCursor
from .final_df_untility import final_df_convert
def tc_athena_handler(conn_dtl,sqlqry,id):
    #print(conn_dtl)
    cursor = connect(aws_access_key_id=conn_dtl['AK'],
                 aws_secret_access_key=conn_dtl['SK'],
                 s3_staging_dir=conn_dtl['SD'],
                 region_name=conn_dtl['AR']).cursor()

    cursor.execute(sqlqry)
    data=cursor.fetchone()[0]
    #print(cursor.fetchall()[0])
    cursor.close()
    return(data)
def tc_athena_handler_2(conn_dtl,sqlqry,pk_column):
    cursor = connect(aws_access_key_id=conn_dtl['AK'],
                   aws_secret_access_key=conn_dtl['SK'],
                  s3_staging_dir=conn_dtl['SD'],
                 region_name=conn_dtl['AR'],
                 cursor_class=PandasCursor).cursor()
    df = cursor.execute(sqlqry).as_pandas()
    cursor.close()
    final_df=final_df_convert(df,pk_column)
    return final_df