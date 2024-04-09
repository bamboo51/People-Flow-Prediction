import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


class Data:
    def __init__(self, time:str="min_05", place:str="p040"):
        self.time = time
        self.place = place

    def load(self):
        self.data = pd.read_csv(f"../data/num_file/{self.time}/{self.place}.csv")
        self.data.loc[self.data["count"]==0, "count"] = np.NaN
        # self.data["count"] = self.data["count"].interpolate(method="linear")
        self.data["count"] = self.data["count"].fillna(method="ffill")
        self.data["datetime"] = pd.to_datetime(self.data["datetime"], format="%Y-%m-%d %H:%M:%S")
        print(self.data)
        return self.data

    def normalize(self):
        self.scaler = StandardScaler()
        self.data["count"] = self.scaler.fit_transform(self.data["count"].values.reshape(-1, 1))
        print(self.data)
        return self.data
    
    def truncate(self, time_step:int=10):
        encode_input = []
        decode_input = []
        decode_output = []

        for i in range(len(self.data)-time_step-1):
            encode_input.append(self.data["count"].values[i:i+time_step])
            decode_input.append(self.data["count"].values[i:i+time_step])
            decode_output.append(self.data["count"].values[i+1:i+time_step+1])

        encode_input = np.array(encode_input)
        decode_input = np.array(decode_input)
        decode_output = np.array(decode_output)
        self.encode_input = encode_input.reshape(encode_input.shape[0], encode_input.shape[1], 1)
        self.decode_input = decode_input.reshape(decode_input.shape[0], decode_input.shape[1], 1)
        self.decode_output = decode_output.reshape(decode_output.shape[0], decode_output.shape[1], 1)
        # print(f"encoder_input:{self.encode_input.shape}, decoder_input:{self.decode_input.shape}, decoder_output:{self.decode_output.shape}")

    def split(self, test_size:float=0.2):
        train_size = 1 - test_size
        self.encode_input_train, self.encode_input_test = train_test_split(self.encode_input, train_size=train_size, shuffle=False)
        self.decode_input_train, self.decode_input_test = train_test_split(self.decode_input, train_size=train_size, shuffle=False)
        self.decode_output_train, self.decode_output_test = train_test_split(self.decode_output, train_size=train_size, shuffle=False)
        print(f"train:{self.encode_input_train.shape}, test:{self.encode_input_test.shape}")
        return {"ei_train": self.encode_input_train, "ei_test": self.encode_input_test, 
                "di_train":self.decode_input_train, "di_test": self.decode_input_test, 
                "do_train": self.decode_output_train, "do_test":self.decode_output_test}