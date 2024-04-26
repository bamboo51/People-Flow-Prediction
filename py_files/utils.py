import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

plt.rcParams['figure.figsize'] = (12, 8)
plt.rc('font', size=16)                    
plt.rc('axes', titlesize=16)               
plt.rc('axes', labelsize=16)              
plt.rc('xtick', labelsize=16)              
plt.rc('ytick', labelsize=16)              
plt.rc('legend', fontsize=16)             
plt.rc('figure', titlesize=16)

def one_step_forecast(df, window):
    d = df.values
    x = []
    n = len(df)
    idx = df.index[:-window]
    for start in range(n-window):
        end = start + window
        x.append(d[start:end])
    cols = [f'x_{i}' for i in range(1, window+1)]
    x = np.array(x).reshape(n-window, -1)
    y = df.iloc[window:].values
    df_xs = pd.DataFrame(x, columns=cols, index=idx)
    df_y = pd.DataFrame(y.reshape(-1), columns=['y'], index=idx)
    return pd.concat([df_xs, df_y], axis=1).dropna()

def plot_forecast(y_test, predict, index, history, eval_hist, file_name, window_size):
    fig, ax = plt.subplots(2, 1)
    (pd.Series(history.history['loss']).plot(style='k',alpha=0.50, title=f'Loss by Epoch@window size={window_size}', ax = ax[0], label='loss'))
    (pd.Series(history.history['val_loss']).plot(style='k',ax=ax[0],label='val_loss'))
    ax[0].legend()
    (pd.Series(y_test, index=index)).plot(style='k--', alpha=0.5, ax=ax[1], title=f'Forecast vs Actual@window size={window_size}', label='actual')
    (pd.Series(predict, index=index)).plot(style='k',label='Forecast', ax=ax[1])
    fig.tight_layout()
    ax[1].legend()
    plt.grid(True)
    plt.savefig(f'./img_file/train/{file_name}.png')
    plt.show()

def plot_error(y_test, predict, index, file_name, window_size):
    plt.plot(index, y_test-predict)
    plt.grid(True)
    plt.title(f'Error@window size={window_size} MAE={mean_absolute_error(y_test, predict):.2f} MAPE={mean_absolute_percentage_error(y_test, predict):.2f}')
    plt.savefig(f'./img_file/error/{file_name}.png')
    plt.show()