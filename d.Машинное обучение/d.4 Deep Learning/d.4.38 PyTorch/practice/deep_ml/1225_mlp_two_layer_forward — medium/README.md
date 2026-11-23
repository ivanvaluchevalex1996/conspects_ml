# Deep-ML #1225 · Two-Layer MLP Forward Pass · **medium**

**Уровень:** medium (Deep-ML).

- [problems/1225](https://www.deep-ml.com/problems/1225) · [1225_mlp_two_layer_forward.ipynb](./1225_mlp_two_layer_forward.ipynb) · эталон [1225_mlp_two_layer_forward_решения.ipynb](./1225_mlp_two_layer_forward_решения.ipynb) **после** попытки

## Что это за задача

Прямой проход **двухслойного MLP**: линейный → активация → линейный.

## Зачем это в реальной жизни

Типичный **табличный классификатор / MLP** перед softmax. Forward отдельно — без backward — чтобы не смешивать «что считает сеть» и «как учится».

