# d.4 Deep Learning

Порядок **как ML Handbook ментора (гл. 33–37)**. База градиента: [d.0](../d.0%20Градиент%20и%20правило%20цепочки.md#0-%D0%B7%D0%B0%D1%87%D0%B5%D0%BC-%D1%8D%D1%82%D0%BE-%D0%B2%D1%81%D1%91).

**Гл. 38–39 (PyTorch)** — не здесь: [`учеба мл/pytorch`](../../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/pytorch/) · блок внизу.

## Карта handbook ↔ папки

| гл. | Папка | Вход | Теория (полный текст) | Практика |
|:---:|:---|:---|:---|:---|
| **33** | [d.4.33](d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md) | [сайт](https://mlhandbook-production.up.railway.app/parts/deep-learning/neural-network.html) | §0–§7, §12–13 (активации и backprop — в d.4.34 / d.4.35) | [`practice/`](d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/practice/) |
| **34** | [d.4.34](d.4.34%20Функции%20активации/d.4.34%20Функции%20активации.md) | [activations](https://mlhandbook-production.up.railway.app/parts/deep-learning/activations.html) | полный текст §8–10; [d.4.1.1](d.4.34%20Функции%20активации/d.4.1.1%20%D0%97%D0%B0%D1%82%D1%83%D1%85%D0%B0%D1%8E%D1%89%D0%B8%D0%B9%20%D0%B3%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%20%E2%80%94%20%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20ReLU%20%D0%B2%20%D1%81%D0%BA%D1%80%D1%8B%D1%82%D1%8B%D1%85%2C%20%D0%B0%20%D0%BD%D0%B5%20sigmoid.md) | [`practice/`](d.4.34%20Функции%20активации/practice/) |
| **35** | [d.4.35](d.4.35%20Backpropagation/d.4.35%20Backpropagation.md) | [backprop](https://mlhandbook-production.up.railway.app/parts/deep-learning/backprop.html) | §11 в [том же файле](d.4.35%20Backpropagation/d.4.35%20Backpropagation.md); + [e.1 micrograd](../../e.%D0%9A%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D0%B8%20%E2%80%94%20%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC%20micrograd/e.1%20%D0%9A%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D0%B8%20%E2%80%94%20%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC%20micrograd.md) | [`practice/`](d.4.35%20Backpropagation/practice/) |
| **36** | [d.4.36](d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL.md) | [dl-optimization](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-optimization.html) | [`d.4.2 … .md`](d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/d.4.2%20Градиентная%20оптимизация.md) | [`practice/`](d.4.36%20Оптимизация%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL/practice/) |
| **37** | [d.4.37](d.4.37%20Регуляризация%20%D0%B2%20DL/d.4.37%20Регуляризация%20%D0%B2%20DL.md) | [dl-regularization](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-regularization.html) | [`d.4.3 … .md`](d.4.37%20Регуляризация%20%D0%B2%20DL/d.4.3%20Регуляризация%20%D0%B2%20Deep%20Learning.md); примеры `d.4.3.1`–`3` | [`practice/`](d.4.37%20Регуляризация%20%D0%B2%20DL/practice/) |

Сводная таблица (старое ↔ новое): [`handbook-README-archived.md`](handbook-README-archived.md).

## Трек **e** (вне handbook; ynote)

| # | Файл |
|:---|:---|
| e.1 | [Карпати / micrograd](../../e.%D0%9A%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D0%B8%20%E2%80%94%20%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC%20micrograd/e.1%20%D0%9A%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D0%B8%20%E2%80%94%20%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC%20micrograd.md) |

## Связь с соседними разделами

| Нужно | Куда |
|:---|:---|
| Градиент, цепочка | [d.0](../d.0%20Градиент%20и%20правило%20цепочки.md) |
| Loss | [d.1.2](../d.1%20Введение%20в%20мл/d.1.2%20Loss%20%D0%B8%20%D1%8D%D0%BC%D0%BF%D0%B8%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%80%D0%B8%D1%81%D0%BA.md) |
| SGD классика | [d.2.1.4](../d.2%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B/d.2.1%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8/d.2.1.4%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%20MSE%20%D0%B8%20SGD%20%D0%B4%D0%BB%D1%8F%20%D0%BB%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%BE%D0%B9%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) |
| Classic ML | [d.3](../d.3%20Classic%20ML/d.3%20Classic%20ML.md) |

## PyTorch (гл. 38–39, отдельная папка)

Код: [`pytorch дубинин`](../../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/pytorch/pytorch%20дубинин/0_как_учить_pytorch.md) · handbook [`gl38`](../../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/pytorch/pytorch%20handbook/handbook_gl38/README.md) · [`gl39`](../../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/pytorch/pytorch%20handbook/handbook_gl39/README.md)

| Тема DL | PyTorch |
| --- | --- |
| гл. 33–35 | `08/`–`11/`, project |
| гл. 36 | `08/` блок 5, `12/` |
| гл. 37 | `07/`, `14`–`16/` |
| e.1 | `08/` блок 5 |