import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assignment 3, Part 1: Using the built-in Seaborn dataset mpg, provide a heatmap of the correlation of all
# the numeric columns and provide a pairplot of the same.
mpg = sns. load_dataset('mpg')
# print(mpg.head())
sns.heatmap(mpg.corr(), cmap='coolwarm')
plt.tight_layout()

sns.set_style('whitegrid')
sns.pairplot(mpg, height=1, aspect=2/2)
plt.tight_layout()
plt.show()

# Assignment 3, Part 2: Using the built-in Seaborn dataset diamonds, establish a FacetGrid based on ‘cut’ and ‘color’.
# Eliminate colors ‘D’ and ‘E’ as well as the cut ‘Fair’. Within that grid, plot the scatterplot for ‘price’ vs.
# ‘carat’.
diamonds = sns.load_dataset('diamonds')
# print(diamonds)
diamonds.drop(diamonds.loc[diamonds['color'] == 'D'].index, inplace=True)
diamonds.drop(diamonds.loc[diamonds['color'] == 'E'].index, inplace=True)
diamonds.drop(diamonds.loc[diamonds['cut'] == 'Fair'].index, inplace=True)
# print(diamonds)
diamonds["cut"] = diamonds["cut"].cat.remove_unused_categories()
diamonds["color"] = diamonds["color"].cat.remove_unused_categories()
sns.set_style('darkgrid')
facet = sns.FacetGrid(diamonds, col='cut', row='color',height=2, aspect=2/2)
facet = facet.map(plt.scatter, 'price', 'carat')
plt.show()

# Assignment 3, Part 3: Using the built-in Seaborn dataset car_crashes, prepare plots with a scattergram with the
# linear model for both the total vs. speeding and the total vs. alcohol.
carCrashes = sns.load_dataset('car_crashes')
# print(carCrashes.head())
crashesG1 = sns.regplot(x='total', y='speeding', data=carCrashes).set(title='Total vs. Speeding')
plt.show()
crashesG2 = sns.regplot(x='total', y='alcohol', data=carCrashes).set(title='Total vs. Alcohol')
plt.show()

# Assignment 4, Part 4: Using the built-in Seaborn dataset iris, provide a plot with four subplots wherein the
# distribution of each of the numeric columns is presented as a set of boxplots, one for each ‘species’.
iris = sns.load_dataset('iris')
# print(iris.head())
sns.set(style='darkgrid')
fig, axes = plt.subplots(2, 2, figsize=(8,10),num=1)

ax = sns.boxplot(x="species", y="sepal_length", data=iris, orient='v', ax=axes[0,0])
ax = sns.boxplot(x="species", y="sepal_width", data=iris, orient='v', ax=axes[0,1])
ax = sns.boxplot(x="species", y="petal_length", data=iris, orient='v', ax=axes[1,0])
ax = sns.boxplot(x="species", y="petal_width", data=iris, orient='v', ax=axes[1,1])
plt.show()
