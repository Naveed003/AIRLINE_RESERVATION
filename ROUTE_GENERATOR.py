import pandas as pd
import random


COUNTRY1 = "DXB"
COUNTRY2 = input("ENTER COUNTRY 2: ").upper()
COUNTRY3 = input("ENTER COUNTRY 3: ").upper()

flight_id1 = "G"+str(random.randint(100, 999))
flight_id2 = "G"+str(random.randint(100, 999))
flight_id3 = "G"+str(random.randint(100, 999))
list = [
    ["FLIGHT_NO", "ORIGIN", "DESTINATION"],
    [flight_id1, COUNTRY1, COUNTRY2],
    [flight_id1, COUNTRY2, COUNTRY1],
    [flight_id2, COUNTRY1, COUNTRY3],
    [flight_id2, COUNTRY3, COUNTRY1],
    [flight_id3, COUNTRY1, COUNTRY2],
    [flight_id3, COUNTRY2, COUNTRY3],
    [flight_id3, COUNTRY3, COUNTRY2],
    [flight_id3, COUNTRY2, COUNTRY1],
]
df = pd.DataFrame(list[1:], columns=list[0])
print(df)
