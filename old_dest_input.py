ef NEW_BOOKING():
    def arrival():
        print("\n", "="*4, "ARRIVAL", "="*4)
        print("\n")
        for i in range(0, len(list)):
            p_command = "OPTION {}: {}".format(i+1, list[i])
            print(p_command)
        count = 0
        No_of_locations=[]
        for i in range(1,len(list)+1):
            No_of_locations.append(str(i))
        while True:
            response = input("\nEnter Option Number: ")
            response.strip()
            if response not in No_of_locations:
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
        list = [DXB]
        if response == "1":
            dep = "DXB"
            list.remove("Dubai International Airport (DXB)")
            break
        elif response == "2":
            dep = "JFK"
            list.remove("John F. Kennedy International Airport (JFK)")
            break
        elif response == "3":
            dep = "LHR"
            list.remove("Heathrow Airport (LHR)")
            break
        elif response == "4":
            dep = "BOM"
            list.remove(
                "Chhatrapati Shivaji Maharaj International Airport (BOM)")
            break
        elif response == "5":
            dep = "SYD"
            list.remove("Sydney Airport (SYD)")
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
    arrival()
