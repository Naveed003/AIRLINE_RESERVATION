def seat_ids():
    global seat_id
    import random
    import json
    import os

    seat_id = []
    with open(os.getcwd()+'/SEATS/seat_ids.txt', 'r') as f:
        seat_ids = json.loads(f.read())
    while True:
        seat_id = random.randint(0, 999999)
        if seat_id in seat_ids:
            print(seat_id)
            pass
        else:
            seat_ids.append(seat_id)

            with open('SEATS/seat_ids.txt', 'w') as f:
                f.write(json.dumps(seat_ids))
            break
    return seat_id


def flight_seat(x):
    if x == 1:
        import os
        import pandas as pd
        import json
        seatid = seat_ids()
        df1 = pd.DataFrame()
        list = [["0", "0", "", "", "0", "0", "0", "0", "", "", "0", "0"]]
        list1 = [["", "", "", "", "", "", "", "", "", "", "", ""]]
        a = [0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19, 20, 21,
             22, 23, 24, 25, 26, 0, 27, 28, 29, 30,  31, 32, 33, 34, 35, 38, 37, 38]
        indexx = []
        index1 = []
        df = pd.DataFrame(columns=["A", "B", "", "", "C",
                                   "D", "E", "F", "", "", "G", "H"])
        for i in range(len(a)):
            indexx = str(a[i])
            index1 = [indexx]
            if indexx != '0':
                df1 = pd.DataFrame(list, columns=["A", "B", "", "", "C",
                                                  "D", "E", "F", "", "", "G", "H"], index=index1)
                df = pd.concat([df, df1])
            else:
                df1 = pd.DataFrame(list1, columns=["A", "B", "", "",
                                                   "C", "D", "E", "F", "", "", "G", "H"], index=index1)
                df = pd.concat([df, df1])

        print("\n", "="*4, 'SEAT SELECTION', "="*4, "\n")

        print("\t0=AVAILABLE AND X=BOOKED\n")

        df.to_csv(os.getcwd()+r'/SEATS/{}.csv'.format(seatid))
        return df
    if x == 2:
        return seat_id



