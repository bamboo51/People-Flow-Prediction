import pandas as pd
import os

directory = './min_01/'

for filename in sorted(os.listdir(directory)):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)

        df = pd.read_csv(file_path)
        
        df['datetime'] = pd.to_datetime(df['datetime'])
        df.set_index('datetime', inplace=True)
        result = df.resample('30min').sum()
        print(result)
        
        output_filename = os.path.splitext(filename)[0]
        print(output_filename)
        output_path = os.path.join('./min_30/', output_filename+'.csv')
        result.to_csv(output_path)
        