import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset_path = 'Module_3\Exercise_Week_1\IMDB-Movie-Data.csv'

data = pd.read_csv(dataset_path)

# Extract data as dataframe
genre = data['Genre']

some_cols = data[['Title', 'Genre', 'Actors', 'Director', 'Rating']]
print(some_cols)

new_df = data.iloc[10:15][['Title', 'Rating', 'Revenue (Millions)']]
print(new_df)

# Data Selection
selected_data = data[((data['Year'] >= 2010 & (data['Year'] <= 2015))
                      & (data['Rating'] < 6.0)
                      & (data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95)))]

print(selected_data)

# Groupby data and sort values
group_by_data = data.groupby('Director')[['Rating']].mean().sort_values(['Rating'], ascending=True).head()
print(group_by_data)
print()

# View missing values
null_data = data.isnull().sum()
print(null_data)

# Dealing with missing values - Deleting missing values
