import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')
year = 2020

query_text = f"date.str.startswith(@year)"

print(query_text)