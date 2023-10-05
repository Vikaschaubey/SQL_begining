import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
n=int(input("Enter the id : "))
try:
    query="delete from student where stu_id=%s"
    cur.execute(query,n)
    mysql.commit()
    print("Row deleted")
except:
    print("Error")