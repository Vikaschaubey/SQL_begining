import pymysql as mq
myobj=mq.connect(host="localhost",user="root",password="", database="college")
cur = myobj.cursor()
name=input("Enter the name: ")
print("{:<20}{:<20}{:<20}".format("State_id","State_name","Country_id"))
sql="select * from state where state_name LIKE '%"+name+"%'" 

#sql="select * from state where state_name LIKE '"+name+"%'"
# start with input character
#sql="select * from state where state_name LIKE '%"+name+"'" End with input character
#sql="select * from state where state_name LIKE '%"+name+"%'"
#Input char in between 

try:
    cur.execute(sql)
    a= cur.fetchall()
    for i in a:
        print("{:<20}{:<20}{:<20}".format(i[0],i[1],i[2]))
except:
    print("Error")
