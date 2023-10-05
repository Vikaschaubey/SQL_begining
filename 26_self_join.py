import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()

try:
    sql="select * from categories as c1, categories as c2 where c1.cat_id=c2.parent_id"
    cur.execute(sql)
    s=cur.fetchall()
    for i in s:
        print(i)
        #print("{:<15} {:<20} {:<20}".format(i[0],i[1],str(i[2])))
except:
    print("Error")
    

