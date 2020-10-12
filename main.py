# main menu
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
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None
# my sql connction
mydb = mysql.connector.connect(host="remotemysql.com", user="QxKi8MQlUR",
                               passwd="Kf0GcKV5sh", port=3306, database="QxKi8MQlUR")
mycursor = mydb.cursor()
date1 = datetime.now()
datee1 = str(date1)
datee1 = datee1[:19]
c_date = date.today()
datee1 = '2020-10-03 18:59:09'
query = "insert into E_SCHEDULE SELECT * FROM SCHEDULE WHERE DEPATURE_TIME<'{}'".format(
    datee1)
mycursor.execute(query)
query = "delete from SCHEDULE where DEPATURE_TIME<'{}'".format(datee1)
mycursor.execute(query)
query-"delete from DELAY where DEPATURE_TIME<'{}'".format(datee1)
mycursor.execute(query)
query = "insert into E_BOOKINGS SELECT * FROM BOOKINGS WHERE DEPATURE_TIME<'{}'".format(
    datee1)
mycursor.execute(query)
query = "delete from BOOKINGS where DEPATURE_TIME<'{}'".format(datee1)
mycursor.execute(query)
query = "delete from PASSPORT WHERE P_EXPIRY<'{}'".format(c_date)
mycursor.execute(query)
mydb.commit()


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
            print("="*8, "FLIGHT STATUS", "="*8)
            FLIGHT_STATUS(0)
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


def mail(email, message):
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    msg['Subject'] = "AIRLINE BOOKING CONFIRMATION"
    msg['From'] = "gihs.airline@gmail.com"
    msg['To'] = email
    msg.set_content(message)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login("gihs.airline@gmail.com", "gelronfuifxcyheb")

        smtp.send_message(msg)


