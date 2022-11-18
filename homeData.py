import pandas as pd
from sklearn.tree import DecisionTreeRegressor

file_path = "home-data-for-ml-course/train.csv"
home_data = pd.read_csv(file_path)

y = home_data['SalePrice']

home_features = ['TotRmsAbvGrd', 'GarageCars', 'LotArea', 'Utilities', 'LotFrontage']
x = home_data[home_features]
print(y.describe())