from datetime import date
import sqlite3
import pandas as pd
import time
import random
from random import randint
from datetime import datetime
import mysql.connector
import calendar
mydb = mysql.connector.connect(host="remotemysql.com", user="QxKi8MQlUR",
                               passwd="Kf0GcKV5sh", port=3306, database="QxKi8MQlUR")
mycursor = mydb.cursor()


def main():
    print("="*20, "GIHS AIRLINE", "="*20)
    print("\n", "="*8, "MAIN MENU", "="*8, "\n")

    print("OPTION 1: NEW BOOKING")
    print("OPTION 2: FLIGHT STATUS")
    print("OPTION 3: MANAGE BOOKINGS")
    print("OPTION 4: STAFF LOGIN")
    print("OPTION 5: ABOUT")
    print("OPTION 6: EXIT")

    while True:
        response = input("\nENTER OPTION NUMBER: ")
        if response == "1":
            NEW_BOOKING()
            break
        elif response == "2":
            FLIGHT_STATUS()
            break
        elif response == "3":
            MANAGE_BOOKINGS()
            break
        elif response == "4":
            STAFF_LOGIN()
            break
        elif response == "5":
            ABOUT()
            break
        elif response == "6":
            break
        else:
            print("="*20, "ENTER VALID OPTION", "="*20)


def NEW_BOOKING():

    def dep_arrival_input():
        print("\n", "="*8, "NEW BOOKING", "="*8)
        print("\n", "="*4, "DEPATURE", "="*4)
        print("\nCODE DXB: Dubai International Airport")
        print("CODE JFK: John F. Kennedy International Airport")
        print("CODE LHR: Heathrow Airport")
        print("CODE BOM: Chhatrapati Shivaji Maharaj International Airport")
        print("CODE SYD: Sydney Airport")
        list = ['DXB', 'JFK', 'LHR', 'BOM', 'SYD']
        global dep
        while True:
            dep = input('\nEnter the Respective Code: ')
            dep = dep.strip()
            dep = dep.upper()
            if dep in list:
                break
            else:
                print("\n", "="*4, 'Please Enter a Valid code', "="*4)
                pass

        index = list.index(dep)
        list.remove(dep)
        list2 = [
            "Dubai International Airport",
            "John F. Kennedy International Airport",
            "Heathrow Airport",
            "Chhatrapati Shivaji Maharaj International Airport",
            "Sydney Airport"
        ]
        list2.pop(index)

        print("\n", "="*4, "ARRIVAL", "="*4)
        for i in range(0, len(list)):
            p_command = "CODE {}: {}".format(list[i], list2[i])
            print(p_command)
        global arr
        while True:
            arr = input('\nEnter the Respective Code: ')
            arr = arr.strip()
            arr = arr.upper()
            if arr in list:
                break
            else:
                print("\n", "="*4, 'Please Enter a Valid code', "="*4)
                pass

    def addYears(d, years):
        global f_date
        try:
            f_date = d.replace(year=d.year+years)
            print(f_date)
        except ValueError:
            f_date = d + (date(d.year+years, 1, 1)-date(d.year, 1, 1))
            print(f_date)

    def string_to_date(datee):
        year = int(datee[0:4])
        month = int(datee[5:7])
        day = int(datee[8:])

        global depature_date
        global day_week
        depature_date = date(year, month, day)
        day_week = depature_date.weekday()
        day_week = calendar.day_name[day_week]
        if day_week.upper()[0] == "T":
            day_week = day_week.upper()[0:4]
        else:
            day_week = day_week.upper()[0:3]
        print(day_week)

    def date_input():
        current_date = date.today()
        addYears(current_date, 1)
        global depature_date
        while True:
            depature_date = input("\nENTER DEPATURE DATE (YYYY-MM-DD): ")
            depature_date.strip()
            if depature_date[4] != "-" or depature_date[7] != "-" or len(depature_date) != 10:
                print("\n", "="*4, 'Please Enter a Valid Date ', "="*4)
            elif depature_date[5:7] > "12" or depature_date[-2:] > "31":
                print("\n", "="*4, 'Please Enter a Valid Date ', "="*4)
            elif depature_date[5:7] in ["04", "06", "09", "11"] and depature_date[-2:] > "30":
                print("\n", "="*4, 'Please Enter a Valid Date ', "="*4)
            elif depature_date[5:7] == "02" and int(depature_date[0:4]) % 4 != 0 and depature_date[-2:] > "28":
                print("\n", "="*4, 'Please Enter a Valid Date ', "="*4)
            elif depature_date[5:7] == "02" and int(depature_date[0:4]) % 4 == 0 and depature_date[-2:] > "29":
                print("\n", "="*4, 'Please Enter a Valid Date ', "="*4)
            elif str(current_date) <= depature_date and str(f_date) > depature_date:
                dep_date = depature_date
                break
            else:
                print("\n", "="*4, 'Please Enter a Valid Date ', "="*4)

        string_to_date(depature_date)

    def flights_extract():
        while True:
            date_input()
            query = "select * from SCHEDULE"
            mycursor.execute(query)
            res = mycursor.fetchall()
            if res == []:
                query = "select FLIGHT_NO,ORIGIN,DESTINATION,DEPATURE_TIME,ARRIVAL_TIME,DAY from ROUTES where ORIGIN='{}' AND DESTINATION='{}'".format(
                    dep, arr)
                mycursor.execute(query)
                list = mycursor.fetchall()
                global df

                df = pd.DataFrame(list,columns=[
                        "flight_no", "origin", "dest", "dep_time", "arr_time", "days"])

        
                for i in range(len(df["days"])):
                    if day_week in df["days"][i] or df["days"][i] == "DAILY":
                        pass
                    else:
                        df = df.drop([i], axis=0)
                
                
                if df.empty:

                    query = "select FLIGHT_NO,ORIGIN,DESTINATION,DEPATURE_TIME,ARRIVAL_TIME,DAY from ROUTES where ORIGIN='{}' AND DESTINATION='DXB'".format(
                        dep)
                    mycursor.execute(query)
                    res = mycursor.fetchall()
                    df=pd.DataFrame(res, columns=[
                        "flight_no", "origin", "dest", "dep_time", "arr_time", "days"])
                    for i in range(len(df["days"])):
                        if day_week in df["days"][i] or df["days"][i] == "DAILY":
                            pass
                        else:
                            df = df.drop([i], axis=0)
                    if df.empty:
                        print("\n", "="*4, 'NO FLIGHTS AVAILABLE', "="*4,"\n")
                        print()


                    else:
                        query = "select FLIGHT_NO,ORIGIN,DESTINATION,DEPATURE_TIME,ARRIVAL_TIME,DAY from ROUTES where ORIGIN='DXB' AND DESTINATION='{}'".format(
                            arr)
                        mycursor.execute(query)
                        for i in mycursor.fetchall():
                            res.append(i)
                        
                        

                        df=pd.DataFrame(res, columns=[
                            "flight_no", "origin", "dest", "dep_time", "arr_time", "days"])



            #dep_time=df.iat[0,3]
            #arr_time=df.iat[0,4]


    dep_arrival_input()
    flights_extract()

def FLIGHT_STATUS():
    print("="*8, "FLIGHT STATUS", "="*8)


def MANAGE_BOOKINGS():
    print("="*8, "MANAGE BOOKINGS", "="*8)


def STAFF_LOGIN():
    print("="*8, "STAFF LOGIN", "="*8)


def ABOUT():
    print("="*8, "ABOUT", "="*8)


NEW_BOOKING()
