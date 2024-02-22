import pandas as pd

# list_teams =['49ers','KC','Cowboys','Steelers']

# print(type(list_teams))

# print(list_teams)

# series_teams = pd.Series(list_teams)

# print(series_teams)
# print(type(series_teams))
# print(series_teams.index)


# students = {'Hawai':'Isabella','Ohio':'David','Iowa':'Justin','Colorado':'Robert'}
# print(type(students))
# print(students)

# student_series = pd.Series(index=students.keys(),data=students.values())

# print(type(student_series))
# print(student_series)
# print(student_series.index)

df = pd.read_csv('big-mac-full-index.csv')

# print(type(df))
# print(df.columns)
# print(type(df.columns))

# print(df['iso_a3'])

# print(type(df['iso_a3']))

# print(df)

country_code = 'ARG'
query_text = f"iso_a3 == @country_code"

df_arg = df.query(query_text)

# print(round(df_arg['local_price'].mean(),2))
# print(df_arg['dollar_price'].min())
# print(df_arg['dollar_price'].max())

idx_dollar_price = df_arg['dollar_price'].idxmax()

print(idx_dollar_price)

arg_series = df_arg.loc[1184]
print(arg_series)
print(type(arg_series))
# print(arg_series)
# print(df_arg['local_price'].median())
