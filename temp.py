import pandas as pd  

list=[[1,2,3],[1,8,9]]
df=pd.DataFrame(list)
print(df)
print(df.isin(["1"]).any())
