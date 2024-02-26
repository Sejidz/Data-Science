sales_11 = pd.read_csv(
    'assignment1 data/sales_202111.csv'
)
sales_12 = pd.read_csv(
    'assignment1 data/sales_202112.csv'
)

# Change the name of the column
sales_11.rename(columns={'Order Number': 'Description'}, inplace=True)

# Write the changes back to the CSV file
sales_11.to_csv('your_file.csv', index=False)
