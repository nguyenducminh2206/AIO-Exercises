import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

dataset_path = 'Module_3\Exercise_Week_4\Housing.csv'
df = pd.read_csv(dataset_path)

categorical_cols = df.select_dtypes(include=['object']).columns.to_list()

ordinal_encoder = OrdinalEncoder()
encoded_categorical_cols = ordinal_encoder.fit_transform(
    df[categorical_cols]
)

encoded_categorical_df = pd.DataFrame(
    encoded_categorical_cols,
    columns=categorical_cols
)

numerical_df = df.drop(categorical_cols, axis=1)
encoded_df = pd.concat(
    [numerical_df, encoded_categorical_df], axis=1
)

normalizer = StandardScaler()
dataset_arr = normalizer.fit_transform(encoded_df)

X, y = dataset_arr[:, 1:], dataset_arr[:, 0]

test_size = 0.3
random_state = 1
is_shuffle = True
X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=test_size,
    random_state=random_state,
    shuffle=is_shuffle
)

regressor_random_forest = RandomForestRegressor(random_state=1)
regressor_random_forest.fit(X_train, y_train)

y_pred_random_forest = regressor_random_forest.predict(X_val)
mse_random_forest = mean_squared_error(y_val, y_pred_random_forest)
print(mse_random_forest)


regressor_adaboost = AdaBoostRegressor(random_state=1)
regressor_adaboost.fit(X_train, y_train)
                       

y_pred_adaboost = regressor_adaboost.predict(X_val)
mse_adaboost = mean_squared_error(y_val, y_pred_adaboost)
print(mse_adaboost)
