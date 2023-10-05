import pymysql as mq
myobj=mq.connect(host="localhost",user="root",password="", database="college")
cur = myobj.cursor()
try:
    sql_query="create table student(stu_Id INT PRIMARY KEY auto_increment,stu_name varchar(30), stu_class varchar(10), stu_email varchar(50) )"
    cur.execute(sql_query)
    print("Table created")
except:
    print("Table already exist")
