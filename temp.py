import pandas as pd
import sys
"""
list = [[1, 2, 3], [7, 8, 9]]
df = pd.DataFrame(list,columns=["a","b","c"])
df.insert(2,"hello",["31","32"])
total=1234
print("\nTOTAL FARE: ${:,.2f}".format(total))
print(df)
pp_details=[['12345678', 'NAVE', 4866]]
pp_detail=pd.DataFrame(pp_details,columns=["PASSPORT NUMBER","NAME","PNR"])

text="helglo "
print(text[0:-2])
"""

""" import datetime
C_TIME=str(datetime.datetime.now())[11:-7] """
""" 
def b():
    a=input("enter num: ")
    if int(a)%2==0:
        a="even"
        return True,a
    else:
        a="ODD"
        return True,a


ll=b()

print(ll) """

""" def a():
    print("a")
def b():
    def z():
        a()
    z()
b() """

""" df=[["col1","col2","col3"],[1,2,3],["a","b","c"]]
df=pd.DataFrame(df[1:],columns=df[0])
df=df.rename(columns={"col1":"hello"})
cols=[]
for i in df.columns:
    cols.append(i)

print(cols[-1])
df=df.rename(columns={"col1":"hello"}) """

""" import random
while True:
    a=random.choice(["a","b","c"])
    print(a) """

import pycountry
from datetime import date
""" 
a=list(pycountry.countries)
for i in a:
    print(a) """
""" a=date.today()
print(int((str(a))[-2:])) """

# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# Create data
height = [3, 12, 5, 18, 45]
bars = ("very long group name 1","very long group name 2","very long group name 3","very long group name 4","very long group name 5")
 
# Create bars
plt.bar([1,2,3,4,5],height)
 
# Rotation of the bars names
plt.xticks([1,2,3,4,5], bars, rotation=90)
 
# Custom the subplot layout
plt.subplots_adjust(bottom=0.7, top=0.99)
 
# Show graphic
plt.show()