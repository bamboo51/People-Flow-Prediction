# Training using seq2seq

## Data visulaization
<center><img src="./img/data.png"></img></center>

## Training curve
hyperparameters
- `epochs`: 100
- `batch_size`: 128
- `learning_rate`: 0.001
- `monitor`: "val_loss"
- `patience`: 10
- `loss`: "mse"
- `metrics`: ["mae"]
- `validation_split`: 0.2
<center><img src="./img/loss.png"></center>

## Actual vs Predict
<center>
    <img src="./img/pred_actual.png">
    <img src="./img/error.png">
</center>