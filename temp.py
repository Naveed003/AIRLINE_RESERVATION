import pandas as pd
import sys

list = [[1, 2, 3], [7, 8, 9]]
df = pd.DataFrame(list,columns=["a","b","c"])
df.loc[1,"b"]=7
print(df)

