import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
try:
    query="select min(country_id) from state "
    cur.execute(query)
    s=cur.fetchall()
    for i in s:
        print(i)
    
except:
    print("error")
