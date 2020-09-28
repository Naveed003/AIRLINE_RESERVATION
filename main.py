from datetime import date
import sqlite3
import pandas as pd
import time
import random
from random import randint
import datetime
from datetime import datetime
from datetime import date
import mysql.connector
import calendar
import os
import re
from FLIGHT_SEATS import *
import phonenumbers
import pycountry
print("hello")
# my sql connction
mydb = mysql.connector.connect(host="remotemysql.com", user="QxKi8MQlUR",
                               passwd="Kf0GcKV5sh", port=3306, database="QxKi8MQlUR")
mycursor = mydb.cursor()

# main menu


def main():
    print("="*20, "GIHS AIRLINE", "="*20)
    print("\n", "="*8, "MAIN MENU", "="*8, "\n")

    print("OPTION 1: NEW BOOKING")
    print("OPTION 2: FLIGHT STATUS")
    print("OPTION 3: MANAGE BOOKINGS")
    print("OPTION 4: STAFF LOGIN")
    print("OPTION 5: ABOUT")
    print("OPTION 6: EXIT")
    # taking input from user for main menu selection
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
    # taking input for new booking
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

    def addYears(d, years):  # adding one year to current date
        global f_date
        try:
            f_date = d.replace(year=d.year+years)
            print(f_date)
        except ValueError:
            f_date = d + (date(d.year+years, 1, 1)-date(d.year, 1, 1))
            print(f_date)

    def string_to_date(datee):  # convertting sting to date
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

    def date_input():  # taking input for departure date and checking validity
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

    def flights_extract():  # extracting flights from database
        while True:
            date_input()

            def dir():  # extracting direct flights
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
                        # removing unwanted flights
                        for i in dirr.index:
                            if day_week in dirr["days"][i] or dirr["days"][i] == "DAILY":
                                pass
                            else:
                                dirr = dirr.drop([i], axis=0)

                    else:
                        dirr = pd.DataFrame()
                    return dirr

            def con():  # extracting connecting flights
                # making variable for linking to mysql
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
                    # Query for joining two tables
                    query = 'select * from {},{} WHERE {}.DESTINATION = {}.ORIGIN AND {}.DEPATURE_TIME>{}.ARRIVAL_TIME'.format(
                        dep_1, arr_1, dep_1, arr_1, arr_1, dep_1)

                    mycursor.execute(query)
                    list = mycursor.fetchall()
                    global df
                    global df1
                    global df3
                    global conn
                    if list != []:
                        # convertting the sql list to dataframe

                        df = pd.DataFrame(list, columns=[
                            "flight_no", "origin", "dest", "dep_time", "arr_time", "days", "type", "duration", "flight_no1", "origin1", "dest1", "dep_time1", "arr_time1", "days1", "type1", "duration1"])
                        # splitting df

                        df1 = pd.concat([df["flight_no"], df["origin"], df["dest"],
                                         df["dep_time"], df["arr_time"], df["days"]], axis=1)
                        df2 = pd.concat([df["flight_no1"], df["origin1"], df["dest1"],
                                         df["dep_time1"], df["arr_time1"], df["days1"]], axis=1)

                        flight_no = []
                        # removing unwanted flights
                        for i in df1.index:
                            if df1["flight_no"][i] in flight_no:
                                df1 = df1.drop([i], axis=0)
                            else:
                                flight_no.append(df1["flight_no"][i])

                        # renaming coloums and assinging it to new dataframe
                        df3 = df2.rename(columns={'flight_no1': 'flight_no', 'origin1': 'origin', 'dest1': 'dest',
                                                  'dep_time1': 'dep_time', 'arr_time1': 'arr_time', 'days1': 'days'}, inplace=False)
                        flight_no = []
                        # removing unwanted flights
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
                        # concatting all dataframes
                        conn = pd.concat([df1, df3], axis=0)
                        return conn
                    else:
                        query = 'select * from {},{} WHERE {}.DESTINATION = {}.ORIGIN '.format(
                            dep_1, arr_1, dep_1, arr_1)  # ignoring time constraint
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

            dirr = dir()  # assinging variables from func
            conn = con()
            # checking if flights found
            if dirr.empty and df1.empty:
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
                confirmation()
                break

            else:
                dirr = dirr
                conn = conn
                confirmation()
                break

    def confirmation():  # confirmation of flights and taking inputs from user
        option = 1
        FLIGHTS = []
        OPTION = []
        if dirr.empty:
            print("\n", "="*8, 'NO DIRECT FLIGHTS', "="*8, "\n")
        else:  # printing direct flights along with option number and uppending it to flight list
            print("\n", "="*8, 'DIRECT FLIGHTS', "="*8, "\n")
            for i in range(1, len(dirr)+1):
                dep1 = dirr.iloc[i-1:i, :]
                FLIGHTS.append(dep1)
                MESSAGE = "OPTION {}".format(option)
                print("\n", "="*4, MESSAGE, "="*4, "\n")
                print(dep1)
                option += 1
                OPTION.append(str(option))
        if conn.empty:
            print("\n", "="*8, 'NO CONNECTING FLIGHTS AVAILABLE', "="*8, "\n")
        else:  # printing connecting flights along with option number and uppending it to flight list
            print("\n", "="*8, 'CONNECTING FLIGHTS', "="*8, "\n")
            for i in range(1, len(df1)+1):
                dep1 = df1.iloc[i-1:i, :]
                for j in range(1, len(df3)+1):
                    arr1 = df3.iloc[j-1:j, :]
                    MESSAGE = "OPTION {}".format(option)
                    print("\n", "="*4, MESSAGE, "="*4, "\n")
                    df = pd.concat([dep1, arr1], axis=0)
                    print(df)
                    FLIGHTS.append(df)
                    OPTION.append(str(option))
                    option = option+1

        if option > 1:  # continue only if flights found
            while True:
                # asking for confirmation to continue
                exit = input('\nDO YOU WANT TO CONTINUE BOOKING(Y/N): ')
                exit = exit.strip()
                exit = exit.upper()
                if exit == "Y":
                    pass
                else:
                    main()
                    break
                # asking for which flight
                flight_booking = input('\nENTER THE OPTION NO.: ')
                if flight_booking not in OPTION:
                    print("\n", "="*4, 'ENTER A VALID OPTION', "="*4, "\n")
                else:
                    # coustomer id and booking id generation
                    query = "select CUSTOMER_ID FROM CUSTOMERS"
                    mycursor.execute(query)
                    res = mycursor.fetchall()
                    ids = []
                    for i in res:
                        for j in i:
                            ids.append(j)

                    query = "select BOOKING_ID FROM BOOKINGS"
                    mycursor.execute(query)
                    res = mycursor.fetchall()
                    booking_ids = []
                    for i in res:
                        for j in i:
                            bookin_ids.append(j)

                    while True:
                        customer_id = random.randint(0, 9999)
                        if customer_id in ids:
                            continue
                        else:
                            break

                    while True:
                        booking_id = random.randint(0, 9999)
                        if booking_id in booking_ids:
                            continue
                        else:
                            break

                    while True:  # taking input for name
                        customer_name = input("\nENTER PASSENGER NAME: ")
                        customer_name = customer_name.strip()
                        if customer_name == "":
                            print("\n", "="*4,
                                  'PLEASE ENTER YOUR NAME', "="*4, "\n")
                            continue
                        break
                    while True:  # taking input and valiation for phone number
                        customer_phone = input(
                            "\nENTER PHONE NUMBER (+(COUNTRY CODE)-*********): ")
                        try:
                            z = phonenumbers.parse(customer_phone)
                            if phonenumbers.is_valid_number(z) == False:
                                print("\n", "="*4,
                                      'PLEASE ENTER VALID NUMBER', "="*4, "\n")
                                continue
                            break

                        except Exception:
                            print("\n", "="*4,
                                  'PLEASE ENTER VALID NUMBER', "="*4, "\n")

                            continue
                    while True:  # taking input and valiation for EMAIL
                        customer_email = input("\nENTER EMAIL ID: ")
                        customer_email = customer_email.strip()
                        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                        if(re.search(regex, customer_email)):
                            break

                        else:
                            print("\n", "="*4,
                                  'PLEASE ENTER VALID EMAIL ID', "="*4, "\n")
                            continue

                    while True:  # taking input and valiation for SEX
                        customer_sex = input("\nENTER SEX (M/F): ")
                        customer_sex = customer_sex.strip()
                        customer_sex = customer_sex.upper()
                        if customer_sex.upper() not in ["M", "F"]:
                            print("\n", "="*4,
                                  'PLEASE ENTER VALID SEX', "="*4, "\n")
                            continue
                        else:
                            break
                    while True:  # taking input and valiation for DOB
                        import datetime

                        customer_dob = input(
                            "\nENTER DATE OF BIRTH (YYYY-MM-DD): ")

                        if str(date.today()) > customer_dob:
                            try:
                                date_of_birth = datetime.datetime.strptime(
                                    customer_dob, "%Y-%m-%d")
                                customer_dob = str(date_of_birth)
                                break
                            except:
                                print(
                                    "\n", "="*4, 'ENTER A VALID DATE OF BIRTH', "="*4, "\n")
                                continue

                        else:
                            print("hdskjf")
                            print("\n", "="*4,
                                  'ENTER A VALID DATE OF BIRTH', "="*4, "\n")
                            continue
                    while True:  # taking input and valiation for Nationality

                        a = input("\nENTER YOUR COUNTRY OF NATIONALITY: ")
                        b = list(pycountry.countries)
                        if pycountry.countries.get(name=a) != None:
                            break

                        else:
                            print("\n", "="*4, 'ENTER A VALID COUNTRY', "="*4, "\n")
                            continue
                    while True:
                        customer_pp_num = input(
                            'ENTER PASSENGER PASSPORT NUMBER: ')
                        if len(customer_pp_num) < 5:
                            print("\n", "="*4,
                                  'ENTER A VALID PASSPORT NUMBER', "="*4, "\n")
                            continue
                        else:
                            break

                    df = flight_seat(1)
                    print(df)
                    while True:
                        COLUMN = input("ENTER THE COLUMN: ")
                        COLUMN = COLUMN.strip()
                        COLUMN = COLUMN.upper()
                        if COLUMN in ["A", "B", "C", "D", "E", "F", "G", "H"]:
                            while True:
                                ROW = input("ENTER THE ROW NUMBER: ")
                                if ROW in [str(i) for i in range(1, 39)]:
                                    break

                                else:
                                    print("\n", "="*4,
                                          'ENTER A VALID OPTION', "="*4, "\n")
                                    continue
                            seat_id = flight_seat(2)
                            print(seat_id)
                            if df.loc[ROW, COLUMN] == '0':
                                df.loc[ROW, COLUMN] = "X"
                                df.to_csv(
                                    os.getcwd()+r'/SEATS/{}.csv'.format(seat_id))
                                print(df)
                                break
                            else:
                                print("\n", "="*4, 'SEAT UNAVAILABLE', "="*4, "\n")
                                continue

                        else:
                            print("\n", "="*4, 'ENTER A VALID OPTION', "="*4, "\n")
                            continue

                        break

                    break

    dep_arrival_input()
    flights_extract()


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
