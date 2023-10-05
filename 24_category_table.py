import pymysql as mq
myobj=mq.connect(host="localhost",user="root",password="", database="college")
cur = myobj.cursor()
try:
    sql_query="create table categories(cat_id INT PRIMARY KEY auto_increment,cat_name varchar(30), parent_id INT )"
    cur.execute(sql_query)
    print("Table created")
except:
    print("Table already exist")
