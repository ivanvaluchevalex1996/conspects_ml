# Deep-ML #1221 · Reshape and Transpose a Tensor · **easy**

**Уровень:** easy (Deep-ML).

- [problems/1221](https://www.deep-ml.com/problems/1221) · [1221_reshape_transpose_tensor.ipynb](./1221_reshape_transpose_tensor.ipynb) · эталон [1221_reshape_transpose_tensor_решения.ipynb](./1221_reshape_transpose_tensor_решения.ipynb) **после** попытки

## Что это за задача

**reshape / view** и **transpose / permute**: привести данные к форме, которую ждёт слой (NCHW, NT, …).

## Зачем это в реальной жизни

Картинки, батчи, attention — всё через правильные оси. Ошибка permute ломает свёртки и loss; в DataLoader коллатор тоже про формы.

