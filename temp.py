import pycountry
while True:

    a=input("netrr: ")


    b=list(pycountry.countries)
    try:
        
        if pycountry.countries.get(name=a)!=None:
            print("dfs")
        else:
            print("stop dies")
    except Exception:
        print("fo")



