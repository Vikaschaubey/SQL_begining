import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
print("{:<15} {:<20}".format("Student Name","Student Class"))
try:
    query="select stu_name, stu_class from student"
    cur.execute(query)
    s=cur.fetchall()
    for i in s:
        print("{:<15} {:<20}".format(i[0],i[1]))
    
except:
    print("error")
