import pandas as pd
import random

def F_n():
    global B
    import random
    import json
    with open('flight_Numbers.txt', 'r') as f:
        flight_Numbers = json.loads(f.read())
    while True:
        B=random.randint(100,999)
        if B in flight_Numbers:
            print(B)
            pass
        else:
            flight_Numbers.append(B)
            
            with open('flight_Numbers.txt', 'w') as f:
                f.write(json.dumps(flight_Numbers))
            break
 

COUNTRY1 = "DXB"
COUNTRY2 = input("ENTER COUNTRY 2: ").upper()
COUNTRY3 = input("ENTER COUNTRY 3: ").upper()
F_n()
flight_id1 = "G"+str(B)
F_n()
flight_id2 = "G"+str(B)
F_n()
flight_id3 = "G"+str(B)
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