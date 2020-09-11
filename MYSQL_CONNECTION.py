import mysql.connector
import pandas as pd 
mydb=mysql.connector.connect(host="remotemysql.com",user="QxKi8MQlUR",passwd="Kf0GcKV5sh",port=3306,database="QxKi8MQlUR")
mycursor=mydb.cursor()


query="select FLIGHT_NO,ORIGIN,DESTINATION,DAY from ROUTES where ORIGIN='DXB' AND DESTINATION='LHR'"
mycursor.execute(query)
list=mycursor.fetchall()
df=pd.DataFrame(list,columns=["flight_no","origin","dest","days"])
indexs=[]
for i in range(len(df["days"])):
    if "MON" in df["days"][i]:
        indexs.append(i)
        print(df["days"][i])
        df=df.drop([i],axis=0)

print(df)

    
    
mydb.close()

