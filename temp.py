""" import pandas as pd
import sys

list = [[1, 2, 3], [7, 8, 9]]
df = pd.DataFrame(list,columns=["a","b","c"])
df.insert(2,"hello",["31","32"])
total=1234
print("\nTOTAL FARE: ${:,.2f}".format(total))
print(df)
pp_details=[['12345678', 'NAVE', 4866]]
pp_detail=pd.DataFrame(pp_details,columns=["PASSPORT NUMBER","NAME","PNR"])

text="helglo "
print("\u0332".join(text)) """

1,4,5,6,12