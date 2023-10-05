import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
print("{:<20}".format("department_name"))
try:
    query="select distinct dname from office "
    cur.execute(query)
    s=cur.fetchall()
    for i in s:
        print("{:<20} ".format(i[0]))
    
except:
    print("error")
