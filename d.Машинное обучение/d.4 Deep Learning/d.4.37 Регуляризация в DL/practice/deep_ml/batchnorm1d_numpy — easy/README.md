# BatchNorm1d (NumPy, ментор) · **easy**
**Уровень:** easy (Deep-ML).


- [batchnorm1d_numpy.ipynb](./batchnorm1d_numpy.ipynb) · эталон [batchnorm1d_numpy_решения.ipynb](./batchnorm1d_numpy_решения.ipynb) **после** попытки

## Что это за задача

BatchNorm **1D руками** на NumPy: среднее/дисперсия по батчу, нормализация, γ и β.

## Зачем это в реальной жизни

BatchNorm стабилизирует активации, позволяет **больший lr** и ускоряет сходимость в CNN/MLP. В проде важно знать разницу train (статистика батча) vs eval (скользящее среднее).

