import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="", database="college")
cur=mysql.cursor()
sql="create table country(country_id INT PRIMARY KEY auto_increment, country_name varchar(30))"
try:
    cur.execute(sql)
    mysql.commit()
    print("Table created")
except:
    print("Error")