def NEW_BOOKING():
    # taking input for new booking
    def dep_arrival_input():
        print("\n", "="*8, "NEW BOOKING", "="*8)
        print("\n", "="*4, "DEPARTURE", "="*4)
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
        except ValueError:
            f_date = d + (date(d.year+years, 1, 1)-date(d.year, 1, 1))

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

    def date_input():  # taking input for departure date and checking validity
        current_date = date.today()
        addYears(current_date, 1)
        global depature_date
        global dep_date
        while True:
            depature_date = input("\nENTER DEPARTURE DATE (YYYY-MM-DD): ")
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
            elif str(current_date) < depature_date and str(f_date) > depature_date:
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
                    dirr= dirr.reset_index()
                    dirr = dirr.drop("index", axis=1)
                    for i in range(len(dirr)):

                        price = dirr.loc[i, 'PRICE (USD)']
                        current_date = date.today()
                        current_day = current_date.weekday()
                        departure_month = depature_date.month
                        delta = depature_date - current_date
                        timeofdep = str(dirr.loc[i, 'dep_time'])
                        timeofdep = timeofdep[7:-6]
                        if delta.days <= 90:
                            price = price + price*(15/100)

                        elif delta.days <= 30:
                            price = price + price*(20/100)

                        elif delta.days <= 15:
                            price = price + price*(30/100)

                        elif delta.days <= 2:
                            price = price + price*(50/100)

                        if current_day >= 5:
                            price = price + price*(5/100)

                        if departure_month in [6, 8]:
                            price = price + price*(25/100)

                        elif departure_month in [7, 12]:
                            price = price + price*(30/100)

                        elif departure_month in [1, 2]:
                            price = price + price*(15/100)

                        if int(timeofdep) >= 20:
                            price = price - price*(15/100)

                        elif int(timeofdep) <= 6:
                            price = price - price*(15/100)

                        dirr.loc[i, 'PRICE (USD)'] = int(price)

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

                        df1 = df1.reset_index()
                        df1 = df1.drop("index", axis=1)
                        for i in range(len(df1)):

                            price = df1.loc[i, 'PRICE (USD)']
                            current_date = date.today()
                            current_day = current_date.weekday()
                            departure_month = depature_date.month
                            delta = depature_date - current_date
                            timeofdep = str(df1.loc[i, 'dep_time'])
                            timeofdep = timeofdep[7:-6]
                            if delta.days <= 90:
                                price = price + price*(15/100)

                            elif delta.days <= 30:
                                price = price + price*(20/100)

                            elif delta.days <= 15:
                                price = price + price*(30/100)

                            elif delta.days <= 2:
                                price = price + price*(50/100)

                            if current_day >= 5:
                                price = price + price*(5/100)

                            if departure_month in [6, 8]:
                                price = price + price*(25/100)

                            elif departure_month in [7, 12]:
                                price = price + price*(30/100)

                            elif departure_month in [1, 2]:
                                price = price + price*(15/100)

                            if int(timeofdep) >= 20:
                                price = price - price*(15/100)

                            if int(timeofdep) <= 6:
                                price = price - price*(15/100)

                            df1.loc[i, 'PRICE (USD)'] = int(price)
                        df3 = df3.reset_index()
                        df3 = df3.drop("index", axis=1)
                        for i in range(len(df1)):

                            price = df3.loc[i, 'PRICE (USD)']
                            current_date = date.today()
                            current_day = current_date.weekday()
                            departure_month = depature_date.month
                            delta = depature_date - current_date
                            timeofdep = str(df3.loc[i, 'dep_time'])
                            timeofdep = timeofdep[7:-6]
                            if delta.days <= 90:
                                price = price + price*(15/100)

                            elif delta.days <= 30:
                                price = price + price*(20/100)

                            elif delta.days <= 15:
                                price = price + price*(30/100)

                            elif delta.days <= 2:
                                price = price + price*(50/100)

                            if current_day >= 5:
                                price = price + price*(5/100)

                            if departure_month in [6, 8]:
                                price = price + price*(25/100)

                            elif departure_month in [7, 12]:
                                price = price + price*(30/100)

                            elif departure_month in [1, 2]:
                                price = price + price*(15/100)

                            if int(timeofdep) >= 20:
                                price = price - price*(15/100)

                            if int(timeofdep) <= 6:
                                price = price - price*(15/100)

                            df3.loc[i, 'PRICE (USD)'] = int(price)
                        conn=pd.concat([df1,df3],axis=1)
                        return conn
                    else:

                        err = 1
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
                        df1 = df1.reset_index()
                        df1 = df1.drop("index", axis=1)
                        for i in range(len(df1)):

                            price = df1.loc[i, 'PRICE (USD)']
                            current_date = date.today()
                            current_day = current_date.weekday()
                            departure_month = depature_date.month
                            delta = depature_date - current_date
                            timeofdep = str(df1.loc[i, 'dep_time'])
                            timeofdep = timeofdep[7:-6]
                            if delta.days <= 90:
                                price = price + price*(15/100)

                            elif delta.days <= 30:
                                price = price + price*(20/100)

                            elif delta.days <= 15:
                                price = price + price*(30/100)

                            elif delta.days <= 2:
                                price = price + price*(50/100)

                            if current_day >= 5:
                                price = price + price*(5/100)

                            if departure_month in [6, 8]:
                                price = price + price*(25/100)

                            elif departure_month in [7, 12]:
                                price = price + price*(30/100)

                            elif departure_month in [1, 2]:
                                price = price + price*(15/100)

                            if int(timeofdep) >= 20:
                                price = price - price*(15/100)

                            if int(timeofdep) <= 6:
                                price = price - price*(15/100)

                            df1.loc[i, 'PRICE (USD)'] = int(price)
                        df3 = df3.reset_index()
                        df3 = df3.drop("index", axis=1)
                        for i in range(len(df1)):

                            price = df3.loc[i, 'PRICE (USD)']
                            current_date = date.today()
                            current_day = current_date.weekday()
                            departure_month = depature_date.month
                            delta = depature_date - current_date
                            timeofdep = str(df3.loc[i, 'dep_time'])
                            timeofdep = timeofdep[7:-6]
                            if delta.days <= 90:
                                price = price + price*(15/100)

                            elif delta.days <= 30:
                                price = price + price*(20/100)

                            elif delta.days <= 15:
                                price = price + price*(30/100)

                            elif delta.days <= 2:
                                price = price + price*(50/100)

                            if current_day >= 5:
                                price = price + price*(5/100)

                            if departure_month in [6, 8]:
                                price = price + price*(25/100)

                            elif departure_month in [7, 12]:
                                price = price + price*(30/100)

                            elif departure_month in [1, 2]:
                                price = price + price*(15/100)

                            if int(timeofdep) >= 20:
                                price = price - price*(15/100)

                            if int(timeofdep) <= 6:
                                price = price - price*(15/100)

                            df3.loc[i, 'PRICE (USD)'] = int(price)
                        conn=pd.concat([df1,df3],axis=1)
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
                    booking_ids.append(j)

            while True:
                customer_id = random.randint(0, 9999)
                if customer_id in ids:
                    continue
                else:
                    break

            while True:
                booking_id = random.randint(100, 99999)
                if booking_id in booking_ids:
                    continue
                else:
                    break

            while True:  # taking input for name
                customer_name = input("\nENTER PASSENGER NAME: ")
                customer_name = customer_name.strip()
                customer_name = customer_name.upper()
                if customer_name == "":
                    print("\n", "="*4,
                          'PLEASE ENTER YOUR NAME', "="*4, "\n")
                    continue
                break
            while True:  # taking input and valiation for phone number
                customer_phone = input("ENTER PASSENGER PHONE NUMBER ((COUNTRY CODE)-########): ")
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
                customer_email = input("\nENTER PASSENGER EMAIL ADDRESS: ")
                customer_email = customer_email.strip()
                customer_email = customer_email.lower()
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                if(re.search(regex, customer_email)):
                    break

                else:
                    print("\n", "="*4,
                          'PLEASE ENTER VALID EMAIL ID', "="*4, "\n")
                    continue

            while True:  # taking input and valiation for SEX
                customer_sex = input("\nENTER PASSENGER SEX (M/F): ")
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

                customer_dob = input("\nENTER PASSENGER DATE OF BIRTH (YYYY-MM-DD): ")
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
                if str(date.today()) > customer_dob:
                    break

                else:
                    print("\n", "="*4,
                          'ENTER A VALID DATE OF BIRTH', "="*4, "\n")
                    continue
            while True:  # taking input and valiation for Nationality

                a = "INDIA"
                b = list(pycountry.countries)
                a = a.strip()
                a = a.upper()
                if pycountry.countries.get(name=a) != None:
                    break

                else:
                    print("\n", "="*4, 'ENTER A VALID COUNTRY', "="*4, "\n")
                    continue

            while True:
                customer_pp_num = input("\nENTER PASSPORT NUMBER OF PASSENGER: ")
                query = "select P_NUMBER,P_NAME,P_EXPIRY FROM PASSPORT WHERE P_NUMBER='{}'".format(
                    customer_pp_num)
                mycursor.execute(query)
                res = mycursor.fetchall()
                if len(customer_pp_num) < 5:
                    print("\n", "="*4,
                          'ENTER A VALID PASSPORT NUMBER', "="*4, "\n")
                    continue
                else:
                    if res != []:
                        while True:
                            customer_pp_name = input(
                                "\nENTER NAME ACCORDING TO PASSPORT: ")
                            customer_pp_name = customer_pp_name.strip()
                            customer_pp_name = customer_pp_name.upper()
                            if res[0][1] == customer_pp_name:
                                while True:
                                    customer_pp_expiry = input(
                                        "\nENTER EXPIRY OF PASSPORT (YYYY-MM-DD): ")
                                    try:
                                        customer_pp_expiry = datetime.datetime.strptime(
                                            customer_pp_expiry, "%Y-%m-%d")
                                        customer_pp_expiry = str(
                                            customer_pp_expiry)
                                        customer_pp_expiry = customer_pp_expiry[0:10]
                                    except:
                                        print(
                                            "\n", "="*4, 'PASSPORT EXPIRY DOES NOT MATCH OUR DB', "="*4, "\n")
                                        continue
                                    date1 = dep_date[:8] + \
                                        str(int(dep_date[-2])+1)
                                    if str(res[0][2]) == customer_pp_expiry:
                                        break
                                    else:
                                        print(
                                            "\n", "="*4, 'PASSPORT EXPIRY DOES NOT MATCH OUR DB', "="*4, "\n")
                                        continue
                                break
                            else:
                                print(
                                    "\n", "="*4, 'NAME YOU ENTERED DOES NOT MATCH OUR DB', "="*4, "\n")
                                continue

                    else:

                        while True:
                            customer_pp_name = input(
                                "\nENTER NAME ACCORDING TO PASSPORT: ")
                            customer_pp_name = customer_pp_name.strip()
                            customer_pp_name = customer_pp_name.upper()
                            if customer_pp_name != "":
                                while True:
                                    customer_pp_expiry = input(
                                        "\nENTER EXPIRY OF PASSPORT (YYYY-MM-DD): ")
                                    try:
                                        customer_pp_expiry = datetime.datetime.strptime(
                                            customer_pp_expiry, "%Y-%m-%d")
                                        customer_pp_expiry = str(
                                            customer_pp_expiry)
                                        customer_pp_expiry = customer_pp_expiry[0:10]
                                        break
                                    except:
                                        print(
                                            "\n", "="*4, 'ENTER A VALID PASSPORT EXPIRY', "="*4, "\n")
                                        continue
                                    if str(customer_pp_expiry) >= dep_date:
                                        break
                                    else:
                                        print(
                                            "\n", "="*4, 'SORRY YOUR PASSPORT IS EXPIRED', "="*4, "\n")
                                        time.sleep(4)
                                        sys.exit()
                                break

                            else:
                                print(
                                    "\n", "="*4, 'ENTER NAME ACCORDING TO PASSPORT', "="*4, "\n")
                                continue

                    break
            PP_DETAILS = [customer_pp_num.upper(),
                          customer_pp_name.upper(), customer_pp_expiry.upper()]
            details = [customer_id, booking_id, customer_name, customer_phone,
                       customer_email, customer_sex, customer_dob, customer_pp_num, a, PP_DETAILS]
            return details

        def f_confirmation():
            if len(selection1) != 1:
                try:
                    if err == 1:
                        timee = str(selection1.iloc[0]["ARRIVAL_TIME"])[-8:]
                        datee = dep_date[0:8]+str((int(dep_date[-2:])+1))
                        dep_time = datee+" "+timee
                        sel = selection1.reset_index()
                        sel = sel.drop("index", axis=1)
                        sel.loc[1, "DEPARTURE_TIME"] = dep_time
                        timee = str(selection1.iloc[0]["DEPARTURE_TIME"])[-8:]
                        datee = dep_date
                        dep_time = dep_date+" "+timee
                        sel.loc[0, "DEPARTURE_TIME"] = dep_time

                    elif err == 0:
                        date = dep_date

                        arr_time1 = str(selection1.iloc[0]["ARRIVAL_TIME"])
                        dep_time1 = str(selection1.iloc[0]["DEPARTURE_TIME"])
                        dep_time2 = str(selection1.iloc[1]["DEPARTURE_TIME"])

                        arr_time1 = arr_time1[-8:]
                        dep_time1 = dep_time1[-8:]
                        dep_time2 = dep_time2[-8:]

                        a = date+" "+dep_time1
                        selection1.loc[0, "DEPARTURE_TIME"] = a

                        if arr_time1 < dep_time1:
                            a = int(dep_date[-2:])
                            a += 1
                            date = date[:-2]+str(a)
                            A = str(selection1.iloc[0]["ARRIVAL_TIME"])
                            a = date+" "+dep_time2
                        else:
                            a = date+" "+dep_time2
                        sel = selection1.reset_index()
                        sel = sel.drop("index", axis=1)
                        sel.loc[1, "DEPARTURE_TIME"] = a

                except Exception:
                    if len(selection1) == 1:
                        date = dep_date
                        dep_time1 = str(selection1.iloc[0]["DEPARTURE_TIME"])
                        dep_time1 = dep_time1[-8:]
                        a = date+" "+dep_time1
                        sel = selection1.reset_index()
                        sel = sel.drop("index", axis=1)
                        sel.loc[0, "DEPARTURE_TIME"] = a
                    else:
                        date = dep_date
                        arr_time1 = str(selection1.iloc[0]["ARRIVAL_TIME"])
                        dep_time1 = str(selection1.iloc[0]["DEPARTURE_TIME"])
                        dep_time2 = str(selection1.iloc[1]["DEPARTURE_TIME"])

                        arr_time1 = arr_time1[-8:]
                        dep_time1 = dep_time1[-8:]
                        dep_time2 = dep_time2[-8:]

                        a = date+" "+dep_time1

                        sel = selection1.reset_index()
                        sel = sel.drop("index", axis=1)
                        sel.loc[0, "DEPARTURE_TIME"] = a

                        if arr_time1 < dep_time1:
                            a = int(dep_date[-2:])
                            a += 1
                            date = date[:-2]+str(a)
                            A = str(selection1.iloc[0]["ARRIVAL_TIME"])
                            a = date+" "+dep_time2
                        else:
                            a = date+" "+dep_time1
                        sel = selection1.reset_index()
                        sel = sel.drop("index", axis=1)
                        sel.loc[0, "DEPARTURE_TIME"] = a
            else:
                timee = str(selection1.iloc[0]["ARRIVAL_TIME"])[-8:]
                datee = dep_date
                dep_time = datee+" "+timee
                sel = selection1.reset_index()
                sel = sel.drop("index", axis=1)
                sel.loc[0, "DEPARTURE_TIME"] = dep_time
                timee = str(selection1.iloc[0]["DEPARTURE_TIME"])[-8:]
                datee = dep_date
                dep_time = dep_date+" "+timee
                sel.loc[0, "DEPARTURE_TIME"] = dep_time
            print("\n", "="*8, 'SELECTION', "="*8, "\n")
            sel.insert(6, "SEAT", list_seat)
            price = []
            total = 0
            for i in range(len(sel)):
                a = str(sel.loc[i, 'ARRIVAL_TIME'])[-8:]
                sel.loc[i, 'ARRIVAL_TIME'] = a
                a = str(sel.loc[i, 'DURATION'])[-8:]
                sel.loc[i, 'DURATION'] = a
                d = str(sel.loc[i, "PRICE (USD)"])
                total += int(d)
                price.append(d)
            sel = sel.drop("PRICE (USD)", axis=1)
            print(sel)
            DET = sel
            sel = sel.drop("SEAT", axis=1)

            sel.insert(6, "PRICE (USD)", price)
            print("\nTOTAL FARE: ${:,.2f}".format(total))
            while True:
                response = input("\nDO YOU WANT TO CONFIRM (Y/N): ")
                response = response.strip()
                if response.upper() == "Y":
                    break
                else:
                    main()
                    break
            try:

                for i in range(len(sel)):
                    a = str(sel.loc[i, 'ARRIVAL_TIME'])[-8:]
                    sel.loc[i, 'ARRIVAL_TIME'] = a
                    a = str(sel.loc[i, 'DURATION'])[-8:]
                    sel.loc[i, 'DURATION'] = a
                    query = 'select FLIGHT_NO FROM SCHEDULE WHERE FLIGHT_NO = "{}" AND ORIGIN ="{}" AND DESTINATION ="{}" AND DEPATURE_TIME = "{}"'.format(
                        sel.loc[i, 'FLIGHT NO'], sel.loc[i, 'ORIGIN'], sel.loc[i, 'DESTINATION'], sel.loc[i, 'DEPARTURE_TIME'])
                    mycursor.execute(query)
                    res = mycursor.fetchall()
                    if res == []:
                        query = 'INSERT INTO SCHEDULE VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(
                            sel.loc[i, 'FLIGHT NO'], sel.loc[i, 'ORIGIN'], sel.loc[i, 'DESTINATION'], sel.loc[i, 'DEPARTURE_TIME'], sel.loc[i, 'ARRIVAL_TIME'], sel.loc[i, 'DURATION'], list_seat_id[i])
                        mycursor.execute(query)
                        query = 'INSERT INTO DELAY VALUES ("{}","{}","{}","{}","{}","{}","{}",{})'.format(
                            sel.loc[i, 'FLIGHT NO'], sel.loc[i, 'ORIGIN'], sel.loc[i, 'DESTINATION'], sel.loc[i, 'DEPARTURE_TIME'], sel.loc[i, 'ARRIVAL_TIME'], sel.loc[i, 'DURATION'], list_seat_id[i], 0)
                        mycursor.execute(query)
                query = "select CUSTOMER_ID,CUSTOMER_NAME,CUSTOMER_PHONE,CUSTOMER_EMAIL,CUSTOMER_SEX,CUSTOMER_DOB,CUSTOMER_NATIONALITY,CUSTOMER_PASSPORT_NUMBER FROM CUSTOMERS where CUSTOMER_PASSPORT_NUMBER='{}' AND CUSTOMER_NAME='{}' AND CUSTOMER_PHONE='{}' AND CUSTOMER_EMAIL='{}' AND CUSTOMER_SEX='{}' AND CUSTOMER_DOB='{}' AND CUSTOMER_NATIONALITY='{}'".format(
                    details[-3], details[2], details[3], details[4], details[5], details[6], details[8])
                mycursor.execute(query)
                res = mycursor.fetchall()
                from datetime import date
                if res != []:
                    res1 = []
                    for i in res:
                        for j in i:
                            res1.append(str(j))
                    if res1[1:] == [details[2], details[3], details[4], details[5], details[6], details[8], details[-3]]:
                        details[0] = res[0][0]
                    else:
                        query = "INSERT INTO CUSTOMERS VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}')".format(
                            details[0], details[2], details[3], details[4], details[5], details[6], details[-2], details[-3], str(date.today()))
                        mycursor.execute(query)

                else:
                    query = "INSERT INTO CUSTOMERS VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        details[0], details[2], details[3], details[4], details[5], details[6], details[-2], details[-3], str(date.today()))
                    mycursor.execute(query)
                for i in range(len(sel)):
                    query = 'INSERT INTO BOOKINGS VALUES("{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                        details[0], details[1], sel.loc[i, 'FLIGHT NO'], sel.loc[i, 'DEPARTURE_TIME'], list_seat[i], list_seat_id[i], sel.loc[i, 'PRICE (USD)'], str(date.today()))
                    mycursor.execute(query)
                query = "select P_NUMBER,P_NAME,P_EXPIRY FROM PASSPORT"
                pp_details = details[-1]
                mycursor.execute(query)
                res = mycursor.fetchall()
                temp = []
                res1 = []
                if res != []:
                    for i in res:
                        for j in i:
                            temp.append(str(j))
                        res1.append(temp)
                        temp = []
                    if pp_details in res1:
                        pass
                    else:
                        query = "insert into PASSPORT VALUES({},'{}','{}','{}')".format(
                            int(details[0]), pp_details[0], pp_details[1], pp_details[2])
                        mycursor.execute(query)
                else:
                    query = "insert into PASSPORT VALUES({},'{}','{}','{}')".format(
                        int(details[0]), pp_details[0], pp_details[1], pp_details[2])

                    mycursor.execute(query)

                for i in range(len(list_seat_id)):
                    with open(os.getcwd()+'/SEATS/{}.txt'.format(list_seat_id[i]), 'r') as f:
                        seat_list = json.loads(f.read())
                    with open('SEATS/{}.txt'.format(list_seat_id[i]), 'w') as f:
                        f.write(json.dumps(SEATS_1[i]))
                CUSTOMER_NAME = details[2].upper()
                from datetime import date
                date = date.today()
                pp_details = pp_details[0:2]
                pp_details.append(details[6])
                pp_details.append(details[5])
                pp_details.append(details[3])
                pp_details.append(details[1])
                DET = DET
                booking_id = details[1]
                total = total
                import smtplib
                from email.message import EmailMessage
                msg = EmailMessage()
                msg['Subject'] = "AIRLINE BOOKING CONFIRMATION"
                msg['From'] = "gihs.airline@gmail.com"
                msg['To'] = str(details[4])
                if len(sel) == 1:
                    MESSAGE = """
DEAR {},

This email is to confirm your booking on {}.

FLIGHT DETAILS

    FLIGHT NUMBERS: {}

    DEPATURE DATES: {}

     DEPARTURE      ARRIVAL
            {}               {}
         {}         {}

    DURATION: {}

    SEAT: {}



PASSENGER DETAILS

    PASSPORT NUMBER: {}
    NAME: {}
    DOB: {}
    SEX: {}
    PHONE: {}
    PNR: : {}

Further details of your bookings are listed below:

BOOKING ID: {}
TOTAL FARE: {}

Amenities: Complementary Wifi,InFlight Entertainment,
            Airport Lounge,Inflight Gym

Baggage info: Free check-in baggage allowance is 30 kg per adult & child.
                Each bag must not exceed 32 kg and overall dimensions of
                checked baggage should not exceed 62 inches.

Cancellation policy: Cancellations made 7 days or more in advance of
                    the check-in day, will receive a 100% refund.
                    Cancellations made within 3 - 6 days will incur
                    a 20% fee. Cancellations made within 48 hours
                    to the check-in day will incur a 30% fee.
                    Cancellation made within 24 Hrs to the check-in
                    day will incur a 50% fee.

ABOUT THIS TRIP:

            Use your Trip ID for all communication

            Check-in counters for International flights
                close 75 minutes before departure

            Your carry-on baggage shouldn't weigh more than 7kgs

            Carry photo identification, you will need it as proof of
                identity while checking-in

            Kindly ensure that you have the relevant visa, immigration
                clearance and travel with a passport, with a validity of at least 6 months.

If you have any inqueries, Please do not hesitate to contact
or call the AIRLINE directly

We are looking forward to your visit and hope that you enjoy your stay
Best regards
""".format(details[2].upper(), date, sel.loc[0, "FLIGHT NO"], (str(sel.loc[0, "DEPARTURE_TIME"]))[:10], sel.loc[0, "ORIGIN"], sel.loc[0, "DESTINATION"], (str(sel.loc[0, "DEPARTURE_TIME"]))[-8:], sel.loc[0, "ARRIVAL_TIME"], sel.loc[0, "DURATION"], DET.loc[0, "SEAT"], pp_details[0], pp_details[1], pp_details[2], pp_details[3], pp_details[4], pp_details[5], booking_id, total)
                else:
                    MESSAGE = """
DEAR {},

This email is to confirm your booking on {}.

FLIGHT DETAILS

        FLIGHT NUMBER: {} and {}

        DEPATURE DATE: {} and {}

        DEPARTURE      ARRIVAL
                {}               {}
            {}         {}
                {}               {}
            {}         {}

        DURATIONS: {} and {}

        SEATS: {} and {}



PASSENGER DETAILS

        PASSPORT NUMBER: {}
        NAME: {}
        DOB: {}
        SEX: {}
        PHONE: {}
        PNR: : {}

Further details of your bookings are listed below:

BOOKING ID: {}
TOTAL FARE: {}

Amenities: Complementary Wifi,InFlight Entertainment,
            Airport Lounge,Inflight Gym

Baggage info: Free check-in baggage allowance is 30 kg per adult & child.
                Each bag must not exceed 32 kg and overall dimensions of
                checked baggage should not exceed 62 inches.

Cancellation policy: Cancellations made 7 days or more in advance of
                    the check-in day, will receive a 100% refund.
                    Cancellations made within 3 - 6 days will incur
                    a 20% fee. Cancellations made within 48 hours
                    to the check-in day will incur a 30% fee.
                    Cancellation made within 24 Hrs to the check-in
                    day will incur a 50% fee.

ABOUT THIS TRIP:

            Use your Trip ID for all communication

            Check-in counters for International flights
                close 75 minutes before departure

            Your carry-on baggage shouldn't weigh more than 7kgs

            Carry photo identification, you will need it as proof of
                identity while checking-in

            Kindly ensure that you have the relevant visa, immigration
                clearance and travel with a passport, with a validity of at least 6 months.

If you have any inqueries, Please do not hesitate to contact
or call the AIRLINE directly

We are looking forward to your visit and hope that you enjoy your stay
Best regards
""".format(details[2].upper(), date, sel.loc[0, "FLIGHT NO"], sel.loc[1, "FLIGHT NO"], (str(sel.loc[0, "DEPARTURE_TIME"]))[:10], (str(sel.loc[1, "DEPARTURE_TIME"]))[:10], sel.loc[0, "ORIGIN"], sel.loc[0, "DESTINATION"], (str(sel.loc[0, "DEPARTURE_TIME"]))[-8:], sel.loc[0, "ARRIVAL_TIME"], sel.loc[1, "ORIGIN"], sel.loc[1, "DESTINATION"], (str(sel.loc[1, "DEPARTURE_TIME"]))[-8:], sel.loc[1, "ARRIVAL_TIME"], sel.loc[0, "DURATION"], sel.loc[1, "DURATION"], DET.loc[0, "SEAT"], DET.loc[1, "SEAT"], pp_details[0], pp_details[1], pp_details[2], pp_details[3], pp_details[4], pp_details[5], booking_id, total)

                msg.set_content(MESSAGE)
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login("gihs.airline@gmail.com", "gelronfuifxcyheb")

                    smtp.send_message(msg)
                mydb.commit()
                print("\n", "="*8, 'THANK YOU FOR USING OUR SERVICE', "="*8, "\n")
                print(
                    "\n", "="*8, 'TO CONFIRM YOUR BOOKING PLEASE PAY THE MENTIONED AMOUNT', "="*8, "\n")
                print(
                    "\n", "="*8, 'PLEASE CHECK YOUR MAIL FOR FURTHER PROCEDURES', "="*8, "\n")

            except Exception:
                print("\n", "="*8, 'ERROR WHILE BOOKING FLIGHTS', "="*8, "\n")
                message = """
ERROR WHILE BOOKING FLIGHTS
PLEASE TRY AGAIN LATER

IF ERROR CONTINUES
FEEL FREE TO CONTACT USAT

gihs.airline@gmail.com

"""
                print(message)
                time.sleep(3)
                main()

        option = 1
        details = []
        FLIGHTS = []
        OPTION = []
        if dirr.empty:
            print("\n", "="*8, 'NO DIRECT FLIGHTS', "="*8, "\n")
        else:  # printing direct flights along with option number and uppending it to flight list
            del dirr["days"]
            print("\n", "="*8, 'DIRECT FLIGHTS', "="*8, "\n")
            print("\n", "="*4, "*ALL TIMINGS ARE IN GULF STANDARD TIME*", "="*4, "\n")
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
            print("\n", "="*4, "*ALL TIMINGS ARE IN GULF STANDARD TIME*", "="*4, "\n")
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
                SEATS_1 = []
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
                                                      "dest": "DESTINATION", "dep_time": "DEPARTURE_TIME", "arr_time": "ARRIVAL_TIME", "duration": "DURATION"})

                if res != []:
                    if len(res) == 1:
                        if details == []:
                            details = customer_input()
                        else:
                            pass
                        df = pd.DataFrame(res, columns=[
                            "FLIGHT NO", "ORIGIN", "DESTINATION", "DEPARTURE_TIME", "ARRIVAL_TIME", "DURATION", "SEAT_ID"])
                        zzz = df
                        Flight_no = zzz.iloc[0]["FLIGHT NO"]
                        p_x = selection[selection["FLIGHT NO"]
                                        == Flight_no].index.values
                        zzz["PRICE (USD)"] = selection.iloc[p_x[0]
                                                            ]["PRICE (USD)"]
                        seatid = df.iloc[0]["SEAT_ID"]
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
                                        seat = COLUMN+ROW
                                        list_seat_id.append(str(seatid))
                                        list_seat.append(COLUMN+ROW)
                                        SEATS_1.append(seats)
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
                        if details == []:
                            details = customer_input()
                        else:
                            pass
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
                                        seat = COLUMN+ROW
                                        list_seat_id.append(str(seatid[0]))
                                        list_seat.append(seat)
                                        SEATS_1.append(seats)
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
                                        seat = COLUMN+ROW
                                        list_seat_id.append(str(seatid[1]))
                                        list_seat.append(COLUMN+ROW)
                                        SEATS_1.append(seats)
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
                else:
                    selection = selection.reset_index()
                    selection = selection.drop("index", axis=1)
                    col = []
                    for i in selection.columns:
                        col.append(i)
                    selection1 = pd.DataFrame(columns=col)
                selection = selection.reset_index()
                selection = selection.drop("index", axis=1)
                if selection.empty == False:
                    if details == []:
                        details = customer_input()
                    else:
                        pass
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
                        else:
                            print(
                                "\n", "="*4, 'SEAT SELECTION FOR {} TO {}'.format(selection.iloc[1][1], selection.iloc[1][2]), "="*4, "\n")
                            selection1 = pd.concat(
                                [selection1, selection.iloc[1:, :]], axis=0)
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
                                if df.loc[ROW, COLUMN] == '0':
                                    df.loc[ROW, COLUMN] = "X"
                                    seats = [df.columns.values.tolist()] + \
                                        df.values.tolist()
                                    with open('seats/{}.txt'.format(seat_id), 'w') as f:
                                        f.write(json.dumps(seats))
                                    list_seat_id.append(str(seat_id))
                                    list_seat.append(COLUMN+ROW)
                                    SEATS_1.append(seats)
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


