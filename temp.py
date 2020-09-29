import pandas as pd  
import sys

list=[[1,2,3],[7,8,9]]
df=pd.DataFrame(list)
print(df)
print(df.loc[0,1])
a=df.isin(["1"]).any()
print(type(a))
b=[]
for i in a:
    b.append(i)
sys.exit()
if True not in b:
    print("fo")
else:
    print("get")
    



