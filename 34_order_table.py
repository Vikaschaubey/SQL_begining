import pymysql as mq
myobj=mq.connect(host="localhost",user="root",password="", database="college")
cur = myobj.cursor()
try:
    sql_query="create table order(order_id INT PRIMARY KEY auto_increment,user_id int, order_amt int)"
    cur.execute(sql_query)
    print("Table created")
except:
    print("Table already exist")
