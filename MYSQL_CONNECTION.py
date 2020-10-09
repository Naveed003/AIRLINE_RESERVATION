import mysql.connector
import pandas as pd 
mydb=mysql.connector.connect(host="remotemysql.com",user="QxKi8MQlUR",passwd="Kf0GcKV5sh",port=3306,database="QxKi8MQlUR")
mycursor=mydb.cursor()
query="show COLUMNS FROM BOOKINGS"

mycursor.execute(query)

RES=mycursor.fetchall()
RES=pd.DataFrame(RES)
print(RES.iloc[1,0])