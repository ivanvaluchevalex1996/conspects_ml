# d.4.37 · ML Handbook гл. 37 — Регуляризация в Deep Learning

Сайт: [dl-regularization.html](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-regularization.html) · [`README.md`](./README.md)

**Теория:** [`d.4.3`](./d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md) · примеры [`d.4.3.1`](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3.1%20Пример%20—%20нормализация%20и%20один%20шаг%20обучения.md) · [`d.4.3.2`](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3.2%20Пример%20—%20зачем%20BatchNorm.md) · [`d.4.3.3`](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3.3%20Пример%20—%20Dropout%20и%20чем%20он%20отличается%20от%20ReLU.md)  
**Практика:** [`practice/`](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/practice/README.md)

| Тема handbook | У тебя в `d.4.3` |
|:---|:---|
| нормализация входа | [§1](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md#1-нормализация-входных-данных-пункт-лекции-data-normalization) |
| weight decay (L2) | [§2.1](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md#21-через-лосс--штраф-за-большие-веса-weight-decay) |
| Dropout | [§2.2](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md#dropout--случайно-выключаем-нейроны-на-обучении) |
| BatchNorm (регуляризация) | [§2.2 BN](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md#batch-normalization-batchnorm--нормализация-внутри-сети) |
| аугментации | [§2.3](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md#23-через-данные--аугментации) |
| early stopping | [§2.4](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md#24-early-stopping--остановиться-вовремя) |
| метрики vs loss | [§3](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md#3-метрики-и-валидация-в-dl) |

Конец блока DL handbook (33–37). PyTorch гл. 38–39 — папка [`pytorch`](../../../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/pytorch/).