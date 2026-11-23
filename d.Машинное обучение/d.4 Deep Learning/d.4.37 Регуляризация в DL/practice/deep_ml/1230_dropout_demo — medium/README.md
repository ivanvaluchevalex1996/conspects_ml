# Deep-ML #1230 · dropout_demo · **medium**
**Уровень:** medium (Deep-ML).


- [problems/1230](https://www.deep-ml.com/problems/1230) · [1230_dropout_demo.ipynb](./1230_dropout_demo.ipynb) · эталон [1230_dropout_demo_решения.ipynb](./1230_dropout_demo_решения.ipynb) **после** попытки

## Что это за задача

Показать разницу **train vs eval** для dropout: разные маски / поведение.

## Зачем это в реальной жизни

Типичный баг: забыли `model.eval()` перед валидацией или прод-инференсом — метрики «плывут», предсказания шумные. Задача фиксирует правильную семантику режимов.

