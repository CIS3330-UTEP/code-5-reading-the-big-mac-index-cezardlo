import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year, country_code):
#The function receives the year and the country_code in lowercase
# we are
    filter =df[(df['date'].str)] and (df['iso_a3']== country_code)
#The function should return the mean value in the specific year
# of the big mac in dollars ('dollar_pice' column)
#The value must be rounded to 2 decimal numbers
    return round(filter['dollar_price'].mean(),2)
# help me return nothing if I have an empty in pandas

# I used Gen Ai to find out how to put in the code to return country code and filtered mean.
def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)# Ai Df error so i needed to recall df
    filtered = df[df['iso_a3'] == country_code.upper()]
    return round(filtered['dollar_price'].mean(), 2)
# Ai mentor walked me on the filtered isoA3 code I tend to confuse = and ==
def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered = df[df['date'].str.startswith(str(year))]
    if filtered.empty:
        return None
    cheapest = filtered.loc[filtered['dollar_price'].idxmin()]
    return f"{cheapest['name']}({cheapest['iso_a3']}): {cheapest['dollar_price']:.2f}"
# I asked AI to walk me through idxmin funtion
def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered = df[df['date'].str.startswith(str(year))]
    most_expensive = filtered.loc[filtered['dollar_price'].idxmax()]
    return f"{most_expensive['name']}({most_expensive['iso_a3']}):{most_expensive['dollar_price']:.2f}"

if __name__ == "__main__":
    print(get_big_mac_price_by_country('mex'))  # Output should be a number like 2.45
    print("Big Mac Price by Country (MYS):", get_big_mac_price_by_country('MYS'))
    print("Cheapest Big Mac Price by Year (2008):", get_the_cheapest_big_mac_price_by_year(2008))
    print("Most Expensive Big Mac Price by Year (2003):", get_the_most_expensive_big_mac_price_by_year(2003))