def FLIGHT_STATUS(xyz):
    def data_check(value, table, column):
        try:
            if type(value) == int:
                query = "select * from {} where {}={}".format(table, column, value)
                mycursor.execute(query)
                res = mycursor.fetchall()
                if res != []:
                    return True
                else:
                    return False
            else:
                query = "select * from {} where {}='{}'".format(table, column, value)
                mycursor.execute(query)
                res = mycursor.fetchall()
                if res != []:
                    return True
                else:
                    return False
        except Exception:
            return False
    while True:
        res = input("\nENTER BOOKING ID: ")
        BOOKING_ID = res
        try:
            res = int(res)
            a = data_check(res, "BOOKINGS", "BOOKING_ID")
            if a == True:
                break
            else:
                print("\n", "="*4, "ENTER VALID BOOKING ID", "="*4, "\n")
                continue
        except Exception:
            print("\n", "="*4, "ENTER VALID SEAT ID", "="*4, "\n")
            continue

    query = "select SEAT_ID FROM BOOKINGS WHERE BOOKING_ID={}".format(res)
    mycursor.execute(query)
    res = mycursor.fetchall()
    ress = []
    for i in res:
        for j in i:
            ress.append(j)
    res = ress
    if len(res) == 2:
        x = 2
    else:
        x = 1
    df = []
    temp = []
    for i in range(x):
        query = "select DELAY.FLIGHT_NO,DELAY.ORIGIN,DELAY.DESTINATION,DELAY.DEPATURE_TIME,DELAY.ARRIVAL_TIME,DELAY.DURATION,BOOKINGS.SEAT_NO,DELAY.DELAY from DELAY,BOOKINGS WHERE DELAY.SEAT_ID={} AND BOOKINGS.BOOKING_ID={} and BOOKINGS.SEAT_ID=DELAY.SEAT_ID".format(
            res[i], BOOKING_ID)
        mycursor.execute(query)
        for i in mycursor.fetchall():
            for j in i:
                temp.append(j)
            df.append(temp)
            temp = []

    df = pd.DataFrame(df, columns=["FLIGHT NO", "ORIGIN", "DESTINATION",
                                   "DEPARTURE TIME", "ARRIVAL TIME", "DURATION", "SEAT NO", "DELAY"])
    for i in range(len(df)):
        df.loc[i, "ARRIVAL TIME"] = (str(df.loc[i, "ARRIVAL TIME"]))[-8:]
        df.loc[i, "DURATION"] = (str(df.loc[i, "DURATION"]))[-8:]
        if df.loc[i, "DELAY"] == 0:
            df.loc[i, "DELAY"] = "ON TIME"
        else:
            df.loc[i, "DELAY"] = str(df.loc[i, "DELAY"]) + " MINUTES"
    print("\n", "="*4, "*THE MENTIONED DEPATURE TIME AND ARRIVAL TIME DO NOT ACCOUNT FOR DELAY*", "="*4, "\n")
    print("\n", df)
    if xyz == 0:
        main()
    else:
        return BOOKING_ID


