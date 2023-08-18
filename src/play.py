import pandas as pd
from bokeh.io import show
from bokeh.layouts import column, row
from bokeh.models import CheckboxGroup, Checkbox, RadioGroup, Div, ColumnDataSource

smartPhonesDF = pd.read_csv('../smartphones.csv')

#select the rows where the price is lower than 1000
smartPhonesDFFilterPrice = smartPhonesDF[smartPhonesDF['price'] < 10000]
#show the first 10

"""
print(smartPhonesDFFilterPrice.head(10))
print("n price", smartPhonesDF['price'].shape[0])
print("n screen_size",smartPhonesDF['screen_size'].shape[0])
print("n fast_charging_available",smartPhonesDF['fast_charging_available'].shape[0])
print("n avg_rating",smartPhonesDF['avg_rating'].shape[0])
print("some screen sizes", smartPhonesDF['screen_size'].unique()[:10])
print("some available_charging values", smartPhonesDF['fast_charging_available'].head(10))
print("some primary rear cameras", smartPhonesDF['primary_camera_rear'].head(10))
print("some primary front cameras", smartPhonesDF['primary_camera_front'].head(10))
"""


#show the maximum rating
#rint("max rating\n", smartPhonesDF['avg_rating'].max())

#show the minimum rating
#print("min rating\n", smartPhonesDF['avg_rating'].min())

#make 2 dataframes the first dataframe for all rows where the rating is less than 8 and another where the rating is greater than 8
smartPhonesDFFilterRating = smartPhonesDF[smartPhonesDF['avg_rating'] < 8]
smartPhonesDFFilterRating2 = smartPhonesDF[smartPhonesDF['avg_rating'] > 8]

# Create a ColumnDataSource for the data
sourceFigure2D = ColumnDataSource(data=dict(
    x=smartPhonesDF['battery_capacity'],
    y=smartPhonesDF['price'],
    model=smartPhonesDF['model'],
    brand=smartPhonesDF['brand_name'],
    rating=smartPhonesDF['avg_rating']
))


question = Div(text="Do you want to opt-in?")
radio_group = RadioGroup(labels=["Yes", "No", "Any"], active=0)
layout = row(question, radio_group)
#show(layout)

#get ther rating of Doogee V Max
#print("rating of Doogee V Max", smartPhonesDF.loc[smartPhonesDF['model'] == 'Doogee V Max', 'avg_rating'].values[0])
#get the rating of Apple iPhone SE 2020
#print("rating of Apple iPhone SE 2020", smartPhonesDF.loc[smartPhonesDF['model'] == 'Apple iPhone SE 2020', 'avg_rating'].values[0])


# Sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# List of values to filter
filter_values = [2, 4, 6]

# Filtered dictionary using filter() and lambda function
filtered_dict = dict(filter(lambda item: item[1] in filter_values, my_dict.items()))
print(filtered_dict)