import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
print("{:<15} {:<20} {:<20}".format("State_id","State name","Country name"))
try:
    sql="select state_id, state_name, country_name  from state,country where state.country_id=country.country_id"
    cur.execute(sql)
    s=cur.fetchall()
    for i in s:
        print("{:<15} {:<20} {:<20}".format(i[0],i[1],str(i[2])))
except:
    print("Error")
    

