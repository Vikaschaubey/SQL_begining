import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
print("{:<20} {:<20}".format("count","department_name"))
try:
    query="select count(*), dname from office group by dname "
    cur.execute(query)
    s=cur.fetchall()
    for i in s:
        print("{:<20} {:<20}".format(i[0],i[1]))
    
except:
    print("error")
