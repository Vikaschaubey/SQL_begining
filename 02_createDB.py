import pymysql as sq
myobj=sq.connect(host="localhost",user="root",password="")
cobj=myobj.cursor()
try:
    db="create database college"
    cobj.execute(db)
    print("Database Created")

except:
    print("Database Error")