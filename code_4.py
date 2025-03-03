import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year, country_code):
    df = pd.read_csv(big_mac_file)
    filtered = df[(df['date'].str.startswith(str(year))) & (df['iso_a3'] == country_code.upper())]
    return round(filtered['dollar_price'].mean(), 2) if not filtered.empty else None

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    filtered = df[df['iso_a3'] == country_code.upper()]
    return round(filtered['dollar_price'].mean(), 2) if not filtered.empty else None

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered = df[df['date'].str.startswith(str(year))]
    if filtered.empty:
        return None
    cheapest = filtered.loc[filtered['dollar_price'].idxmin()]
    return f"{cheapest['name']}({cheapest['iso_a3']}): ${cheapest['dollar_price']:.2f}"

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    filtered = df[df['date'].str.startswith(str(year))]
    if filtered.empty:
        return None
    most_expensive = filtered.loc[filtered['dollar_price'].idxmax()]
    return f"{most_expensive['name']}({most_expensive['iso_a3']}): ${most_expensive['dollar_price']:.2f}"

if __name__ == "__main__":
    print("Big Mac Price by Year (2008, MYS):", get_big_mac_price_by_year(2008, 'MYS'))
    print("Big Mac Price by Country (MYS):", get_big_mac_price_by_country('MYS'))
    print("Cheapest Big Mac Price by Year (2008):", get_the_cheapest_big_mac_price_by_year(2008))
    print("Most Expensive Big Mac Price by Year (2003):", get_the_most_expensive_big_mac_price_by_year(2003))
