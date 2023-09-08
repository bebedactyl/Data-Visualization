import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import yfinance as yf

# Assignment 2, Part 1: Create a list of the atomic weights of the first six elements of the periodic table, each
# rounded to the nearest integer. Provide two pie charts as follows: (1) each slice annotated with a percentage of the
# whole and (2) each slice annotated with its atomic weight. Explode a different element with each chart.

dataDict = {'Element': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon'],
            'Symbol': ['H', 'He', 'Li', 'Be', 'B', 'C'],
            'Atomic Weight (u)': [1.0078, 4.0026, 6.9410, 9.0122, 10.811,12.011]}
# print(dataDict)

df = pd.DataFrame(dataDict)
df['Atomic (Round)'] = df['Atomic Weight (u)'].round(decimals = 0)
df["Atomic (Round)"] = df["Atomic (Round)"].astype(float).astype(int)
# print(df)

explode=(0,0,0.1,0,0,0)
explode2=(0,0,0,0,0,0.1)

figure1,axes=plt.subplots(1,2,figsize=(10,4),num=1)
axes[0].pie(df["Atomic (Round)"], labels = df["Element"], explode=explode, autopct='%1.0f%%')
axes[1].pie(df["Atomic (Round)"], labels = df["Element"], explode=explode2,
            autopct=lambda p: '{:.0f}'.format(p * sum(df['Atomic (Round)']) / 100.0))
plt.show()


# Assignment 2, Part 2: Read into a DataFrame the file py_ide2.csv, and provide both a horizontal bar chart and
# a vertical bar chart, complete with all labels. Be sure to rotate the IDE names so that they are readable.

df2 = pd.read_csv('py_ide2_csv_2.txt')
# print(df2)

fig, ax = plt.subplots(1, 2, figsize=(8, 4), num=2)
ax[0].barh(df2['IDE'], df2['Adoption'])
ax[0].set_xlabel('Adoption')
ax[0].set_ylabel('IDE')
ax[0].set_title('IDE Adoption')
plt.xticks(range(len(df2)), df2['IDE'],rotation=90)
ax[1].bar(df2['IDE'], df2['Adoption'])
ax[1].set_xlabel('IDE')
ax[1].set_ylabel('Adoption')
ax[1].set_title('IDE Adoption')
plt.tight_layout()
plt.show()

# Assignment 2, Part 3: Construct a list of eight strings that represent days evenly spread out. Drawing from the
# random uniform distribution, make an array of eight floats ranging from 100 to 200 in value. Establish a DataFrame
# from that list and that array, convert the dates to pandas datetime objects, and set them to the index. Make two
# charts in the same window or canvas as follows: (1) a line plot of the values vs. dates and (2) a bar chart of
# the same.

listOfDays = ['2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01']
np.random.seed(12345)
array = np.random.uniform(100,201,8)
# print(array)

arrayDict = dict(zip(["Date", "Value"], [listOfDays, array]))
df3 = pd.DataFrame(arrayDict)
df3['Date'] = pd.to_datetime(df3['Date']).dt.date
df3.set_index("Date", inplace=True)
# print(df3)

fig, ax = plt.subplots(1, 2, figsize=(14, 5), num=3)
ax[0].plot(df3['Value'])
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Value')
ax[0].set_title('Value per Day')
ax[1].bar(x=df3.index, height=df3['Value'], width=10)
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Value')
ax[1].set_title('Value per Day')
plt.tight_layout()
plt.show()

# Assignment 2, Part 4: Pull from Yahoo! Finance the closing prices and volumes of the stock of your choice over the
# trading days of one month, and plot the prices and volumes on a canvas in two separate panels, one above the other,
# with the dates aligned.

df4 = yf.download('AAPL', '2019-01-01', '2019-01-31')
# print(df4.head(20))

fig = plt.figure(figsize=(10, 6), num=4)
ax1 = fig.add_axes([0.1, 0.50, 0.85, 0.45])
ax2 = fig.add_axes([0.1, 0.25, 0.85, 0.15])
ax1.plot(df4.index, df4['Open'], 'r', label='Open')
ax1.plot(df4.index, df4['Close'], 'g', label='Close')
ax1.plot(df4.index, df4['High'], 'b', label='High')
ax1.plot(df4.index, df4['Low'], 'y', label='Low')
ax1.legend(loc=0)
ax1.set_title('AAPL Stock Prices and Volumes Jan 2019')
ax1.set_ylabel('Prices')
ax2.plot(df4.index, df4['Volume'])
ax2.set_xlabel('Date')
ax2.set_ylabel('Volume')
plt.tight_layout()
plt.show()
