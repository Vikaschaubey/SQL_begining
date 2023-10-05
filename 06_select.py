import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
print("{:<15} {:<20} {:<20} {:<10}".format("Student Id","Student Name", "Student Email", "Student Class"))
try:
    query="select * from student"
    cur.execute(query)
    s=cur.fetchall()
    for i in s:
        print("{:<15} {:<20} {:<20} {:<10}".format(i[0],i[1],i[3],i[2]))
    
except:
    print("error")
