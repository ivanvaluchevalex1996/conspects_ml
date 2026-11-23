# Deep-ML #26 · Basic Autograd (`Value`) · **medium**
**Уровень:** medium (Deep-ML).


- [problems/26](https://www.deep-ml.com/problems/26) · [26_basic_autograd.ipynb](./26_basic_autograd.ipynb) · эталон [26_basic_autograd_решения.ipynb](./26_basic_autograd_решения.ipynb) **после** попытки
- Референс: [micrograd](https://github.com/karpathy/micrograd)

## Что это за задача

Свой мини-движок **autograd** (как Karpathy micrograd): класс `Value`, ребро графа, `backward()`.

## Зачем это в реальной жизни

PyTorch под капотом строит **граф вычислений** и рассылает градиенты. Реализация руками показывает, почему нужны `zero_grad`, зачем не держать лишние ссылки и как из одного скаляра loss течёт ∂ к весам.

