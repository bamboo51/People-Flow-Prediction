from model import Seq2Seq
from train import train
from preprocess import Data
from plot import *

# preprocessing data
data = Data()
original_data = data.load()
plot_data(original_data)
original_data = data.interpolate()
plot_data(original_data)
data.normalize()
data.truncate()
truncated_data, train_size, test_size = data.split()
print(original_data["datetime"][train_size:])

# build model
model = Seq2Seq()
seq2seq = model.build()

# train model
history = train(seq2seq, truncated_data["ei_train"], truncated_data["di_train"])
plot_loss(history)

predict = seq2seq.predict(truncated_data["ei_test"])
predict = predict[:, -1, :]
predict = data.scaler.inverse_transform(predict)
test_data = data.scaler.inverse_transform(truncated_data["do_test"][:, -1, :])
index = original_data["datetime"][train_size:]
plot_predict(test_data, predict, index=index)
plot_error(test_data, predict, index=index)


