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
 

    

