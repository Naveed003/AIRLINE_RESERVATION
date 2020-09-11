import mysql.connector
import pandas as pd 
mydb=mysql.connector.connect(host="remotemysql.com",user="QxKi8MQlUR",passwd="Kf0GcKV5sh",port=3306,database="QxKi8MQlUR")
mycursor=mydb.cursor()


query="select arrival_time from ROUTES"
mycursor.execute(query)
list=mycursor.fetchall()
df=pd.DataFrame(list,columns=["flight_no"])
a=df.loc[1]
b=df.loc[0]
print(b)
print(a-b)


    
    
mydb.close()

