# Deep-ML #25 · Single Neuron + backprop · **medium**
**Уровень:** medium (Deep-ML).


- [problems/25](https://www.deep-ml.com/problems/25) · [25_single_neuron_backprop.ipynb](./25_single_neuron_backprop.ipynb) · эталон [25_single_neuron_backprop_решения.ipynb](./25_single_neuron_backprop_решения.ipynb) **после** попытки
- Теория: [d.4.35](../../../d.4.35%20Backpropagation/d.4.35%20Backpropagation.md) §11

## Что это за задача

Обучить **один нейрон** с MSE и сигмоидой: прямой проход, градиенты, шаг градиентного спуска по батчу.

## Зачем это в реальной жизни

Мини-версия **полного цикла обучения** без autograd: так понимают, что делает `loss.backward()` и `optimizer.step()`. Полезно при отладке «почему не учится» на маленькой модели.

