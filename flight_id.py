def F_n():
    global B
    import random
    import json
    with open('flight_Numbers.txt', 'r') as f:
        flight_Numbers = json.loads(f.read())
    while True:
        B=random.randint(100,999)
        if B in flight_Numbers:
            print(B)
            pass
        else:
            flight_Numbers.append(B)
            
            with open('flight_Numbers.txt', 'w') as f:
                f.write(json.dumps(flight_Numbers))
            
            
            break

def extract_flight_no():
    import mysql.connector
    mydb=mysql.connector.connect(host="remotemysql.com",user="QxKi8MQlUR",passwd="Kf0GcKV5sh",port=3306,database="QxKi8MQlUR")
    mycursor=mydb.cursor()
    QUERY="SELECT FLIGHT_NO FROM ROUTES"
    mycursor.execute(QUERY)
    res=mycursor.fetchall()
    list=[]
    for i in res:
        for j in i:
            j=str(j)
            j=j.lstrip("G")
            j=int(j)
            if j not in list:
                list.append(j)


    print(list)

    mydb.close()
 

    

