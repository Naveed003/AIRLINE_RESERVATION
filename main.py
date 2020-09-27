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
            if len(depature_date) != 10:
                print("\n", "="*4, 'Please Enter a Valid Date ', "="*4)
            elif depature_date[4] != "-" or depature_date[7] != "-" or len(depature_date) != 10:
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

            def dir():
                query = "select * from SCHEDULE"
                mycursor.execute(query)
                res = mycursor.fetchall()
                if res == []:
                    query = "select FLIGHT_NO,ORIGIN,DESTINATION,DEPATURE_TIME,ARRIVAL_TIME,DAY from ROUTES where ORIGIN='{}' AND DESTINATION='{}'".format(
                        dep, arr)
                    mycursor.execute(query)
                    list = mycursor.fetchall()
                    global dirr
                    if list != []:
                        dirr = pd.DataFrame(list, columns=[
                            "flight_no", "origin", "dest", "dep_time", "arr_time", "days"])

                        for i in dirr.index:
                            if day_week in dirr["days"][i] or dirr["days"][i] == "DAILY":
                                pass
                            else:
                                dirr = dirr.drop([i], axis=0)

                    else:
                        dirr = pd.DataFrame()
                    return dirr

            def con():
                if arr == 'DXB':
                    arr_1 = "DXB_ARR"
                elif arr == 'BOM':
                    arr_1 = "BOM_ARR"
                elif arr == 'JFK':
                    arr_1 = "JFK_ARR"
                elif arr == 'SYD':
                    arr_1 = "SYD_ARR"
                elif arr == 'LHR':
                    arr_1 = "LHR_ARR"
                if dep == 'DXB':
                    dep_1 = "DXB_DEP"
                elif dep == 'BOM':
                    dep_1 = "BOM_DEP"
                elif dep == 'JFK':
                    dep_1 = "JFK_DEP"
                elif dep == 'SYD':
                    dep_1 = "SYD_DEP"
                elif dep == 'LHR':
                    dep_1 = "LHR_DEP"
                days = ["SUN", "MON", "TUES", "WED",
                        "THUR", "FRI", "SAT", "SUN"]
                days_index = days.index(day_week)
                query = "select * from SCHEDULE"
                mycursor.execute(query)
                res = mycursor.fetchall()
                if res == []:
                    query = 'select * from {},{} WHERE {}.DESTINATION = {}.ORIGIN AND {}.DEPATURE_TIME>{}.ARRIVAL_TIME'.format(
                        dep_1, arr_1, dep_1, arr_1, arr_1, dep_1)

                    mycursor.execute(query)
                    list = mycursor.fetchall()
                    global df
                    global df1
                    global df3
                    global conn
                    if list != []:

                        df = pd.DataFrame(list, columns=[
                            "flight_no", "origin", "dest", "dep_time", "arr_time", "days", "type", "duration", "flight_no1", "origin1", "dest1", "dep_time1", "arr_time1", "days1", "type1", "duration1"])

                        df1 = pd.concat([df["flight_no"], df["origin"], df["dest"],
                                         df["dep_time"], df["arr_time"], df["days"]], axis=1)
                        df2 = pd.concat([df["flight_no1"], df["origin1"], df["dest1"],
                                         df["dep_time1"], df["arr_time1"], df["days1"]], axis=1)
                        flight_no = []
                        for i in df1.index:
                            if df1["flight_no"][i] in flight_no:
                                df1 = df1.drop([i], axis=0)
                            else:
                                flight_no.append(df1["flight_no"][i])

                        df3 = df2.rename(columns={'flight_no1': 'flight_no', 'origin1': 'origin', 'dest1': 'dest',
                                                  'dep_time1': 'dep_time', 'arr_time1': 'arr_time', 'days1': 'days'}, inplace=False)
                        flight_no = []

                        for i in df3.index:
                            if df3["flight_no"][i] in flight_no:
                                df3 = df3.drop([i], axis=0)
                            else:
                                flight_no.append(df3["flight_no"][i])

                        for i in df1.index:
                            if day_week in df1["days"][i] or df1["days"][i] == "DAILY":
                                pass
                            else:
                                df1 = df1.drop([i], axis=0)

                        for i in df3.index:
                            if day_week in df3["days"][i] or df3["days"][i] == "DAILY" or days[days_index+1] in df3["days"][i]:
                                pass
                            else:
                                df3 = df3.drop([i], axis=0)
                        conn = pd.concat([df1, df3], axis=0)
                        return conn
                    else:
                        query = 'select * from {},{} WHERE {}.DESTINATION = {}.ORIGIN '.format(
                            dep_1, arr_1, dep_1, arr_1)
                        mycursor.execute(query)
                        list = mycursor.fetchall()

                        df = pd.DataFrame(list, columns=[
                            "flight_no", "origin", "dest", "dep_time", "arr_time", "days", "type", "duration", "flight_no1", "origin1", "dest1", "dep_time1", "arr_time1", "days1", "type1", "duration1"])

                        df1 = pd.concat([df["flight_no"], df["origin"], df["dest"],
                                         df["dep_time"], df["arr_time"], df["days"]], axis=1)
                        df2 = pd.concat([df["flight_no1"], df["origin1"], df["dest1"],
                                         df["dep_time1"], df["arr_time1"], df["days1"]], axis=1)
                        flight_no = []
                        for i in df1.index:
                            if df1["flight_no"][i] in flight_no:
                                df1 = df1.drop([i], axis=0)
                            else:
                                flight_no.append(df1["flight_no"][i])

                        df3 = df2.rename(columns={'flight_no1': 'flight_no', 'origin1': 'origin', 'dest1': 'dest',
                                                  'dep_time1': 'dep_time', 'arr_time1': 'arr_time', 'days1': 'days'}, inplace=False)
                        flight_no = []

                        for i in df3.index:
                            if df3["flight_no"][i] in flight_no:
                                df3 = df3.drop([i], axis=0)
                            else:
                                flight_no.append(df3["flight_no"][i])

                        for i in df1.index:
                            if day_week in df1["days"][i] or df1["days"][i] == "DAILY":
                                pass
                            else:
                                df1 = df1.drop([i], axis=0)

                        for i in df3.index:
                            if day_week in df3["days"][i] or df3["days"][i] == "DAILY" or days[days_index+1] in df3["days"][i]:
                                pass
                            else:
                                df3 = df3.drop([i], axis=0)

                        conn = pd.concat([df1, df3], axis=0)
                        return conn

            dirr = dir()
            conn = con()
            if dirr.empty and df1.empty:  # or dirrr.empty:
                print("\n", "="*4, 'NO FLIGHTS AVAILABLE', "="*4, "\n")
                print("\n", "="*4, 'DO YOU WANT TO TRY A DIFFERENT DATE', "="*4, "\n")
                RESPONSE = input("ENTER (Y/N): ")
                if RESPONSE.lower() == "y":
                    continue
                else:
                    main()
                    break
            elif df1.empty or df3.empty:
                conn = pd.Dataframe()
                break

            else:
                dirr = dirr
                conn = conn
                break

    def confirmation():
        option = 1
        if dirr.empty:
            print("\n", "="*8, 'NO DIRECT FLIGHTS', "="*8, "\n")
        else:
            print("\n", "="*8, 'DIRECT FLIGHTS', "="*8, "\n")
            print(dirr)
        if conn.empty:
            print("\n", "="*8, 'NO CONNECTING FLIGHTS AVAILABLE', "="*8, "\n")
        else:
            print("\n", "="*8, 'CONNECTING FLIGHTS', "="*8, "\n")
            CONN_FLIGHTS = []
            for i in range(1, len(df1)+1):
                dep1 = df1.iloc[i-1:i, :]
                for j in range(1, len(df3)+1):
                    arr1 = df3.iloc[j-1:j, :]
                    MESSAGE = "OPTION {}".format(option)
                    print("\n", "="*4, MESSAGE, "="*4, "\n")
                    df = pd.concat([dep1, arr1], axis=0)
                    print(df)
                    CONN_FLIGHTS.append(df)
                    option = option+1

a

    dep_arrival_input()
    flights_extract()
    confirmation()
    """ print("\n", "="*4, 'DIRECT FLIGHTS', "="*4, "\n")
    print(dirr)
    print("\n", "="*4, 'CONNECTING FLIGHTS', "="*4, "\n")
    print(conn)
    for i in range(1,len(conn)+1):
        print(conn.iloc[i-1:i,:]) """


def FLIGHT_STATUS():
    print("="*8, "FLIGHT STATUS", "="*8)


def MANAGE_BOOKINGS():
    print("="*8, "MANAGE BOOKINGS", "="*8)


def STAFF_LOGIN():
    print("="*8, "STAFF LOGIN", "="*8)


def ABOUT():
    print("="*8, "ABOUT", "="*8)


NEW_BOOKING()



