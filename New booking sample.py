print("\n", "="*8, "NEW BOOKING", "="*8)
print("\n", "="*4, "DEPATURE", "="*4)
print("\nCODE DXB: Dubai International Airport")
print("CODE JFK: John F. Kennedy International Airport")
print("CODE LHR: Heathrow Airport")
print("CODE BOM: Chhatrapati Shivaji Maharaj International Airport")
print("CODE SYD: Sydney Airport")
list=['DXB','JFK','LHR','BOM','SYD']
global dep 
while True:
    global dep
    dep=input('\nEnter the Respective Code: ')
    dep = dep.strip()
    dep = dep.upper()
    if dep in list:
        break
    else:
        print("\n", "="*4,'Please Enter a Valid code', "="*4)
        pass

index=list.index(dep)
list.remove(dep)
print(list)
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
    arr=input('\nEnter the Respective Code: ')
    arr = arr.strip()
    arr = arr.upper()
    if arr in list:
        break
    else:
        print("\n", "="*4,'Please Enter a Valid code', "="*4)
        pass

