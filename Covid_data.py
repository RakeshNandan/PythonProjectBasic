import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import numpy as np

def data_cleaning(data):
    data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
    data['State/UnionTerritory'] = data['State/UnionTerritory'].sort_values(ascending=True)
    data['State/UnionTerritory'].unique()
    # data['Date/Time'] = data['Date'] + data['Time']
    # print(data['Date/Time'])
    data.drop('Time', axis=1, inplace=True)
    print(data)
    
def data_representation(data):
    plt.scatter(data['State/UnionTerritory'], data['ConfirmedIndianNational'])
    plt.xlabel('states')
    plt.ylabel('india count')
    plt.show()
    


# data cleaning

# print(data)
# data.info()
# print(data['Date'])
# print(data['State/UnionTerritory'])
# # print(data.dtypes)
# # print(data)

#plots and graph representation



