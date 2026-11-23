# Deep-ML #1226 · Implement ReLU and Leaky ReLU · **easy**

**Уровень:** easy (Deep-ML).

- [problems/1226](https://www.deep-ml.com/problems/1226) · [1226_relu_leaky_relu.ipynb](./1226_relu_leaky_relu.ipynb) · эталон [1226_relu_leaky_relu_решения.ipynb](./1226_relu_leaky_relu_решения.ipynb) **после** попытки

## Что это за задача

ReLU и Leaky ReLU через **PyTorch** (тензоры, без ручного цикла по элементам).

## Зачем это в реальной жизни

В реальном коде активации — **векторизованно** на GPU; задача приучает использовать `F.relu` / `nn.ReLU`, а не Python-циклы.

