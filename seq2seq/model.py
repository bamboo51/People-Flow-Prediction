from keras.layers import Input, LSTM, BatchNormalization, RepeatVector, TimeDistributed, Dense
from keras.models import Model

class Encoder:
    def __init__(self, time_step):
        self.time_step = time_step

    def build(self):
        inputs = Input(shape=(self.time_step, 1))
        encoder_last_h1, _, encoder_last_c = LSTM(32, return_sequences=False, return_state=True)(inputs)
        encoder_last_h1 = BatchNormalization()(encoder_last_h1)
        encoder_last_c = BatchNormalization()(encoder_last_c)
        return inputs, [encoder_last_h1, encoder_last_c]

class Decoder:
    def __init__(self, time_step):
        self.time_step = time_step

    def build(self, encoder_last_h1, encoder_last_c):
        decoder_input = RepeatVector(self.time_step)(encoder_last_h1)
        decoder_output = LSTM(32, return_state=False, return_sequences=True)(decoder_input, initial_state=[encoder_last_h1, encoder_last_c])
        outputs = TimeDistributed(Dense(1))(decoder_output)
        return outputs

class Seq2Seq:
    def __init__(self, time_step:int=10):
        self.time_step = time_step

    def build(self):
        encoder = Encoder(self.time_step)
        decoder = Decoder(self.time_step)

        inputs, [encoder_last_h1, encoder_last_c] = encoder.build()
        outputs = decoder.build(encoder_last_h1, encoder_last_c)

        model = Model(inputs=inputs, outputs=outputs)
        model.summary()
        return model
