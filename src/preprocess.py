import matplotlib.pyplot as plt
from utils import *

wine_dataset = pd.read_csv('winequality-red.csv')

print(wine_dataset.shape)
print(wine_dataset.head())
print(wine_dataset.isnull().sum())

# Statistical measures
print(wine_dataset.describe())

# Number of values for each quality
sns.catplot(x='quality', data=wine_dataset, kind='count')
plt.show()

# Volatile acidity vs Quality
plt.figure(figsize=(5,5))
sns.barplot(x='quality', y='volatile acidity', data=wine_dataset)
plt.show()

# Citric acid vs Quality
plt.figure(figsize=(5,5))
sns.barplot(x='quality', y='citric acid', data=wine_dataset)
plt.show()

# Correlation heatmap
correlation = wine_dataset.corr()

plt.figure(figsize=(10,10))
sns.heatmap(
    correlation,
    cbar=True,
    square=True,
    fmt='.1f',
    annot=True,
    annot_kws={'size':8},
    cmap='Blues'
)
plt.show()

# Data preprocessing
X = wine_dataset.drop('quality', axis=1)
Y = wine_dataset['quality'].apply(
    lambda y_value: 1 if y_value >= 7 else 0
)

print(X)
print(Y)