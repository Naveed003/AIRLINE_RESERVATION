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
response=input("ENTER OPTION NUMBER: ")
if response=="1":
    NEW_BOOKING()
if response=="2":
    FLIGHT_STATUS()
if response=="3":
    MANAGE_BOOKINGS()
if response=="4":
    STAFF_LOGIN()
if response=="5":
    ABOUT()
