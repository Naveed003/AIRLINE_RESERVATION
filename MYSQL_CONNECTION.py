import mysql.connector
import pandas as pd 
mydb=mysql.connector.connect(host="remotemysql.com",user="QxKi8MQlUR",passwd="Kf0GcKV5sh",port=3306,database="QxKi8MQlUR")
mycursor=mydb.cursor()

query="select * from ROUTES"
mycursor.execute(query)
for i in mycursor.fetchall():
    print(i)
    
    
mydb.close()

