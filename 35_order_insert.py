import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur = mysql.cursor()

try:
    query="INSERT INTO orders(user_id,order_amt) values(%s,%s)"
    t=[(1,5000),(4,2000),(2,6000),(5,4000),(2,4000),(3,4000),(3,4000)]
    cur.executemany(query,t)
    mysql.commit()
    print("Row inserted")
except:
    print("Error in insertion")