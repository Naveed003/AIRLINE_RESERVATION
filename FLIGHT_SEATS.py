import pandas as pd
df1=pd.DataFrame()
list=[["0","0","","","0","0"]]
list1=[["","","","","",""]]
a="0ABCD0EFGHIJKL0MNOPQRSTUVWXYZ"
indexx=[]
index1=[]
df=pd.DataFrame(columns=["1","2","","","3","4"])
for i in range(len(a)):
    indexx=str(a[i])
    index1=[indexx]
    if indexx != '0':
        df1=pd.DataFrame(list,columns=["1","2","","","3","4"],index=index1)
        df = pd.concat([df, df1])
    else:
        df1=pd.DataFrame(list1,columns=["1","2","","","3","4"],index=index1)
        df = pd.concat([df, df1])
print(df)
