from .tc_repo_config  import tc_repo_db
import mysql.connector
from mysql.connector import Error
import time
import datetime
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
def write_to_repo_db_1(record,id,result_origin):
 chk_qry=f"select max(id) id from bubble.raindrop_testresult where testcases_id={id}"
 try:
    connection = mysql.connector.connect(host=tc_repo_db['host'],
                                         database=tc_repo_db['db_name'],
                                         user=tc_repo_db['user_name'],
                                         password=tc_repo_db['password'])
    if connection.is_connected():
        print("Connected to MySQL DB")
        cursor = connection.cursor()
        cursor.execute(chk_qry)
        chk_record = cursor.fetchone()
        source_record=0
        target_record=0
        global val
        print(chk_record[0])
        print(result_origin)
        if result_origin=='source':
            source_record=record
        if result_origin=='target':
            target_record=record
        if chk_record[0] is None:
            ins_sql = "INSERT INTO bubble.raindrop_testresult (testcases_id,source_result,target_result,change_date) VALUES (%s,%s,%s,%s,%s)"
            val = (id,source_record,target_record,timestamp)
            cursor.execute(ins_sql, val)
            connection.commit()
        else:
            if result_origin=='source':
             upd_sql="UPDATE bubble.raindrop_testresult SET source_result = %s,change_date=current_timestamp WHERE testcases_id = %s"
             val = (source_record, id)
             cursor.execute(upd_sql, val)
             connection.commit()
             print("source updated")
            if result_origin=='target':
             print("target upd sec")
             upd_sql="UPDATE bubble.raindrop_testresult SET target_result = %s,change_date=current_timestamp WHERE testcases_id = %s"
             val = (target_record, id)
             cursor.execute(upd_sql, val)
             connection.commit()
             print("target updated")
        print("Test result is captured", record)

 except Error as e:
    print("Error while connecting to MySQL", e)
 finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
