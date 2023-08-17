import pandas as pd

# Sample DataFrame
data = {
    'brand': ['Apple', 'Samsung', 'Apple', 'Samsung', 'Apple'],
    'model': ['iPhone X', 'Galaxy S10', 'iPhone 11', 'Galaxy S20', 'iPhone 12'],
    'price': [1000, 900, 1100, 1000, 1200],
    'internal_memory': [64, 128, 64, 256, 128],
    'average_rating': [4.5, 4.2, 4.7, 4.4, 4.9]
}

df = pd.DataFrame(data)

print(df)
print()

# Select numerical columns only
numerical_columns = df.select_dtypes(include=['number'])

# Group by 'brand' and calculate the averages for numerical columns
averages_df = numerical_columns.groupby(df['brand']).mean().reset_index()

print(averages_df)

# maka a dataframe from the csv file
smartphones_brand_averages_df = pd.read_csv('smartphones.csv')

numerical_columns = smartphones_brand_averages_df.select_dtypes(include=['number'])
# Group by 'brand' and calculate the averages for numerical columns
smartphones_brand_averages_df = numerical_columns.groupby(smartphones_brand_averages_df['brand_name']).mean().reset_index()

print(smartphones_brand_averages_df)
