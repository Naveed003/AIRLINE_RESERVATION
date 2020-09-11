import mysql.connector
import pandas as pd 
mydb=mysql.connector.connect(host="remotemysql.com",user="QxKi8MQlUR",passwd="Kf0GcKV5sh",port=3306,database="QxKi8MQlUR")
mycursor=mydb.cursor()


mycursor.execute("select * from SCHEDULE")
print(mycursor.fetchall())

mycursor.execute("select FLIGHT_NO,ORIGIN,DESTINATION from ROUTES")
lis=mycursor.fetchall()
df=pd.DataFrame(lis,columns=["FLIGHT_NO","ORIGIN","DESTINATION"])
print(df)
mydb.close()

