import pandas as pd
import sys

list = [[1, 2, 3], [7, 8, 9]]
df = pd.DataFrame(list)
print(df)
print(df.loc[0, 1])
print(df[df[1] == 8].index.values)
