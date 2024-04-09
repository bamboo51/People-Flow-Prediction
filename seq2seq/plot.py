import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

'''
Set matplotlib
'''
plt.rcParams["figure.figsize"] = [12, 6]   ##
# plt.rcParams['figure.dpi'] = 300           ## 300 for printing
plt.rc('font', size=8)                     ## 
plt.rc('axes', titlesize=16)               ## 
plt.rc('axes', labelsize=14)               ##
plt.rc('xtick', labelsize=10)              ##
plt.rc('ytick', labelsize=10)              ##
plt.rc('legend', fontsize=10)              ##
plt.rc('figure', titlesize=12)             ## 
#############################################
plt.rcParams.update({'axes.grid'     : True})


def plot_data(data, title:str="Amount of people at p040"):
    plt.plot(data["datetime"], data["count"])
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amount of people")
    plt.savefig("./img/data.png")
    plt.show()

def plot_loss(history, title:str="Loss"):
    plt.plot(history.history["loss"], label="Training Loss")
    plt.plot(history.history["val_loss"], label="Validation Loss")
    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig("./img/loss.png")
    plt.show()

def plot_predict(test_data, predict_data, title:str="Predicted vs Actual", index=None):
    plt.plot(index[len(index)-test_data.shape[0]:], test_data, label="Actual")
    plt.plot(index[len(index)-predict_data.shape[0]:], predict_data, label="Predicted")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amount of people")
    plt.legend()
    plt.savefig("./img/pred_actual.png")
    plt.show()

def plot_error(test_data, predict_data, title:str="Error", index=None):
    plt.plot(index[len(index)-test_data.shape[0]:], test_data-predict_data, label="Error")
    error = mean_absolute_error(test_data, predict_data)
    plt.title(f"MAE: {error}")
    plt.xlabel("Time")
    plt.ylabel("Amount of people")
    plt.legend()
    plt.savefig("./img/error.png")
    plt.show()