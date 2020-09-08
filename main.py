from datetime import date
import sqlite3
import pandas as pd
import time
import random
from random import randint
from datetime import datetime
import mysql.connector
from funtions import *




main()
while True:
 response=input("ENTER OPTION NUMBER: ")
 if response=="1":
    NEW_BOOKING()
 elif response=="2":
    FLIGHT_STATUS()
 elif response=="3":
    MANAGE_BOOKINGS()
 elif response=="4":
    STAFF_LOGIN()
 elif response=="5":
    ABOUT()
 elif response=="6":
    break
 else:
    print("="*20, "ENTER VALID OPTION", "="*20)
