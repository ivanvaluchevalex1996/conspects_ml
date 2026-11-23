# Deep-ML #151 · DropoutLayer (NumPy) · **medium**
**Уровень:** medium (Deep-ML).


- [problems/151](https://www.deep-ml.com/problems/151) · [151_dropout_layer.ipynb](./151_dropout_layer.ipynb) · эталон [151_dropout_layer_решения.ipynb](./151_dropout_layer_решения.ipynb) **после** попытки

## Что это за задача

Слой **Dropout** на NumPy (маска, train/eval).

## Зачем это в реальной жизни

До `nn.Dropout` полезно реализовать механику самому: почему при инференсе ничего не «выкидываем», а только масштабируем при обучении.

