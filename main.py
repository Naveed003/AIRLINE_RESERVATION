from datetime import date
import sqlite3
import pandas as pd
import time
import random
from random import randint
from datetime import datetime
import mysql.connector



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
    def arrival():
        print("\n", "="*4, "ARRIVAL", "="*4)
        print("\n")
        for i in range(0, len(list)):
            p_command = "OPTION {}: {}".format(i+1, list[i])
            print(p_command)
        count = 0
        while True:
            response = input("\nEnter Option Number: ")
            response.strip()
            if response not in ["1", "2", "3", "4"]:
                count += 1
                if count > 3:
                    while True:
                        response = input("Do you want to try again (Y/N): ")
                        if response.lower() == "y":
                            break
                        elif response.lower() == "n":
                            main()
                            break
                        else:
                            countt += 1
                            if countt > 3:
                                main()
                                break

                print("="*20, "ENTER VALID OPTION", "="*20)

            else:
                global arr
                arr = list[int(response)-1]
                arr = arr[-4:-1]
                break

    print("\n", "="*8, "NEW BOOKING", "="*8)
    print("\n", "="*4, "DEPATURE", "="*4)
    print("\nOPTION 1: Dubai International Airport (DXB)")
    print("OPTION 2: John F. Kennedy International Airport (JFK)")
    print("OPTION 3: Heathrow Airport (LHR)")
    print("OPTION 4: Chhatrapati Shivaji Maharaj International Airport (BOM)")
    print("OPTION 5: Sydney Airport (SYD)")
    global list
    list = [
        "Dubai International Airport (DXB)",
        "John F. Kennedy International Airport (JFK)",
        "Heathrow Airport (LHR)",
        "Chhatrapati Shivaji Maharaj International Airport (BOM)",
        "Sydney Airport (SYD)"
    ]
    COUNT = 0
    global dep
    while True:
        response = input("\nEnter Option number: ")
        response.strip()
        if response == "1":
            dep = "DXB"
            list.remove("Dubai International Airport (DXB)")
            arrival()
            break
        elif response == "2":
            dep = "JFK"
            list.remove("John F. Kennedy International Airport (JFK)")
            arrival()
            break
        elif response == "3":
            dep = "LHR"
            list.remove("Heathrow Airport (LHR)")
            arrival()
            break
        elif response == "4":
            dep = "BOM"
            list.remove(
                "Chhatrapati Shivaji Maharaj International Airport (BOM)")
            arrival()
            break
        elif response == "5":
            dep = "SYD"
            list.remove("Sydney Airport (SYD)")
            arrival()
            break
        else:
            COUNT += 1
            countt = 0
            if COUNT < 4:
                while True:
                    response = input("Do you want to try again (Y/N): ")
                    if response.lower() == "y":
                        break
                    elif response.lower() == "n":
                        main()
                        break
                    else:
                        countt += 1
                        if countt > 3:
                            main()
                            break
                        print("\n", "="*4, "ENTER VALID OPTION", "="*4)
            else:
                print("TRY AGAIN")
                main()
                break


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



