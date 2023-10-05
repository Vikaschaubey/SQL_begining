import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur = mysql.cursor()

try:
    query="INSERT INTO student(stu_name,stu_class,stu_email) values(%s,%s,%s)"
    t=[("abhi","11th","abhi@gmail.com"),("Vicky","10th","vicky@gmail.com"),("amit","10th","amit@gmail.com")]
    cur.executemany(query,t)
    mysql.commit()
    print("Row inserted")
except:
    print("Error in insertion")