import pandas as pd
import csv
import json

countries_csv = pd.read_csv('countries.csv',index_col=False)
data_csv = pd.read_csv('Data.csv',index_col=False)
stor_dir = './by_country/'
countries_df = pd.DataFrame(countries_csv)
Data_df = pd.DataFrame(data_csv)

for index, row in countries_df.iterrows():
    NOC = row['NOC']
    Country = str(row['Country'])
    filename = f'{Country}.csv'
    dataframe = Data_df[Data_df['NOC'] == NOC]
    dataframe.to_csv(stor_dir + filename,index=False)