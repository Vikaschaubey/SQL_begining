import pymysql as mq
myobj=mq.connect(host="localhost",user="root",password="")
cursorobj=myobj.cursor()