import pandas as pd
import datetime
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
#Load   Data
df_data = pd.read_csv('/content/part-00000-363d1ba3-8ab5-4f96-bc25-4d5862db7cb9-c000.csv.zip', parse_dates= True, low_memory = False)
# For example, to remove all rows after the 100th row (index 99)
cutoff_index = 500
df_clean_data = df_data[:cutoff_index]
#Selecting Needed Columns
df1_clean_data = df_clean_data[['label',
                                                   'Protocol Type' ,
                                                  'Duration' ,
                                                   'Rate',
                                                   'Tot sum',
                                                   'Min',
                                                   'Max',
                                                   'AVG',
                                                   'Std',
                                                   'Tot size',
                                                   'IAT',
                                                   'Radius'
                                                   ]]

df1_clean_data.to_csv(r"Cleansed_Data.csv",index=False)
