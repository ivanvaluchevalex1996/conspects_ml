# Deep-ML #146 · momentum_optimizer · **easy** · **easy**

**Уровень:** easy (Deep-ML); доп. к блоку handbook (нет в 🎯 Домашка на [гл.36](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-optimization.html)).

- [problems/146](https://www.deep-ml.com/problems/146) · [146_momentum.ipynb](./146_momentum.ipynb) · эталон [146_momentum_решения.ipynb](./146_momentum_решения.ipynb) **после** попытки

## Что это за задача

Один шаг **SGD с momentum** в NumPy: накопление скорости по градиенту.

## Зачем это в реальной жизни

Momentum сглаживает шум в стохастических батчах и быстрее идёт по «долинам» лосса. Основа перед Adam; в SGD+nesterov ещё используется в CV.

