import mysql.connector
from mysql.connector import Error
from .data_file_location import data_location
from sqlalchemy import create_engine
import pandas as pd
from .final_df_untility import final_df_convert
def tc_mysql_handler(conn_dtl,sqlqry,id):
    


 try:
    connection = mysql.connector.connect(host=conn_dtl['host'],
                                         database=conn_dtl['db_name'],
                                         user=conn_dtl['user_name'],
                                         password=conn_dtl['password'])
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute(sqlqry)
        record = cursor.fetchone()
        #print("your output is", record)
        return (record[0])

 except Error as e:
    print("Error while connecting to MySQL", e)
 finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


def tc_mysql_handler_2(conn_dtl,sqlqry,pk_column):
    
 db_connection_str = 'mysql+pymysql://'+conn_dtl['user_name']+':'+conn_dtl['password']+'@'+conn_dtl['host']+'/'+conn_dtl['db_name']
 #print(db_connection_str)
 mysql_db_connection = create_engine(db_connection_str)
 df = pd.read_sql(sqlqry, con=mysql_db_connection)
 final_df=final_df_convert(df,pk_column)
 #mysql_db_connection.close()
 return final_df