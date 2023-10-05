import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur = mysql.cursor()

try:
    query="INSERT INTO state(state_id,state_name,country_id) values(%s,%s,%s)"
    t=[(1,"Delhi",3),(2,"Goa",4),(3,"UP",1),(4,"Bihar",8),(5,"MP",7),(6,"Punjab",2)]
    cur.executemany(query,t)
    mysql.commit()
    print("Row inserted")
except:
    print("Error in insertion")