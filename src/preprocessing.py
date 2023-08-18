import pandas as pd

df = pd.read_csv('smartphones.csv')
pd.set_option('display.max_columns', None)
df.fillna(0, inplace=True)  # just replace missing values with zero
df['price'] = df['price']/100     #convert from cents to dollars

numerical_columns   = df.select_dtypes(include=['int64', 'float64', 'int32', 'float32', 'int', 'float', 'number']).columns
categorical_columns = df.select_dtypes(include=['object']).columns

#get a map where the keys are the categorical columns  excluding the models and the values are the unique values of each categorical column
categorical_columns_unique_values = {col: df[col].unique() for col in categorical_columns if col != 'model'}
for col, unique_values in categorical_columns_unique_values.items():
    print(f"{col}: {unique_values}")

assert(df.columns.shape[0] == numerical_columns.shape[0] + categorical_columns.shape[0]) #make sure no columns have been missed

