import pymysql as mq
myobj=mq.connect(host="localhost",user="root",password="", database="college")
cur = myobj.cursor()
try:
    sql="create table state(state_id int primary key,state_name varchar (20),country_id int)"
    cur.execute(sql)
    myobj.commit()
    print("Table created")
except:
    print("Error")