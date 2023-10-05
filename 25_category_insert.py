import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur = mysql.cursor()

try:
    query="INSERT INTO categories(cat_name,parent_id) values(%s,%s)"
    t=[("Mens",0),("Women",0),("Shirt",1),("Shoes",1),("Jewellery",2)]
    cur.executemany(query,t)
    mysql.commit()
    print("Row inserted")
except:
    print("Error in insertion")