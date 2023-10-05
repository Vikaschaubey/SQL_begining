import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="college")
cur=mysql.cursor()
print("{:<15} {:<20} {:<20}".format("State_id","State name","Country name"))
try:
    query="select state.state_id, state.state_name, country.country_name from state INNER JOIN country ON state.country_id=country.country_id"
    cur.execute(query)
    s=cur.fetchall()
    for i in s:
        print("{:<15} {:<20} {:<20}".format(i[0],i[1],i[2]))
    
except:
    print("error")
