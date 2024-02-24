import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    # country_code = ['iso_a3']
    # country_codes = ['ARG' 'AUS' 'BRA' 'CAN' 'CHE' 'CHL' 'CHN' 'CZE' 'DNK' 'EUZ' 'GBR' 'HKG' 'HUN' 'IDN' 'ISR' 'JPN' 
    # 'KOR' 'MEX' 'MYS' 'NZL' 'POL' 'RUS' 'SGP' 'SWE' 'THA' 'TWN' 'USA' 'ZAF' 'PHL' 'NOR' 'PER' 'TUR' 'VEN' 'EGY' 'COL' 'CRI'
    # 'LKA' 'PAK' 'SAU' 'UKR' 'URY' 'ARE' 'IND' 'VNM' 'AZE' 'BHR' 'GTM' 'HND' 'HRV' 'JOR' 'KWT' 'LBN' 'MDA' 'NIC' 'OMN' 'QAT' 'ROU']
    query_df = df[(df['iso_a3'].str.lower() == country_code.lower()) & df['date'].str.startswith(str(year))]
    mean_price = query_df['dollar_price'].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    # query = f"iso_a3 == @country_code'"
    # result = df.query(query)
    query_df = df[df['iso_a3'].str.lower() == country_code]
    mean_price = query_df['dollar_price'].mean()
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    cheapest = df[df['date'].str.startswith(str(year))]['dollar_price'].idxmin()
    cheapest_mac = df.iloc[cheapest]
    return f"{cheapest_mac['name']}({cheapest_mac['iso_a3']}): ${cheapest_mac['dollar_price']}"

def get_the_most_expensive_big_mac_price_by_year(year):
    expensive = df[df['date'].str.startswith(str(year))]['dollar_price'].idxmax()
    expensive_mac = df.iloc[expensive]
    return f"{expensive_mac['name']}({expensive_mac['iso_a3']}): ${expensive_mac['dollar_price']}"

if __name__ == "__main__":
    BMPBY = get_big_mac_price_by_year(2002, 'mex')
    print(BMPBY)
    BMPBC = get_big_mac_price_by_country("che")
    print(BMPBC)
    CHBM = get_the_cheapest_big_mac_price_by_year(2017)
    print(CHBM)
    MEBM = get_the_most_expensive_big_mac_price_by_year(2007)
    print(MEBM)