def MANAGE_BOOKINGS():
    print("="*8, "MANAGE BOOKINGS", "="*8)

    def details(B):
        while True:
            booking_id = B
            query = "select * from BOOKINGS WHERE BOOKING_ID='{}'".format(
                booking_id)
            mycursor.execute(query)
            res = mycursor.fetchall()
            query = "SELECT SCHEDULE.FLIGHT_NO,SCHEDULE.ORIGIN,SCHEDULE.DESTINATION,SCHEDULE.DEPATURE_TIME,SCHEDULE.ARRIVAL_TIME ,SCHEDULE.DURATION,BOOKINGS.SEAT_NO,BOOKINGS.AMOUNT_USD,BOOKINGS.SEAT_ID FROM SCHEDULE,BOOKINGS WHERE BOOKINGS.SEAT_ID=SCHEDULE.SEAT_ID AND BOOKINGS.BOOKING_ID={}".format(
                booking_id)
            mycursor.execute(query)
            res = mycursor.fetchall()
            a = pd.DataFrame(res, columns=["FLIGHT NO", "ORIGIN", "DESTINATION", "DEPARTURE TIME",
                                           "ARRIVAL TIME", "DURATION", "SEAT NO", "AMOUNT (USD)", "SEAT ID"])
            for i in range(len(a)):
                a.loc[i, "ARRIVAL TIME"] = (str(a.loc[i, "ARRIVAL TIME"]))[-8:]
                a.loc[i, "DURATION"] = (str(a.loc[i, "DURATION"]))[-8:]
            return a

    def m_main():
        booking_id = FLIGHT_STATUS(1)
        detail = details(booking_id)
        opt = []
        while True:
            print("OPTION 1: CHANGE SEAT")
            print("OPTION 2: UPDATE PHONE NUMBER")
            print("OPTION 3: UPDATE EMAIL ID")
            print("OPTION 4: CANCEL BOOKING")
            print("OPTION 5: EXIT")
            list = [str(i) for i in range(1, 6)]
            res = input("\nENTER OPTION NUMBER: ")
            if res in list:
                opt.append(res)
                pass
            else:
                print("\n", "="*4, "ENTER VALID OPTION", "="*4, "\n")
                continue
            if res == "1":

                if len(detail) == 2:
                    while True:
                        z = input("DO YOU WANT TO CHANGE FOR BOTH FLIGHTS (Y/N): ")
                        z = z.upper()
                        z = z.strip()
                        if z not in ["Y", "N"]:
                            continue
                        elif z == "Y":
                            break
                        elif z == "N":
                            while True:
                                index = input("WHICH FLIGHT DO YOU WANT CHANGE SEAT FOR (1/2): ")
                                if index == "1":
                                    detail = detail.drop(1, axis=0)
                                    break
                                elif index == "2":
                                    detail = detail.drop(0, axis=0)
                                    break
                                else:
                                    print("\n", "="*4, "ENTER VALID OPTION", "="*4, "\n")
                                    continue
                            break

                detail = detail.reset_index()
                detail = detail.drop("index", axis=1)
                for i in range(len(detail)):
                    seat_id = str(detail.loc[i, "SEAT ID"])
                    seat_no = str(detail.loc[i, "SEAT NO"])
                    print(seat_no)
                    with open(os.getcwd()+'/SEATS/{}.txt'.format(seat_id), 'r') as f:
                        seat_list = json.loads(f.read())
                    indexx = [0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19, 20, 21,
                              22, 23, 24, 25, 26, 0, 27, 28, 29, 30,  31, 32, 33, 34, 35, 36, 37, 38]

                    df = pd.DataFrame(
                        seat_list[1:], columns=seat_list[0], index=indexx)
                    df.loc[int(seat_no[1]), seat_no[0]] = "0"
                    print(
                        "\n", "="*4, 'SEAT SELECTION FOR {} TO {}'.format(detail.loc[i, "ORIGIN"], detail.loc[i, "DESTINATION"]), "="*4, "\n")
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
                                seats = [df.columns.values.tolist()] + \
                                    df.values.tolist()
                                with open('seats/{}.txt'.format(seat_id), 'w') as f:
                                    f.write(json.dumps(seats))
                                print(df)
                                seat_no = COLUMN+ROW
                                query = "update BOOKINGS set SEAT_NO='{}' WHERE SEAT_ID={}".format(
                                    seat_no, seat_id)
                                mycursor.execute(query)
                                mydb.commit()
                                print("\n", "="*4, "SEAT CHANGED SUCCESSFULLY", "="*4, "\n")

                                break
                continue
            elif res == '2':

                seat_id = detail.loc[0, 'SEAT NO']
                while True:  # taking input and valiation for phone number
                    customer_phone = input(
                        "ENTER PASSENGER PHONE NUMBER ((COUNTRY CODE)-########): ")
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

                query = "select CUSTOMER_ID from BOOKINGS WHERE BOOKING_ID={}".format(booking_id)
                mycursor.execute(query)
                res = mycursor.fetchall()
                customer_id = res[0][0]
                query = "update CUSTOMERS set CUSTOMER_PHONE='{}' WHERE CUSTOMER_ID ={} ".format(
                    customer_phone, customer_id,)
                mycursor.execute(query)
                mydb.commit()
                print("\n", "="*4, "PHONE NUMBER CHANGED SUCCESSFULLY", "="*4, "\n")
                continue

            elif res == '3':

                seat_id = detail.loc[0, 'SEAT NO']
                while True:  # taking input and valiation for EMAIL
                    customer_email = input("\nENTER NEW PASSENGER EMAIL ADDRESS: ")
                    customer_email = customer_email.strip()
                    customer_email = customer_email.lower()
                    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                    if(re.search(regex, customer_email)):
                        break

                    else:
                        print("\n", "="*4,
                              'PLEASE ENTER VALID EMAIL ID', "="*4, "\n")
                        continue

                query = "select CUSTOMER_ID from BOOKINGS WHERE BOOKING_ID={}".format(booking_id)
                mycursor.execute(query)
                res = mycursor.fetchall()
                customer_id = res[0][0]
                query = "update CUSTOMERS set CUSTOMER_EMAIL='{}' WHERE CUSTOMER_ID ={} ".format(
                    customer_email, customer_id,)
                mycursor.execute(query)
                mydb.commit()
                print("\n", "="*4, "EMAIL CHANGED SUCCESSFULLY", "="*4, "\n")
                continue

            elif res == '4':

                for i in range(len(detail)):
                    seat_id = str(detail.loc[i, "SEAT ID"])
                    seat_no = str(detail.loc[i, "SEAT NO"])
                    print(seat_no)
                    with open(os.getcwd()+'/SEATS/{}.txt'.format(seat_id), 'r') as f:
                        seat_list = json.loads(f.read())
                    indexx = [0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19, 20, 21,
                              22, 23, 24, 25, 26, 0, 27, 28, 29, 30,  31, 32, 33, 34, 35, 36, 37, 38]

                    df = pd.DataFrame(
                        seat_list[1:], columns=seat_list[0], index=indexx)
                    df.loc[int(seat_no[1]), seat_no[0]] = "0"
                    seats = [df.columns.values.tolist()] + \
                        df.values.tolist()
                    with open('seats/{}.txt'.format(seat_id), 'w') as f:
                        f.write(json.dumps(seats))
                query = "delete from BOOKINGS where BOOKING_ID={}".format(booking_id)
                mycursor.execute(query)
                mydb.commit()
                print("\n", "="*4, "BOOKING CANCELED SUCCESSFULLY", "="*4, "\n")
                continue

            elif res == '5':
                if opt != []:
                    query = "select CUSTOMER_NAME,CUSTOMER_EMAIL FROM CUSTOMERS,BOOKINGS WHERE CUSTOMERS.CUSTOMER_ID=BOOKINGS.CUSTOMER_ID AND BOOKINGS.BOOKING_ID={}".format(
                        booking_id)
                    mycursor.execute(query)
                    res = mycursor.fetchall()
                    NAME = res[0][0]
                    EMAIL = res[0][1]
                    taskdone = {1: "SEAT CHANGED", 2: "PHONE NUMBER UPDATED",
                                3: "EMAIL ADDRESS UPDATED", 4: "BOOKING CANCELLED"}
                    m = ""
                    for i in opt:
                        if int(i) in taskdone.keys():
                            m = m + "\n"+taskdone[int(i)]

                    MESSAGE = """
DEAR {},

This is to inform that you have updated your
flight details.

CHANGES MADE:
    {}

IF YOU HAVE NOT MADE ANY CHANGES PLEASE CONTACT US
email us at: gihs.airlines@gmail.com
call us at:  04-XXXXXXX
""".format(NAME, m)
                    mail(EMAIL, MESSAGE)

                main()
                break

    m_main()


