from datetime import date
import sqlite3
import pandas as pd
import time
import random
from random import randint
from datetime import datetime
import mysql.connector
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
        date_input()

    def addYears(d,years):
        global f_date
        try:
            f_date=d.replace(year=d.year+years)
            print(f_date)
        except ValueError:
            f_date=d + (date(d.year+years,1,1)-date(d.year,1,1))
            print(f_date)



    def date_input():
        current_date = date.today()
        addYears(current_date,1)
        while True:
            depature_date = input("ENTER DEPATURE DATE (YYYY-MM-DD): ")
            if str(current_date) <= depature_date and str(f_date)>depature_date:
                dep_date = depature_date
                break
            else:
                print("\n", "="*4, 'Please Enter a Valid Date ', "="*4)

    def flights_extract():
        pass
    dep_arrival_input()


def FLIGHT_STATUS():
    print("="*8, "FLIGHT STATUS", "="*8)


def MANAGE_BOOKINGS():
    print("="*8, "MANAGE BOOKINGS", "="*8)


def STAFF_LOGIN():
    print("="*8, "STAFF LOGIN", "="*8)


def ABOUT():
    print("="*8, "ABOUT", "="*8)


main()
print(arr, dep)


"""while True:
    response = input("\nENTER OPTION NUMBER: ")
    if response == "1":
        NEW_BOOKING()
    elif response == "2":
        FLIGHT_STATUS()
    elif response == "3":
        MANAGE_BOOKINGS()
    elif response == "4":
        STAFF_LOGIN()
    elif response == "5":
        ABOUT()
    elif response == "6":
        break
    else:
        print("="*20, "ENTER VALID OPTION", "="*20)"""
