# ML Handbook · Deep Learning (гл. 33–37)

Порядок как у [ментора](https://mlhandbook-production.up.railway.app/parts/deep-learning/neural-network.html). Текст теории **не дублируем** — в `d.4.1` / `d.4.2` / `d.4.3` внутри папок `d.4.33`–`37`; здесь **вход по номерам handbook** и таблицы § → §.

**Гл. 38–39 (PyTorch)** — отдельно: папка [`pytorch`](../../../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/pytorch/) (`pytorch%20дубинин`, `pytorch%20handbook`), см. [`d.4 Deep Learning.md`](./d.4%20Deep%20Learning.md).

## Карта handbook ↔ ynote

| гл. | Конспект-вход | Сайт | Локальная теория | Практика |
|:---:|:---|:---|:---|:---|
| **33** | [d.4.33](d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md) | [neural-network](https://mlhandbook-production.up.railway.app/parts/deep-learning/neural-network.html) | [`d.4.33` §5–8](d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md) | [`practice/`](d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/practice/) |
| **34** | [d.4.34](d.4.34%20Функции%20активации/d.4.34%20Функции%20активации.md) | [activations](https://mlhandbook-production.up.railway.app/parts/deep-learning/activations.html) | [`d.4.33` §8–9](d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md), [`d.4.1.1`](d.4.34%20Функции%20активации/d.4.1.1%20%D0%97%D0%B0%D1%82%D1%83%D1%85%D0%B0%D1%8E%D1%89%D0%B8%D0%B9%20%D0%B3%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%20%E2%80%94%20%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20ReLU%20%D0%B2%20%D1%81%D0%BA%D1%80%D1%8B%D1%82%D1%8B%D1%85%2C%20%D0%B0%20%D0%BD%D0%B5%20sigmoid.md) | [`practice/`](d.4.34%20Функции%20активации/practice/) |
| **35** | [d.4.35](d.4.35%20Backpropagation/d.4.35%20Backpropagation.md) | [backprop](https://mlhandbook-production.up.railway.app/parts/deep-learning/backprop.html) | [`d.4.33` §11](d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md), [e.1 micrograd](../../e.%D0%9A%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D0%B8%20%E2%80%94%20%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC%20micrograd/e.1%20%D0%9A%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D0%B8%20%E2%80%94%20%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC%20micrograd.md) | [`practice/`](d.4.35%20Backpropagation/practice/) |
| **36** | [d.4.36](d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL.md) | [dl-optimization](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-optimization.html) | [`d.4.2`](d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/d.4.2%20Градиентная%20оптимизация.md) | [`practice/`](d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/practice/) |
| **37** | [d.4.37](d.4.37%20Регуляризация%20%D0%B2%20DL/d.4.37%20Регуляризация%20%D0%B2%20DL.md) | [dl-regularization](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-regularization.html) | [`d.4.3`](d.4.37%20Регуляризация%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md) | [`practice/`](d.4.37%20Регуляризация%20%D0%B2%20DL/practice/) |

## Старая нумерация d.4.x (всё на месте)

| d.4.x | Handbook |
|:---|:---|
| d.4.1 + practice | → **d.4.33** |
| d.4.2 + practice | → **d.4.36** |
| d.4.3 + practice | → **d.4.37** |
| `handbook/` (33–37) | → папки **d.4.33–37** + `practice/` |