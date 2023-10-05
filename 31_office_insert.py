import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur = mysql.cursor()

try:
    query="INSERT INTO office(ename,dname) values(%s,%s)"
    t=[("ADAMS","CLERK"),("ALLEN","SALESMAN"),("BLAKE","MANAGER"),("CLARK","MANAGER"),("FORD","ANALYST"),("JAMES","CLERK"),("JONES","MANAGER"),("KING","PRESIDENT"),("MARTIN","SALESMAN"),("MILLER","CLERK"),("SCOTT","ANALYST"),("SMITH","CLERK"),("TURNER","SALESMAN"),("WARD","SALESMAN")]
    cur.executemany(query,t)
    mysql.commit()
    print("Row inserted")
except:
    print("Error in insertion")