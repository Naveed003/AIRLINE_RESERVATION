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
import sys
import json
pd.options.mode.chained_assignment = None
# CHANGE DEFAULT CUSTOMER INFO


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
        global dep_date
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
                if res == [] or res != []:
                    query = "select * from ROUTES where ORIGIN='{}' AND DESTINATION='{}'".format(
                        dep, arr)
                    mycursor.execute(query)
                    list = mycursor.fetchall()
                    global dirr
                    if list != []:
                        dirr = pd.DataFrame(list, columns=[
                            "flight_no", "origin", "dest", "dep_time", "arr_time", "days", "TYPE", "DURATION", "PRICE (USD)"])
                        dirr = pd.concat([dirr["flight_no"], dirr["origin"], dirr["dest"],
                                          dirr["dep_time"], dirr["arr_time"], dirr["days"], dirr["DURATION"], dirr["PRICE (USD)"]], axis=1)
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
                if res == [] or res != []:
                    # Query for joining two tables
                    query = 'select * from {},{} WHERE {}.DESTINATION = {}.ORIGIN AND {}.DEPATURE_TIME>{}.ARRIVAL_TIME'.format(
                        dep_1, arr_1, dep_1, arr_1, arr_1, dep_1)

                    mycursor.execute(query)
                    list = mycursor.fetchall()
                    global df
                    global df1
                    global df3
                    global conn
                    global err
                    if list != []:
                        # convertting the sql list to dataframe
                        err = 0
                        df = pd.DataFrame(list, columns=[
                            "flight_no", "origin", "dest", "dep_time", "arr_time", "days", "type", "duration", "PRICE (USD)", "flight_no1", "origin1", "dest1", "dep_time1", "arr_time1", "days1", "type1", "duration1", "PRICE (USD)1"])
                        # splitting df

                        df1 = pd.concat([df["flight_no"], df["origin"], df["dest"],
                                         df["dep_time"], df["arr_time"], df["days"], df["duration"], df["PRICE (USD)"]], axis=1)

                        df2 = pd.concat([df["flight_no1"], df["origin1"], df["dest1"],
                                         df["dep_time1"], df["arr_time1"], df["days1"], df["duration1"], df["PRICE (USD)1"]], axis=1)

                        flight_no = []
                        # removing unwanted flights
                        for i in df1.index:
                            if df1["flight_no"][i] in flight_no:
                                df1 = df1.drop([i], axis=0)
                            else:
                                flight_no.append(df1["flight_no"][i])

                        # renaming coloums and assinging it to new dataframe
                        df3 = df2.rename(columns={'flight_no1': 'flight_no', 'origin1': 'origin', 'dest1': 'dest',
                                                  'dep_time1': 'dep_time', 'arr_time1': 'arr_time', 'days1': 'days', "duration1": "duration", "PRICE (USD)1": "PRICE (USD)"}, inplace=False)

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

                        err = 1
                        print(err)
                        query = 'select * from {},{} WHERE {}.DESTINATION = {}.ORIGIN '.format(
                            dep_1, arr_1, dep_1, arr_1)  # ignoring time constraint
                        mycursor.execute(query)
                        list = mycursor.fetchall()

                        df = pd.DataFrame(list, columns=[
                            "flight_no", "origin", "dest", "dep_time", "arr_time", "days", "type", "duration", "PRICE (USD)", "flight_no1", "origin1", "dest1", "dep_time1", "arr_time1", "days1", "type1", "duration1", "PRICE (USD)1"])

                        df1 = pd.concat([df["flight_no"], df["origin"], df["dest"],
                                         df["dep_time"], df["arr_time"], df["days"], df["duration"], df["PRICE (USD)"]], axis=1)
                        df2 = pd.concat([df["flight_no1"], df["origin1"], df["dest1"],
                                         df["dep_time1"], df["arr_time1"], df["days1"], df["duration1"], df["PRICE (USD)1"]], axis=1)

                        flight_no = []
                        for i in df1.index:
                            if df1["flight_no"][i] in flight_no:
                                df1 = df1.drop([i], axis=0)
                            else:
                                flight_no.append(df1["flight_no"][i])

                        df3 = df2.rename(columns={'flight_no1': 'flight_no', 'origin1': 'origin', 'dest1': 'dest',
                                                  'dep_time1': 'dep_time', 'arr_time1': 'arr_time', 'days1': 'days', "duration1": "DURATION", "PRICE (USD)1": "PRICE (USD)"}, inplace=False)
                        df1 = df1.rename(columns={"duration": "DURATION"})
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
                conn = pd.DataFrame()
                confirmation()
                break

            else:
                dirr = dirr
                conn = conn
                confirmation()
                break

    def confirmation():  # confirmation of flights and taking inputs from user
        def customer_input():
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
                customer_name = "NAVEED"
                customer_name = customer_name.strip()
                if customer_name == "":
                    print("\n", "="*4,
                          'PLEASE ENTER YOUR NAME', "="*4, "\n")
                    continue
                break
            while True:  # taking input and valiation for phone number
                customer_phone = "+971558004998"
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
                customer_email = "imnaveed2003@gmail.com"
                customer_email = customer_email.strip()
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                if(re.search(regex, customer_email)):
                    break

                else:
                    print("\n", "="*4,
                          'PLEASE ENTER VALID EMAIL ID', "="*4, "\n")
                    continue

            while True:  # taking input and valiation for SEX
                customer_sex = "M"
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

                customer_dob = "2003-04-20"

                if str(date.today()) > customer_dob:
                    try:
                        date_of_birth = datetime.datetime.strptime(
                            customer_dob, "%Y-%m-%d")
                        customer_dob = str(date_of_birth)
                        customer_dob = customer_dob[0:10]
                        break
                    except:
                        print(
                            "\n", "="*4, 'ENTER A VALID DATE OF BIRTH', "="*4, "\n")
                        continue

                else:
                    print("\n", "="*4,
                          'ENTER A VALID DATE OF BIRTH', "="*4, "\n")
                    continue
            while True:  # taking input and valiation for Nationality

                a = "INDIA"
                b = list(pycountry.countries)
                if pycountry.countries.get(name=a) != None:
                    break

                else:
                    print("\n", "="*4, 'ENTER A VALID COUNTRY', "="*4, "\n")
                    continue
            while True:
                customer_pp_num = "12345678"
                if len(customer_pp_num) < 5:
                    print("\n", "="*4,
                          'ENTER A VALID PASSPORT NUMBER', "="*4, "\n")
                    continue
                else:
                    break

            details = [customer_id, booking_id, customer_name, customer_phone,
                       customer_email, customer_sex, customer_dob, customer_pp_num, a]
            return details

        def f_confirmation():
            while True:
                response = input("\nDO YOU WANT TO CONFIRM (Y/N): ")
                response = response.strip()
                if response.upper() == "Y":
                    break
                else:
                    main()
                    break
            try:

                if err == 1:
                    print("aa")
                    A = selection1.iloc[0]["ARRIVAL_TIME"]
                    A_ = str(selection1.iloc[1]["DEPATURE_TIME"])
                    print(A)
                    print(A_)
                    A = str(A)
                    B = A_[-8:]
                    A = A[0:10]
                    A = A[-2:]
                    A = int(A)
                    bb = A+1
                    A = str(selection1.iloc[0]["ARRIVAL_TIME"])
                    a = A[:8]+str(bb)+" "+B
                    sel = selection1.reset_index()
                    sel = sel.drop("index", axis=1)
                    sel.loc[1, "DEPATURE_TIME"] = a
                    print(sel)
                elif err == 0:
                    print("abc")
                    date = dep_date

                    arr_time1 = str(selection1.iloc[0]["ARRIVAL_TIME"])
                    dep_time1 = str(selection1.iloc[0]["DEPATURE_TIME"])
                    dep_time2 = str(selection1.iloc[1]["DEPATURE_TIME"])

                    arr_time1 = arr_time1[-8:]
                    dep_time1 = dep_time1[-8:]
                    dep_time2 = dep_time2[-8:]

                    a = date+" "+dep_time1
                    selection1.loc[0, "DEPATURE_TIME"] = a

                    if arr_time1 < dep_time1:
                        print(dep_date)
                        a = int(dep_date[-2:])
                        a += 1
                        date = date[:-2]+str(a)
                        print(date)
                        A = str(selection1.iloc[0]["ARRIVAL_TIME"])
                        a = date+" "+dep_time2
                        selection1.loc[1, "DEPATURE_TIME"] = a
                    else:
                        a = date+" "+dep_time2
                        selection1.loc[1, "DEPATURE_TIME"] = a
                    sel = selection1.reset_index()
                    sel = sel.drop("index", axis=1)
                    print(sel)

            except Exception:
                if len(selection1) == 1:
                    date = dep_date
                    dep_time1 = str(selection1.iloc[0]["DEPATURE_TIME"])
                    dep_time1 = dep_time1[-8:]
                    a = date+" "+dep_time1
                    selection1.loc[0, "DEPATURE_TIME"] = a
                    sel = selection1.reset_index()
                    sel = sel.drop("index", axis=1)
                    print(sel)
                else:
                    arr_time1 = str(selection1.iloc[0]["ARRIVAL_TIME"])
                    dep_time1 = str(selection1.iloc[0]["DEPATURE_TIME"])
                    dep_time2 = str(selection1.iloc[1]["DEPATURE_TIME"])

                    arr_time1 = arr_time1[-8:]
                    dep_time1 = dep_time1[-8:]
                    dep_time2 = dep_time2[-8:]

                    a = date+" "+dep_time1
                    selection1.loc[0, "DEPATURE_TIME"] = a

                    if arr_time1 < dep_time1:
                        print(dep_date)
                        a = int(dep_date[-2:])
                        a += 1
                        date = date[:-2]+str(a)
                        print(date)
                        A = str(selection1.iloc[0]["ARRIVAL_TIME"])
                        a = date+" "+dep_time2
                        selection1.loc[1, "DEPATURE_TIME"] = a
                    else:
                        a = date+" "+dep_time1
                        selection1.loc[1, "DEPATURE_TIME"] = a
                    sel = selection1.reset_index()
                    sel = sel.drop("index", axis=1)
                    print(sel)

        option = 1
        FLIGHTS = []
        OPTION = []
        if dirr.empty:
            print("\n", "="*8, 'NO DIRECT FLIGHTS', "="*8, "\n")
        else:  # printing direct flights along with option number and uppending it to flight list
            del dirr["days"]
            print("\n", "="*8, 'DIRECT FLIGHTS', "="*8, "\n")
            for i in range(1, len(dirr)+1):
                dep1 = dirr.iloc[i-1:i, :]
                FLIGHTS.append(dep1)
                MESSAGE = "OPTION {}".format(option)
                print("\n", "="*4, MESSAGE, "="*4, "\n")
                dep1 = dep1.reset_index()
                dep1 = dep1.drop("index", axis=1)
                print(dep1)
                OPTION.append(str(option))
                option += 1
        if conn.empty:
            print("\n", "="*8, 'NO CONNECTING FLIGHTS AVAILABLE', "="*8, "\n")
        else:  # printing connecting flights along with option number and uppending it to flight list
            del df1["days"]
            del df3["days"]
            print("\n", "="*8, 'CONNECTING FLIGHTS', "="*8, "\n")
            for i in range(1, len(df1)+1):
                dep1 = df1.iloc[i-1:i, :]
                for j in range(1, len(df3)+1):
                    arr1 = df3.iloc[j-1:j, :]
                    MESSAGE = "OPTION {}".format(option)
                    print("\n", "="*4, MESSAGE, "="*4, "\n")
                    df = pd.concat([dep1, arr1], axis=0)
                    df = df.reset_index()
                    df = df.drop("index", axis=1)
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
                    break
                else:
                    main()
                    break
                # asking for which flight
            while True:
                flight_booking = input('\nENTER THE OPTION NO.: ')
                res = []
                try:
                    selection = FLIGHTS[int(flight_booking)-1]
                    if len(selection) == 1:
                        flight_no = selection.iloc[0]["flight_no"]
                        origin = selection.iloc[0]["origin"]
                        destination = selection.iloc[0]["dest"]
                        dep_time = str(depature_date)+" " + \
                            str(selection.iloc[0]["dep_time"])[-8:]
                        query = "select * from SCHEDULE WHERE FLIGHT_NO='{}' AND ORIGIN='{}' AND DESTINATION='{}' AND DEPATURE_TIME='{}'".format(
                            flight_no, origin, destination, dep_time)
                        mycursor.execute(query)
                        res = mycursor.fetchall()
                        listt = []
                        if res != []:
                            for i in res:
                                for j in i:
                                    listt.append(j)

                    else:

                        for i in range(2):
                            flight_no = selection.iloc[i]["flight_no"]
                            origin = selection.iloc[i]["origin"]
                            destination = selection.iloc[i]["dest"]
                            dep_time = str(depature_date)+" " + \
                                str(selection.iloc[i]["dep_time"])[-8:]
                            query = "select * from SCHEDULE WHERE FLIGHT_NO='{}' AND ORIGIN='{}' AND DESTINATION='{}' AND DEPATURE_TIME='{}'".format(
                                flight_no, origin, destination, dep_time)
                            mycursor.execute(query)

                            for i in mycursor.fetchall():
                                res.append(i)
                except Exception:
                    pass
                list_seat = []
                list_seat_id = []
                query = "select * from SCHEDULE WHERE FLIGHT_NO='{}' and ORIGIN"
                if flight_booking not in OPTION:
                    print("\n", "="*4, 'ENTER A VALID OPTION', "="*4, "\n")
                    continue

                selection = FLIGHTS[int(flight_booking)-1]
                selection = selection.reset_index()
                selection = selection.drop("index", axis=1)
                selection = selection.rename(columns={"flight_no": "FLIGHT NO", "origin": "ORIGIN",
                                                      "dest": "DESTINATION", "dep_time": "DEPATURE_TIME", "arr_time": "ARRIVAL_TIME", "duration": "DURATION"})

                if res != []:
                    if len(res) == 1:
                        df = pd.DataFrame(res, columns=[
                            "FLIGHT NO", "ORIGIN", "DESTINATION", "DEPATURE_TIME", "ARRIVAL_TIME", "DURATION", "SEAT_ID"])
                        zzz = df
                        Flight_no = zzz.iloc[0]["FLIGHT NO"]
                        p_x = selection[selection["FLIGHT NO"]
                                        == Flight_no].index.values
                        zzz["PRICE (USD)"] = selection.iloc[p_x[0]
                                                            ]["PRICE (USD)"]
                        seatid = df.iloc[0]["SEAT_ID"]
                        seatid = 1234
                        with open(os.getcwd()+'/SEATS/{}.txt'.format(seatid), 'r') as f:
                            seat_list = json.loads(f.read())
                        indexx = [0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19, 20, 21,
                                  22, 23, 24, 25, 26, 0, 27, 28, 29, 30,  31, 32, 33, 34, 35, 36, 37, 38]

                        df = pd.DataFrame(
                            seat_list[1:], columns=seat_list[0], index=indexx)
                        zz = df
                        a = df.isin(["0"]).any()
                        b = []
                        for i in a:
                            b.append(i)

                        if True not in b:
                            print("\n", "="*4,
                                  'NO SEATS AVAILABLE IN THE SELECTED FLIGHT', "="*4, "\n")
                            a = input("DO YOU WANT TO CONTIUNE BOOKING(Y/N): ")
                            a.strip()
                            a.upper()
                            if a == "Y":
                                confirmation()
                                sys.exit()
                            else:
                                time.sleep(5)
                                sys.exit()
                        else:
                            details = customer_input()
                            print(
                                "\n", "="*4, 'SEAT SELECTION FOR {} TO {}'.format(res[0][1], res[0][2]), "="*4, "\n")
                            print("\t0=AVAILABLE AND X=BOOKED\n")
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
                                    if df.loc[int(ROW), COLUMN] == '0':
                                        df.loc[int(ROW), COLUMN] = "X"
                                        seats = [
                                            df.columns.values.tolist()] + df.values.tolist()
                                        with open('SEATS/{}.txt'.format(seatid), 'w') as f:
                                            f.write(json.dumps(seats))
                                        seat = COLUMN+ROW
                                        list_seat_id.append(str(seatid))
                                        list_seat.append(COLUMN+ROW)
                                        break
                                    else:
                                        print("\n", "="*4,
                                              'SEAT UNAVAILABLE', "="*4, "\n")
                                        continue

                                else:
                                    print("\n", "="*4,
                                          'ENTER A VALID OPTION', "="*4, "\n")
                                    continue
                            columns = []
                            for i in zzz.columns:
                                columns.append(i)
                            selection1 = pd.DataFrame(columns=columns)

                            Flight_no = zzz.iloc[0]["FLIGHT NO"]
                            x = selection[selection["FLIGHT NO"]
                                          == Flight_no].index.values
                            selection1 = pd.concat([selection1, zzz], axis=0)
                            selection1 = selection1.drop("SEAT_ID", axis=1)
                            selection = selection.drop(x, axis=0)

                    else:
                        seatid = [res[0][-1], res[1][-1]]
                        with open(os.getcwd()+'/SEATS/{}.txt'.format(seatid[0]), 'r') as f:
                            seat1 = json.loads(f.read())
                        with open(os.getcwd()+'/SEATS/{}.txt'.format(seatid[1]), 'r') as f:
                            seat2 = json.loads(f.read())
                        indexx = [0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19, 20, 21,
                                  22, 23, 24, 25, 26, 0, 27, 28, 29, 30,  31, 32, 33, 34, 35, 36, 37, 38]
                        seat1 = pd.DataFrame(
                            seat1[1:], columns=seat1[0], index=indexx)
                        seat2 = pd.DataFrame(
                            seat2[1:], columns=seat2[0], index=indexx)
                        a = seat1.isin(["0"]).any()
                        b = []
                        for i in a:
                            b.append(i)
                        a = seat2.isin(["0"]).any()
                        b1 = []
                        for i in a:
                            b1.append(i)

                        if True not in b or True not in b1:
                            print("\n", "="*4,
                                  'NO SEATS AVAILABLE IN THE SELECTED FLIGHT', "="*4, "\n")
                            a = input("DO YOU WANT TO CONTIUNE BOOKING(Y/N): ")
                            a.strip()
                            a.upper()
                            if a == "Y":
                                confirmation()
                                time.sleep(2)
                                sys.exit()
                            else:
                                time.sleep(5)
                                sys.exit()
                        else:
                            details = customer_input()
                            print("\n", "="*4, 'SEAT SELECTION FOR {} TO {}'.format(dep,
                                                                                    res[0][2]), "="*4, "\n")
                            print("\t0=AVAILABLE AND X=BOOKED\n")
                            print(seat1)
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
                                    if seat1.loc[int(ROW), COLUMN] == '0':
                                        seat1.loc[int(ROW), COLUMN] = "X"
                                        seats = [
                                            seat1.columns.values.tolist()] + seat1.values.tolist()
                                        with open('SEATS/{}.txt'.format(seatid[0]), 'w') as f:
                                            f.write(json.dumps(seats))
                                        seat = COLUMN+ROW
                                        list_seat_id.append(str(seatid[0]))
                                        list_seat.append(seat)
                                        break
                                    else:
                                        print("\n", "="*4,
                                              'SEAT UNAVAILABLE', "="*4, "\n")
                                        continue
                                    break

                                else:
                                    print("\n", "="*4,
                                          'ENTER A VALID OPTION', "="*4, "\n")
                                    continue
                            print(
                                "\n", "="*4, 'SEAT SELECTION FOR {} TO {}'.format(res[1][1], res[1][2]), "="*4, "\n")
                            print("\t0=AVAILABLE AND X=BOOKED\n")
                            print(seat2)
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
                                    if seat2.loc[int(ROW), COLUMN] == '0':
                                        seat2.loc[int(ROW), COLUMN] = "X"
                                        seats = [
                                            seat2.columns.values.tolist()] + seat2.values.tolist()
                                        with open('SEATS/{}.txt'.format(seatid[1]), 'w') as f:
                                            f.write(json.dumps(seats))
                                        seat = COLUMN+ROW
                                        list_seat_id.append(str(seatid[1]))
                                        list_seat.append(COLUMN+ROW)
                                        break
                                    else:
                                        print("\n", "="*4,
                                              'SEAT UNAVAILABLE', "="*4, "\n")
                                        continue
                                    break

                                else:
                                    print("\n", "="*4,
                                          'ENTER A VALID OPTION', "="*4, "\n")
                                    continue
                            selection1 = selection
                            selection = pd.DataFrame()

                selection = selection.reset_index()
                selection = selection.drop("index", axis=1)
                if selection.empty == False:
                    details = customer_input()
                    if len(selection) == 1:
                        x = 2
                    else:
                        x = 3
                        col = []
                        for i in selection.columns:
                            col.append(i)
                        selection1 = pd.DataFrame(columns=col)

                    for i in range(1, x):

                        if i == 1:
                            print(
                                "\n", "="*4, 'SEAT SELECTION FOR {} TO {}'.format(selection.iloc[0][1], selection.iloc[0][2]), "="*4, "\n")
                            selection1 = pd.concat(
                                [selection1, selection.iloc[0:1, :]], axis=0)
                            print(selection1)
                        else:
                            print(
                                "\n", "="*4, 'SEAT SELECTION FOR {} TO {}'.format(selection.iloc[1][1], selection.iloc[1][2]), "="*4, "\n")
                            selection1 = pd.concat(
                                [selection1, selection.iloc[1:, :]], axis=0)
                            print(selection1)
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
                                print(df.loc[ROW, COLUMN])
                                if df.loc[ROW, COLUMN] == '0':
                                    df.loc[ROW, COLUMN] = "X"
                                    seats = [df.columns.values.tolist()] + df.values.tolist()
                                    with open('seats/{}.txt'.format(seat_id), 'w') as f:
                                        f.write(json.dumps(seats))
                                    print(df)
                                    list_seat_id.append(str(seat_id))
                                    list_seat.append(COLUMN+ROW)
                                    break
                                else:
                                    print("\n", "="*4,
                                          'SEAT UNAVAILABLE', "="*4, "\n")
                                    continue

                            else:
                                print("\n", "="*4,
                                      'ENTER A VALID OPTION', "="*4, "\n")
                                continue

                            break

                break
            f_confirmation()

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