def STAFF_LOGIN():
    print("\n", "="*8, "STAFF LOGIN", "="*8, "\n")

    def ANALYZE_DATA(x):
        df1 = pd.DataFrame()
        temp = ""
        while True:
            print("\n")
            print("OPTION 1: NO. OF FLIGHTS FLYING IN A MONTH")
            print("OPTION 2: NO. OF BOOKING DONE IN EACH MONTH")
            print("OPTION 3: NO. FLIGHTS IN BOOKED EACH ROUTES")
            print("OPTION 4: EARNINGS PER MONTH")
            print("OPTION 5: EXIT")
            list = ['1', '2', '3', '4', '5', '6']
            while True:
                res = input("\nENTER THE OPTION NO: ")
                if res in list:
                    break
                else:
                    print("\n", "="*4, "PLEASE ENTER A VALID OPTION", "="*4, "\n")
                    continue
            if res == '1':
                query = "SELECT DISTINCT YEAR(DEPATURE_TIME) as YEAR, MONTH(DEPATURE_TIME) AS MONTH , COUNT(DISTINCT SEAT_ID) FROM SCHEDULE GROUP BY YEAR(DEPATURE_TIME) , MONTH(DEPATURE_TIME) ORDER BY YEAR(DEPATURE_TIME) , MONTH(DEPATURE_TIME)"
                mycursor.execute(query)
                data = mycursor.fetchall()
                df = pd.DataFrame(data, columns=['YEAR', 'MONTH', 'NO. OF FLIGHTS'])
                query = "SELECT DISTINCT YEAR(DEPATURE_TIME) as YEAR, MONTH(DEPATURE_TIME) AS MONTH , COUNT(DISTINCT SEAT_ID) FROM E_SCHEDULE GROUP BY YEAR(DEPATURE_TIME) , MONTH(DEPATURE_TIME) ORDER BY YEAR(DEPATURE_TIME) , MONTH(DEPATURE_TIME)"
                mycursor.execute(query)
                data = mycursor.fetchall()
                df1 = pd.DataFrame(data, columns=['YEAR', 'MONTH', 'NO. OF FLIGHTS'])
                temp1 = str(df)
                temp2 = str(df1)
                temp = "\nNUMBER OF PENDING FLIGHTS\n\n" + temp1+"\n\nNUMBER OF FLIGHTS FLOWN \n\n"+temp2+"\n"
                title = ["NUMBER OF PENDING FLIGHTS", "NUMBER OF FLIGHTS FLOWN"]
            elif res == '2':
                query = "SELECT DISTINCT YEAR(DATE_OF_BOOKING) as YEAR, MONTH(DATE_OF_BOOKING) AS MONTH , COUNT(DISTINCT SEAT_ID) FROM BOOKINGS GROUP BY YEAR(DATE_OF_BOOKING) , MONTH(DATE_OF_BOOKING) ORDER BY YEAR(DATE_OF_BOOKING) , MONTH(DATE_OF_BOOKING)"
                mycursor.execute(query)
                data = mycursor.fetchall()
                df = pd.DataFrame(data, columns=['YEAR', 'MONTH', 'NO. OF BOOKINGS'])
                query = "SELECT DISTINCT YEAR(DATE_OF_BOOKING) as YEAR, MONTH(DATE_OF_BOOKING) AS MONTH , COUNT(DISTINCT SEAT_ID) FROM E_BOOKINGS GROUP BY YEAR(DATE_OF_BOOKING) , MONTH(DATE_OF_BOOKING) ORDER BY YEAR(DATE_OF_BOOKING) , MONTH(DATE_OF_BOOKING)"
                mycursor.execute(query)
                data = mycursor.fetchall()
                df1 = pd.DataFrame(data, columns=['YEAR', 'MONTH', 'NO. OF BOOKINGS'])
                temp1 = str(df)
                temp2 = str(df1)
                temp = "\nNUMBER OF BOOKINGS DONE IN EACH MONTH\n\n" + temp1+"\n\nNUMBER OF BOOKINGS DONE IN EACH MONTH (EXPIRED FLIGHTS) \n\n"+temp2+"\n"
                title = ["NUMBER OF IN BOOKINGS DONE EACH MONTH", "NUMBER OF  BOOKINGS DONE IN EACH MONTH (EXPIRED FLIGHTS)"]

            elif res == "3":
                query = "SELECT DISTINCT ORIGIN, DESTINATION, COUNT(DISTINCT SEAT_ID) AS 'NO. OF  FLIGHTS' from SCHEDULE GROUP BY ORIGIN,DESTINATION ORDER BY COUNT(DISTINCT SEAT_ID) DESC"
                mycursor.execute(query)
                data = mycursor.fetchall()
                df = pd.DataFrame(data, columns=["ORIGIN", "DESTINATION", "NO. OF FLIGHTS"])
                title = ["NUMBER OF FLIGHTS BOOKED IN EACH ROUTES"]
            elif res == "4":
                query = "SELECT DISTINCT YEAR(DATE_OF_BOOKING) as YEAR, MONTH(DATE_OF_BOOKING) AS MONTH , SUM(AMOUNT_USD) FROM BOOKINGS GROUP BY YEAR(DATE_OF_BOOKING) , MONTH(DATE_OF_BOOKING) ORDER BY YEAR(DATE_OF_BOOKING) , MONTH(DATE_OF_BOOKING)"
                mycursor.execute(query)
                data = mycursor.fetchall()
                df = pd.DataFrame(data, columns=["YEAR", "MONTH", "INCOME"])
                query = "SELECT DISTINCT YEAR(DATE_OF_BOOKING) as YEAR, MONTH(DATE_OF_BOOKING) AS MONTH , SUM(AMOUNT_USD) FROM E_BOOKINGS GROUP BY YEAR(DATE_OF_BOOKING) , MONTH(DATE_OF_BOOKING) ORDER BY YEAR(DATE_OF_BOOKING) , MONTH(DATE_OF_BOOKING)"
                mycursor.execute(query)
                data = mycursor.fetchall()
                df1 = pd.DataFrame(data, columns=["YEAR", "MONTH", "INCOME"])
                temp1 = str(df)
                temp2 = str(df1)
                temp = "\nINCOME FROM PENDING FLIGHTS\n\n" + temp1+"\n\nINCOME FROM FLIGHTS FLOWN\n\n"+temp2+"\n"
                title = ["INCOME FROM PENDING FLIGHTS", "INCOME FROM FLIGHTS FLOWN"]
            elif res == "5":
                break
            if x == 1:
                if temp != "":
                    print(temp)
                    temp = ""
                else:
                    print(df)
                continue
            else:
                return df, df1, title, res

    def ADD_DELAY(delay, seat_id):
        query = "UPDATE DELAY SET DELAY={} WHERE SEAT_ID={}".format(res, seat_id)
        mycursor.execute(query)
        pass

    def VIUSALIZE_DATA():
        data = ANALYZE_DATA(2)
        res = data[-1]
        titles = data[-2]
        data = data[:-2]
        temp = []
        for i in data:
            temp.append(i)
        data = temp
        temp = data
        for i in range(len(temp)):
            a = temp[i]
            if a.empty:
                data.pop(i)
        temp = []
        ToPlot = []
        for i in range(len(data)):
            df = data[i]
            cols = []
            for i in df.columns:
                cols.append(i)
            col_y = cols[-1]
            if res == "3":
                for i in range(len(df)):
                    b = str(df.loc[i, "ORIGIN"])+"-"+str(df.loc[i, "DESTINATION"])
                    temp.append(b)
                df.insert(2, "x axis", temp)
                df = df.drop(["ORIGIN", "DESTINATION"], axis=1)
                df = df.rename(columns={col_y: "y axis"})
            else:
                for i in range(len(df)):
                    b = str(df.loc[i, "YEAR"])+"-"+str(df.loc[i, "MONTH"])
                    temp.append(b)
                df.insert(2, "x axis", temp)
                df = df.drop(["YEAR", "MONTH"], axis=1)
                df = df.rename(columns={col_y: "y axis"})
            temp = []
            ToPlot.append(df)
        for i in range(len(titles)):
            if res == "1":
                ToPlot[i].plot(x="x axis", y="y axis", kind="bar")
                plt.xlabel("DATES")
                plt.ylabel("NO. OF FLIGHTS")
                plt.xticks(rotation=30)
                plt.title(titles[i])
                plt.show()
            if res == "2":
                ToPlot[i].plot(x="x axis", y="y axis", kind="bar")
                plt.xlabel("DATES")
                plt.ylabel("NO. OF BOOKINGS")
                plt.xticks(rotation=30)
                plt.title(titles[i])
                plt.show()
            elif res == "3":
                ToPlot[i].plot(x="x axis", y="y axis", kind="bar")
                plt.xlabel("ROUTES")
                plt.ylabel("NO. OF FLIGHTS")
                plt.xticks(rotation=30)
                plt.title(titles[i])
                plt.show()
            elif res == "4":
                a = ToPlot[i]
                for b in range(len(a)):
                    a.loc[b, "y axis"] = int(a.loc[b, "y axis"])
                a.plot(x="x axis", y="y axis", kind="bar")
                plt.xlabel("DATES")
                plt.ylabel("INCOME")
                plt.xticks(rotation=30)
                plt.title(titles[i])
                plt.show()
        pass

    def data_check(value, table, column):
        try:
            if type(value) == int:
                query = "select * from {} where {}={}".format(table, column, value)
                mycursor.execute(query)
                res = mycursor.fetchall()
                if res != []:
                    return True
                else:
                    return False
            else:
                query = "select * from {} where {}='{}'".format(table, column, value)
                mycursor.execute(query)
                res = mycursor.fetchall()
                if res != []:
                    return True
                else:
                    return False
        except Exception:
            return False
        pass

    def VIEW_DB():
        query = "show tables"
        mycursor.execute(query)
        res = []
        for i in mycursor.fetchall():
            for j in i:
                res.append(j)
        print("\n")
        opt = []
        for i in range(1, len(res)+1):
            MESSAGE = "OPTION {}: {} ".format(i, res[i-1])
            print(MESSAGE)
            opt.append(i)
        tables = res
        print
        while True:
            res = input("\nENTER OPTION NUMBER: ")
            try:
                res = int(res)
                if res in opt:
                    res = res-1
                    break
                else:
                    print("\n", "="*4, "ENTER VALID OPTION", "="*4, "\n")
                    continue
            except Exception:
                print("\n", "="*4, "ENTER VALID OPTION", "="*4, "\n")
                continue

        query = "show COLUMNS FROM {}".format(tables[res])
        print(query)
        mycursor.execute(query)
        df = pd.DataFrame(mycursor.fetchall())
        cols = []
        for i in range(len(df)):
            cols.append(df.iloc[i, 0])

        data = []
        data.append(cols)
        query = "select * from {}".format(tables[res])
        mycursor.execute(query)
        temp = []
        for i in mycursor.fetchall():
            for j in i:
                temp.append(j)
            data.append(temp)
            temp = []
        df = pd.DataFrame(data[1:], columns=data[0])
        print("\n")
        PAT = "/DB/{}.csv".format(tables[res])
        df.to_csv(r'{}'.format(os.getcwd()+PAT))
        print("TABLE EXPORTED TO DB FOLDER")
        time.sleep(3)
        main()
        pass
    while True:
        USERNAME = input("\nENTER USERNAME: ")
        USERNAME = USERNAME.strip()
        query = "select * from STAFFS WHERE USERNAME='{}'".format(USERNAME)
        try:
            mycursor.execute(query)
        except Exception:
            print("\n", "="*4, "ENTER VALID USERNAME", "="*4, "\n")
            continue
        res = mycursor.fetchall()
        if res != []:
            break
        else:
            print("\n", "="*4, "ENTER VALID USERNAME", "="*4, "\n")
            continue
    while True:
        PASSWORD = input("\nENTER PASSWORD: ")
        PASSWORD = PASSWORD.strip()
        query = "select EMPL_NAME from STAFFS where USERNAME='{}' and PASSWORD='{}'".format(
            USERNAME, PASSWORD)
        try:
            mycursor.execute(query)
        except Exception:
            print("\n", "="*4, "ENTER VALID PASSWORD", "="*4, "\n")
            continue
        res = mycursor.fetchall()
        if res != []:
            break
        else:
            print("\n", "="*4, "ENTER VALID PASSWORD", "="*4, "\n")
            continue

    NAME = res[0][0]
    print("\n", "="*4, "WELCOME BACK {}".format(NAME), "="*4, "\n")

    while True:
        print("\n")
        print("OPTION 1: ANALYZE DATA")
        print("OPTION 2: ADD DELAY")
        print("OPTION 3: VIUSALIZE DATA")
        print("OPTION 4: VIEW DB")
        print("OPTION 5: EXIT")
        list = ["1", "2", "3", "4", "5"]
        while True:
            res = input("\nENTER OPTION NUMBER: ")
            res = res.strip()
            if res not in list:
                print("\n", "="*4, "ENTER A VALID OPTION", "="*4, "\n")
                continue
            else:
                break

        if int(res) == 1:
            ANALYZE_DATA(1)
            continue
        elif int(res) == 2:
            while True:
                flight_no = input("ENTER FLIGHT NUMBER: ")
                depature_date = input("ENTER DATE AND TIME (YYYY-MM-DD HH:MM:SS): ")
                query = "select SEAT_ID from SCHEDULE where FLIGHT_NO='{}' AND DEPATURE_TIME='{}'".format(
                    flight_no, depature_date)
                mycursor.execute(query)
                seat_id = mycursor.fetchall()

                if seat_id != []:
                    seat_id = seat_id[0][0]
                    while True:
                        res = input("\nENTER DELAY IN MINUTES: ")
                        try:
                            res = int(res)
                            ADD_DELAY(res, seat_id)
                            mydb.commit()
                            break
                        except Exception:
                            print("\n", "="*4, "ENTER ONLY NUMBERS", "="*4, "\n")
                            continue
                        break
                    break

                else:
                    print("\n", "="*4, "ENTER VALID DETAILS", "="*4, "\n")
                    continue
            continue

        elif int(res) == 4:
            VIEW_DB()
            continue

        elif int(res) == 3:
            VIUSALIZE_DATA()
            continue
        else:
            main()
            break


def ABOUT():
    print("="*8, "ABOUT", "="*8)


main()
