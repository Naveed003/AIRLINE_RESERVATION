import pandas as pd
import sys

list = [[1, 2, 3], [7, 8, 9]]
df = pd.DataFrame(list)
for i in df.columns:
    print(i)

