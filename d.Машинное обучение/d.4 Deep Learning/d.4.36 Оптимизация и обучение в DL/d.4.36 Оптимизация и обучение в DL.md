# d.4.36 · ML Handbook гл. 36 — Оптимизация и обучение в DL

Сайт: [dl-optimization.html](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-optimization.html) · [`README-legacy.md`](./README-legacy.md)

**Теория (полный текст):** [`d.4.2`](./d.4.2%20Градиентная%20оптимизация.md) · **практика:** [`practice/`](./practice/README.md)

| § | Ментор | У тебя в `d.4.2` |
|:---:|:---|:---|
| 36.1 | Adam, AdamW, SGD+Momentum | [§2.2–2.5](./d.4.2%20Градиентная%20оптимизация.md#22-sgd--базовый-шаг) |
| 36.2 | инициализация Xavier / He | [§1](./d.4.2%20Градиентная%20оптимизация.md#1-инициализация-весов-спрашивают-на-собесах) · практика [`36_5_he_init/`](../d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/practice/site/36_5_he_init/) |
| 36.3 | BatchNorm | [§2.2 BN в `d.4.3`](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md#22-batch-normalization-batchnorm--нормализация-внутри-сети), [`36_3_batchnorm/`](../d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/practice/site/36_3_batchnorm/) |
| 36.4 | LR schedule, warmup, residual | [§2.6](./d.4.2%20Градиентная%20оптимизация.md#26-learning-rate-как-выбрать-и-как-менять), residual — [`d.4.33` §9.5.1](../d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md#951-остаточный-блок-shortcut--deep-ml-113) |
| 36.5 | наглядно: инициализация | [`36_5_he_init/`](../d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/practice/site/36_5_he_init/) |
| 36.6 | BN ускоряет обучение | [`36_6_bn_training/`](../d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/practice/site/36_6_bn_training/) |

Дальше: [d.4.37](../d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL/d.4.37%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20DL.md).