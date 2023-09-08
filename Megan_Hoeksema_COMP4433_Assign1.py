# Assignment 1, Part 1: Construct a CSV file with the first eight elements of the periodic table.
# Include columns for name, symbol, and atomic number. Read that into a pandas DataFrame. Inside the program,
# add a ninth and 10th element, and then add a column with the atomic weights rounded to the nearest integer

import pandas as pd
import numpy as np
import csv

header = ['Name', 'Symbol', 'Atomic number (u)']
elems = [['Hydrogen', 'H', 1.0078], ['Helium', 'He', 4.0026], ['Lithium', 'Li', 6.9410],
         ['Beryllium', 'Be', 9.0122], ['Boron', 'B', 10.811], ['Carbon', 'C', 12.011],
         ['Nitrogen', 'N', 14.007], ['Oxygen', 'O', 15.999]]

with open('elements.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(elems)

df = pd.read_csv('elements.csv')
print('Original DataFrame')
print(df)

df.loc[len(df.index)] = ['Fluorine', 'F', 18.998]
df.loc[len(df.index)] = ['Neon', 'Ne', 20.180]
print('\n New Data Frame')
print(df)


df['Atomic (Round)'] = df['Atomic number (u)'].apply(np.ceil)
df["Atomic (Round)"] = df["Atomic (Round)"].astype(float).astype(int)
print('\n New Data Frame with a New Column')
print(df)


# Assignment 1, Part 2: Make a list of strings for nine Greek letters, for example ‘alpha’. Make that list such that
# the strings are not in alphabetic order. Make two 9-element numpy arrays of random floating-point numbers with an
# estimated mean of 10 and a standard deviation of 1.5. Make another array of nine elements ranging from zero to two
# times pi. Name it ‘angle’. Make another array holding the cosine of that ‘angle’ array. Construct a dictionary from
# all of the above. Form a DataFrame from that dictionary, and print it out. Sort the DataFrame ascending on the Greek
# letters, drop two columns of your choice, drop one of the rows, and print that out.

import numpy as np
import pandas as pd

greekLetters =['Omicron', 'Phi', 'Beta', 'Theta', 'Xi', 'Epsilon', 'Omega', 'Tau', 'Lambda']
np.random.seed(123456)

my_std = 1.5
my_mean = 10
array2 = my_std * np.random.randn(9) + my_mean
array3 = my_std * np.random.randn(9) + my_mean
angle = np.linspace(0, 2 * np.pi, 9)
cosAngle = np.cos(angle)
arrayDict = dict(zip(["greekLetters", "array2", "array3", "angle", "cosAngle"],
                     [greekLetters, array2, array3, angle, cosAngle]))

df = pd.DataFrame(arrayDict)

# print('List of Greek Letters')
# print(greekLetters)
# print('\n Array 2')
# print(array2)
# print('\n Array 3')
# print(array3)
# print('\n Angle Array')
# print(angle)
# print('\n Cosine of Angle Array')
# print(cosAngle)
# print('\n Dictionary of all Arrays')

# print(arrayDict)

print(df)
df.sort_values(by=['greekLetters'], inplace=True)
df = df.drop(df.columns[[1, 2]], axis=1)
df = df.drop(7)

print('\n Dataframe after sorting, dropping two columns, removing 1 row')
print(df)


# Assignment 1, Part 3: Write a program in Python to create and print out the first 12 Fibonacci numbers. Then
# iterate over the last five numbers to build another list with the ratio of each number to its predecessor. What
# do you observe about this latter list?
import numpy as np

def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

listOfFib = [fibonacci(n) for n in range(12)]
print(listOfFib)

differences = np.diff(listOfFib)
print(differences)

#You will notice that the difference between two numbers in a Fibonacci sequence is equal to the previous value in the
# Fibonacci sequence. For example, the 11th number in the sequence is 55. The difference between the 11th number and
# the 12th number (|55 - 89|) is equal to the value in the 10th position (34). You will notice that the difference
# between two numbers in a Fibonacci sequence is equal to the previous value in the Fibonacci sequence. For example,
# the 11th number in the sequence is 55. The difference between the 11th number and the 12th number (|55 - 89|) is
# equal to the value in the 10th position (34).


# Assignment 1, Part 4: Provide a function that converts temperature in Kelvin to Rankine. Make a list of five Kelvin
# temperatures, and print out their values in Rankine. Repeat using a lambda function.

import numpy as np
from scipy.constants import convert_temperature

def kelvinToRankine(list):
    return convert_temperature(np.array(list), 'Kelvin', 'Rankine')

print(kelvinToRankine([-10.5, 50.125, 100.25, 250.5, 325.75]))