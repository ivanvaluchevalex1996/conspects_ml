# d.4.35 · ML Handbook гл. 35 — Backpropagation

Сайт: [backprop.html](https://mlhandbook-production.up.railway.app/parts/deep-learning/backprop.html) · [`README.md`](./README.md)

**Теория:** [`d.4.1` §11](../d.4.33 Нейрон и полносвязная сеть/d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md#11-как-сеть-учится-пока-смысл-не-вся-математика) · база цепочки [`d.0`](../../d.0%20Градиент%20и%20правило%20цепочки.md)  
**Разбор руками (вне handbook):** [e.1 micrograd](../../../e.%D0%9A%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D0%B8%20%E2%80%94%20%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC%20micrograd/e.1%20%D0%9A%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D0%B8%20%E2%80%94%20%D1%80%D0%B0%D0%B7%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC%20micrograd.md)  
**Практика:** [`handbook_gl35/`](./practice/README.md)

| § | Ментор | У тебя |
|:---:|:---|:---|
| 35.1 | forward + backward | [§11.1–11.2](../d.4.33 Нейрон и полносвязная сеть/d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md#112-backpropagation--что-запомнить) |
| 35.2 | цепное правило | [§11.2](../d.4.33 Нейрон и полносвязная сеть/d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md#112-backpropagation--что-запомнить), [d.0 §8–9](../../d.0%20Градиент%20и%20правило%20цепочки.md) |
| 35.3 | XOR NumPy | [`35_3_xor_numpy/`](./practice/site/35_3_xor_numpy/) |
| 35.4 | autograd / `backward` | [§11.2](../d.4.33 Нейрон и полносвязная сеть/d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md#backprop-только-считает-градиенты--веса-обновляет-оптимизатор), [`35_4_xor_torch/`](./practice/site/35_4_xor_torch/) |
| 35.5 | вычислительный граф | e.1 · [d.0 §8](../../d.0%20Градиент%20и%20правило%20цепочки.md) |
| 35.6 | grad check | [`35_6_grad_check/`](./practice/site/35_6_grad_check/) |

Дальше: [d.4.36](./d.4.36%20%D0%9E%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL.md).