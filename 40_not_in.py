import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
print("{:<20}{:<20}{:<20}".format("order id","user id","Amount"))
try:
    query="select * from orders where order_id not in(1,6) "
    cur.execute(query)
    s=cur.fetchall()
    for i in s:
        print("{:<20}{:<20}{:<20}".format(i[0],i[1],i[2]))
    
except:
    print("error")
