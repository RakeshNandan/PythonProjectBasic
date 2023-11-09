import pandas as pd
import csv
import numpy as np

# with open('./covid_19_india.csv', mode ='r')as file:
#     csvFile = csv.reader(file)
#
# csvFile


data = pd.read_csv('data/covid_19_india.csv')
print(data)
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
print(data['Date'])
print(data.dtypes)