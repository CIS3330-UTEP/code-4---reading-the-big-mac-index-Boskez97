import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query_text = f"date.str.startswith(@year) and 'iso_a3 == @country_code'"
    result = df.query(query_text)
    mean_price = result['dollar_price'].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    query = f"iso_a3 == @country_code'"
    result = df.query(query)
    mean_price = result['dollar_price'].mean()
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    cheapest = df[df['date'].str.startswith(str(year))]['dollar_price'].idxmin()
    cheapest_mac = df.iloc[cheapest]
    return f"{cheapest_mac['name']}({cheapest_mac['iso_a3']}): ${cheapest_mac['dollar_price']}"

def get_the_most_expensive_big_mac_price_by_year(year):
    expensive = df[df['date'].str.startswith(str(year))]['dollar_price'].idxmax()
    expensive_mac = df.iloc[0]
    return f"{expensive_mac['mac']}({expensive_mac['iso_a3']}): ${expensive_mac['dollar_price']}"

if __name__ == "__main__":
    function_1 = get_big_mac_price_by_year[2007,"MEX"]
    print(function_1)
    function_2 = get_big_mac_price_by_country("USA")
    print(function_2)
    function_3 = get_the_cheapest_big_mac_price_by_year(2016)
    print(function_3)
    function_4 = get_the_most_expensive_big_mac_price_by_year(2007)
    print(function_4)