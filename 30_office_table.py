import pymysql as mq
myobj=mq.connect(host="localhost",user="root",password="", database="college")
cur = myobj.cursor()
try:
    sql_query="create table office(empno INT PRIMARY KEY auto_increment,ename varchar(30), dname varchar(20))"
    cur.execute(sql_query)
    print("Table created")
except:
    print("Table already exist")
