from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

def train(model, x_train, y_train, epochs:int=100):
    # batch_size = x_train.shape[0]//(epochs//2)
    batch_size = 128
    opt = Adam(learning_rate=0.001)
    model.compile(optimizer=opt, loss="mse", metrics=["mae"])
    es = EarlyStopping(monitor="val_loss", patience=10, verbose=1, mode="auto")
    history = model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2, callbacks=[es], shuffle=False)
    return history