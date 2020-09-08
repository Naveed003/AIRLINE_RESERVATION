import pandas as pd
list=[["1","1","","","1","1"]]
a="0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
indexx=[]
for i in range(len(a)):
    indexx.append(str(a[i]))
df=pd.DataFrame(list,columns=["1","2","","","3","4"],index=indexx)
print(df)