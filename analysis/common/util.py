import pandas as pd
import numpy as np

# Class for standardize data
class Standardize:
    def __init__(self, split=0.15):
        self.split = split

    def _transform(self, df):
        return (df-self.mu)/self.sigma
    
    def split_data(self, df, test_split=0.15):
        n = int(len(df)*test_split)
        train, test = df[:-n], df[-n:]
        return train, test
    
    def fit_transform(self, train, test):
        self.mu = train.mean()
        self.sigma = train.std()
        train_s = self._transform(train)
        test_s = self._transform(test)
        return train_s, test_s
    
    def transform(self, df):
        return self._transform(df)
    
    def inverse(self, df):
        return (df*self.sigma)+self.mu
    
    def inverse_y(self, df):
        return (df*self.sigma[0])+self.mu[0]
    
# Method for one-step forecast
def one_step_forecast(df, window):
    d = df.values
    x = []
    n = len(df)

    idx = df.index[:-window]
    for start in range(n-window):
        end = start+window
        x.append(d[start:end])
    
    cols = [f'x_{i}' for i in range(1, window+1)]
    x = np.array(x).reshape(n-window, -1)
    y = df.iloc[window:].values
    df_xs = pd.DataFrame(x, columns=cols, index=idx)
    df_y = pd.DataFrame(y.reshape(-1), columns=['y'], index=idx)

    return pd.concat([df_y, df_xs], axis=1).dropna()


# Split train and test data
def split_data(df, test_split=0.15):
    n = int(len(df)*test_split)
    train, test = df[:-n], df[-n:]
    return train, test

# Method for multi-step forecast
def multi_step_forecast(data, model, steps=10):
    forecast = []
    for i in range(steps):
        one_step_pred = model.predict(np.array(data).reshape(1, -1))[0]
        forecast.append(one_step_pred)
        _ = data.pop(0)
        data.append(one_step_pred)

    return np.array(forecast)

# Handle loss data
def handle_missing_data(df):
    n = int(df.isna().sum())
    # n = int(ser.iloc[0])
    if n>0:
        print(f'found {n} missing observations ...')
        df.ffill(inplace=True)

# Evaluate
def evaluate(df, train, sort_by='MASE'):
    evals = pd.DataFrame(index=['sMAPE', 'MAPE', 'RMSE'])
    y_truth = df['y']
    y_predicted = df.drop(columns=['y'])
    '''
    for p in y_predicted:
        evals.loc['sMAPE', p] = mape(y_truth, y_predicted[p], symmetric=True)
        evals.loc['MAPE', p] = mape(y_truth, y_predicted[p], symmetric=False)
        evals.loc['RMSE', p] = np.sqrt(mse(y_truth, y_predicted[p]))
        evals.loc['MASE', p] = mase(y_truth, y_predicted[p], y_train=train)
    '''
    return evals.T.sort_values(by=sort_by)
    