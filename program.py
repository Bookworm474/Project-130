import pandas as pd

data = pd.read_csv('stars.csv')
print(data.head())

del data['index']
print(data.head())

data = data.dropna()
data.reset_index(drop=True, inplace=True)

data.to_csv('data.csv')