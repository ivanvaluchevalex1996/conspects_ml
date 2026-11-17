# d.4 Deep Learning

**Лекции DLS (YouTube):** [градиентная оптимизация](https://www.youtube.com/watch?v=6CvpMOO-DB4) → [d.4.36](d.4.36%20Оптимизация%20и%20обучение%20в%20DL/d.4.36%20Оптимизация%20и%20обучение%20в%20DL.md) · [регуляризация](https://www.youtube.com/watch?v=x72-oUjv1ew) → [d.4.37](d.4.37%20Регуляризация%20в%20DL/d.4.37%20Регуляризация%20в%20DL.md) · слайды: [Оптимизация_и_регуляризация_в_Deep_Learning.pdf](../Оптимизация_и_регуляризация_в_Deep_Learning.pdf)

Порядок **как ML Handbook ментора (гл. 33–37)**. База градиента: [d.0](../d.0%20Градиент%20и%20правило%20цепочки.md#0-зачем-это-всё).

**Гл. 38–39 (PyTorch)** — не здесь: [учеба мл/pytorch](../../../pytorch/pytorch%20дубинин/0_как_учить_pytorch.md) · блок внизу.

## Карта handbook ↔ папки

| гл. | Папка | Вход | Теория (полный текст) | Практика |
|:---:|:---|:---|:---|:---|
| **33** | [d.4.33](d.4.33%20Нейрон%20и%20полносвязная%20сеть/d.4.33%20Нейрон%20и%20полносвязная%20сеть.md) | [сайт](https://mlhandbook-production.up.railway.app/parts/deep-learning/neural-network.html) | §0–§7, §12–13 (активации и backprop — в d.4.34 / d.4.35) | [practice/](d.4.33%20Нейрон%20и%20полносвязная%20сеть/practice/) |
| **34** | [d.4.34](d.4.34%20Функции%20активации/d.4.34%20Функции%20активации.md) | [activations](https://mlhandbook-production.up.railway.app/parts/deep-learning/activations.html) | полный текст §8–10, затухание в §9.2.1 | [practice/](d.4.34%20Функции%20активации/practice/) |
| **35** | [d.4.35](d.4.35%20Backpropagation/d.4.35%20Backpropagation.md) | [backprop](https://mlhandbook-production.up.railway.app/parts/deep-learning/backprop.html) | §11 в [том же файле](d.4.35%20Backpropagation/d.4.35%20Backpropagation.md); + [e.1 micrograd](../../e.Карпати%20—%20разбираем%20micrograd/e.1%20Карпати%20—%20разбираем%20micrograd.md) | [practice/](d.4.35%20Backpropagation/practice/) |
| **36** | [d.4.36](d.4.36%20Оптимизация%20и%20обучение%20в%20DL/d.4.36%20Оптимизация%20и%20обучение%20в%20DL.md) | [dl-optimization](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-optimization.html) | полный текст в [том же файле](d.4.36%20Оптимизация%20и%20обучение%20в%20DL/d.4.36%20Оптимизация%20и%20обучение%20в%20DL.md) | [practice/](d.4.36%20Оптимизация%20и%20обучение%20в%20DL/practice/) |
| **37** | [d.4.37](d.4.37%20Регуляризация%20в%20DL/d.4.37%20Регуляризация%20в%20DL.md) | [dl-regularization](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-regularization.html) | полный текст + примеры [d.4.37.1](d.4.37%20Регуляризация%20в%20DL/d.4.37.1%20Пример%20—%20нормализация%20и%20один%20шаг%20обучения.md), [d.4.37.2](d.4.37%20Регуляризация%20в%20DL/d.4.37.2%20Пример%20—%20Dropout%20и%20чем%20он%20отличается%20от%20ReLU.md); BN → [d.4.36.1](d.4.36%20Оптимизация%20и%20обучение%20в%20DL/d.4.36.1%20Пример%20—%20зачем%20BatchNorm.md) | [practice/](d.4.37%20Регуляризация%20в%20DL/practice/) |

## Трек **e** (вне handbook; ynote)

| # | Файл |
|:---|:---|
| e.1 | [Карпати / micrograd](../../e.Карпати%20—%20разбираем%20micrograd/e.1%20Карпати%20—%20разбираем%20micrograd.md) |

## Связь с соседними разделами

| Нужно | Куда |
|:---|:---|
| Градиент, цепочка | [d.0](../d.0%20Градиент%20и%20правило%20цепочки.md) |
| Loss | [d.1.2](../d.1%20Введение%20в%20мл/d.1.2%20Loss%20и%20эмпирический%20риск.md) |
| SGD классика | [d.2.1.4](../d.2%20Линейные%20модели%20метрические%20методы/d.2.1%20Линейные%20модели/d.2.1.4%20Градиент%20MSE%20и%20SGD%20для%20линейной%20регрессии.md) |
| Classic ML | [d.3](../d.3%20Classic%20ML/d.3%20Classic%20ML.md) |

## PyTorch (гл. 38–39, отдельная папка)

Код: [pytorch дубинин](../../../pytorch/pytorch%20дубинин/0_как_учить_pytorch.md) · handbook [gl38](../../../pytorch/pytorch%20handbook/handbook_gl38/README.md) · [gl39](../../../pytorch/pytorch%20handbook/handbook_gl39/README.md)

| Тема DL | PyTorch |
| --- | --- |
| гл. 33–35 | `08/`–`11/`, project |
| гл. 36 | `08/` блок 5, `12/` |
| гл. 37 | `07/`, `14`–`16/` |
| e.1 | `08/` блок 5 |