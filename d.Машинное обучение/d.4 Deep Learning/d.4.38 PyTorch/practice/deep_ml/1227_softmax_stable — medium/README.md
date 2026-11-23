# Deep-ML #1227 · Numerically Stable Softmax · **medium**

**Уровень:** medium (Deep-ML).

- [problems/1227](https://www.deep-ml.com/problems/1227) · [1227_softmax_stable.ipynb](./1227_softmax_stable.ipynb) · эталон [1227_softmax_stable_решения.ipynb](./1227_softmax_stable_решения.ipynb) **после** попытки

## Что это за задача

Численно **устойчивый softmax** (вычитание max по оси).

## Зачем это в реальной жизни

На больших логитах naive softmax → overflow/NaN. Та же идея в `F.softmax` и в cross-entropy внутри PyTorch — без неё прод-модели падают на выбросах.

