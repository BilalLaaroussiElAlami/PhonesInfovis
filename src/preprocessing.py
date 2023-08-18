import pandas as pd

smartphonesDF = pd.read_csv('smartphones.csv')
pd.set_option('display.max_columns', None)
smartphonesDF.fillna(0, inplace=True)  # just replace missing values with zero
smartphonesDF['price'] = smartphonesDF['price'] / 100     #convert from cents to dollars

numerical_columns   = smartphonesDF.select_dtypes(include=['int64', 'float64', 'int32', 'float32', 'int', 'float', 'number']).columns
categorical_columns = smartphonesDF.select_dtypes(include=['object']).columns

#get the maximum and minimum values for each numerical column
numerical_columns_max_min = {col: (smartphonesDF[col].max(), smartphonesDF[col].min()) for col in numerical_columns}
for col, max_min in numerical_columns_max_min.items():
    print(f"{col}: {max_min[0]}")
def getMaxValue(col):
    return numerical_columns_max_min[col][0]
def getMinValue(col):
    return numerical_columns_max_min[col][1]
print(' max price: ', getMaxValue('price'))


#get a map where the keys are the categorical columns  excluding the models and the values are the unique values of each categorical column
categorical_columns_unique_values = {col: smartphonesDF[col].unique() for col in categorical_columns if col != 'model'}
for col, unique_values in categorical_columns_unique_values.items():
    print(f"{col}: {unique_values}")

assert(smartphonesDF.columns.shape[0] == numerical_columns.shape[0] + categorical_columns.shape[0]) #make sure no columns have been missed

