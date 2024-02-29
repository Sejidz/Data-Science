import pandas as pd  # noqa
import numpy as np  # noqa

# Prepare the datamode/
sales_06 = pd.read_csv(
    'assignment1 data/sales_202106.csv'
)
sales_07 = pd.read_csv(
    'assignment1 data/sales_202107.csv'
)
sales_08 = pd.read_csv(
    'assignment1 data/sales_202108.csv'
)
sales_09 = pd.read_csv(
    'assignment1 data/sales_202109.csv'
)
sales_10 = pd.read_csv(
    'assignment1 data/sales_202110.csv'
)
# Combine the data into a single DataFrame
combined_sales = pd.concat([sales_06, sales_07, sales_08, sales_09, sales_10])

# Write the changes back to the CSV file
combined_sales.to_csv('combined_sales.csv', index=False)



# Specify the columns you want to include
columns_to_include = ['Transaction Date', 'Transaction Type', 'Product id', 'Sku Id', 'Buyer Country', 'Buyer Postal Code', 'Amount (Merchant Currency)']

# Read the CSV file and include only specified columns
combined_sales_cleaned = pd.read_csv('combined_sales.csv', usecols=columns_to_include)
combined_sales_cleaned.to_csv('combined_sales_cleaned.csv', index=False)

filtered_df = combined_sales_cleaned[combined_sales_cleaned['Product id'].str.contains("com.vansteinengroentjes.apps.ddfive")]
filtered = filtered_df[~filtered_df['Transaction Type'].isin(['Charge refund', 'Google fee refund', 'Tax refund', 'Tax'])]
filtered.to_csv('filtered.csv', index=False)




#Start with cleaning last two months
sales_11 = pd.read_csv(
    'assignment1 data/sales_202111.csv'
)
sales_12 = pd.read_csv(
    'assignment1 data/sales_202112.csv'
)
# Combine the data into a single DataFrame
combined_sales_last_df = pd.concat([sales_11, sales_12])




new_column_names = {'Order Charged Date': 'Transaction Date', 'Financial Status': 'Transaction Type', 'Product ID': 'Product id', 'SKU ID': 'Sku Id', 'Country of Buyer': 'Buyer Country', 'Postal Code of Buyer': 'Buyer Postal Code', 'Charged Amount': 'Amount (Buyer Currency)'}

# Rename columns
combined_sales_last_df.rename(columns=new_column_names, inplace=True)
combined_sales_last = combined_sales_last_df[~combined_sales_last_df['Transaction Type'].isin(['Refund'])]
combined_sales_last = combined_sales_last[~combined_sales_last['Currency of Sale'].isin(['COP', 'CRC', 'NZD'])]
combined_sales_last = combined_sales_last[combined_sales_last['Product id'].str.contains("com.vansteinengroentjes.apps.ddfive")]






exchange_rates = pd.read_csv('combined_sales.csv', usecols=['Buyer Currency', 'Currency Conversion Rate'])
exchange_rates_kort = exchange_rates[exchange_rates['Buyer Currency'].duplicated() == False]
exchange_rates_kort.to_csv('exchange_rates_kort.csv', index=False)




data_dict = {}
# Iterate over the data and add it to the dictionary
for ind in exchange_rates_kort.index:
    key, value = exchange_rates_kort['Buyer Currency'][ind], exchange_rates_kort['Currency Conversion Rate'][ind]
    data_dict[key] = value



step = 1
for index, row in combined_sales_last.iterrows():
    step += 1
    price = 0
    price = row["Amount (Buyer Currency)"]
    if type(price) == str:
        price = price.replace(',', '')
    price = float(price)
    currency = row['Currency of Sale']
    print (currency, price, data_dict[currency])
    price = price * data_dict[currency]
    print (price)

    combined_sales_last.at[step,'Amount (Merchant Currency)'] = price 

#combined_sales_last.rename(columns=new_column_names, inplace=True)

combined_sales_last.to_csv('combined_sales_last.csv', index=False)