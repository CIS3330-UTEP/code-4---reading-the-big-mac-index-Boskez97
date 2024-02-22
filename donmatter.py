import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    return 

def get_big_mac_price_by_country(country_code):
    return 

def get_the_cheapest_big_mac_price_by_year(year):

    return 

def get_the_most_expensive_big_mac_price_by_year(year):
    return 
if __name__ == "__main__":
    function_1 = get_big_mac_price_by_year[2007,"MEX"]
    print(function_1)
    function_2 = get_big_mac_price_by_country("USA")
    print(function_2)
    function_3 = get_the_cheapest_big_mac_price_by_year(2016)
    print(function_3)
    function_4 = get_the_most_expensive_big_mac_price_by_year(2007)
    print(function_4)