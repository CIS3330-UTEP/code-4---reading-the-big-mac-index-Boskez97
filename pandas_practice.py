import pandas as pd

df = pd.read_csv('big_mac_full_index')
country = 'Brazil'
query_text = f'name == "{country}" '

df_query = df.query(query_text)

print(df_query)