import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = '../data/num_file/hrs_1/p040.csv'
people_num = pd.read_csv(path, encoding='utf-8')

# merge "date" and "hour" columns to be datetime
people_num['datetime'] = pd.to_datetime(people_num['date'])+pd.to_timedelta(people_num['hour'], unit='h')
people_num = people_num.drop(['date', 'hour'], axis=1)
people_num.set_index('datetime', inplace=True)
people_num.columns = ['amount']
people_num['amount'] = people_num['amount'].astype(float)

# resample the data
full_index = pd.date_range(start=people_num.index.min(), end=people_num.index.max(), freq='h')
people_num = people_num.reindex(full_index)
people_num['amount'] = people_num['amount'].bfill()
print(people_num)