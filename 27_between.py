import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
try:
    query="select * from state where state_id between 2 and 4"
    cur.execute(query)
    s=cur.fetchall()
    for i in s:
        print(i)
    
except:
    print("error")
