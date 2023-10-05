import pymysql as mq
myobj=mq.connect(host="localhost",user="root",password="", database="college")
cur = myobj.cursor()
print("{:<20}{:<20}{:<20}".format("State_id","State_name","Country_id"))
sql="select * from state order by country_id ASC LIMIT 2,3" #  2 show the starting position and  3 show the number of row
try:
    cur.execute(sql)
    a= cur.fetchall()
    for i in a:
        print("{:<20}{:<20}{:<20}".format(i[0],i[1],i[2]))
except:
    print("Error")
