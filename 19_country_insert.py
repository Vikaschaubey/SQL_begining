import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="", database="college")
cur=mysql.cursor()
sql="INSERT INTO country(country_name) values(%s)"
t=[("india"),("australia"),("England")]
try:
    cur.executemany(sql,t)
    mysql.commit()
    print("Inserted")
except:
    print('error')