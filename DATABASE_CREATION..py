import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(host="remotemysql.com",user="QxKi8MQlUR",passwd="Kf0GcKV5sh",port=3306,database="QxKi8MQlUR")
mycursor=mydb.cursor()

df=pd.read_excel("Flight_schedule.xlsx")
print(df)
