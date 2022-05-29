import pandas as pd
data_csv = pd.read_csv('Data.csv',index_col=False)
stor_dir = './by_sport/'
Data_df = pd.DataFrame(data_csv)
Data_df.drop_duplicates(subset=['Name','Age','Sport'],inplace=True)
for sport in Data_df['Sport'].unique():
    filename = f'{sport}.csv'
    dataframe = Data_df[Data_df['Sport'] == sport]
    dataframe.to_csv(stor_dir + filename,index=False)