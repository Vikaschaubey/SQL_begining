import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur = mysql.cursor()

try:
    query="INSERT INTO student(stu_name,stu_class,stu_email) values(%s,%s,%s)"
    t=[("Vikash","12th","vikas@gmail.com")]
    cur.execute(query,t)
    mysql.commit()
    print("Row inserted")
except:
    print("Error in insertion")