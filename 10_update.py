import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
s_name=input("Enter the name : ")
classname=input("Enter the class  : ")
id=input("Enter the id : ")
try:
    sql="UPDATE student set stu_name=%s, stu_class=%s WHERE stu_id=%s"
    data=(s_name,classname,id) 
    cur.execute(sql,data)
    mysql.commit()
    print("query update")
except:
    print("Error")