# Практика · handbook гл. 34

Теория — [`d.4.1 … .md`](../../d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md) §8–9. Вход handbook: [`d.4.34`](../../d.4.34%20Функции%20активации/d.4.34%20%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D0%B8.md). На сайте: [activations.html](https://mlhandbook-production.up.railway.app/parts/deep-learning/activations.html).

| Что | Где |
|-----|-----|
| §34.4–advanced (PyTorch / NumPy) | [`handbook/`](./handbook-README-archived.md) — по папке на блок |
| Deep-ML #22…#98 | [`deep_ml/`](./deep_ml/README.md) — по папке на задачу |
| Затухающий градиент · ReLU vs sigmoid (теория) | [`d.4.1.1`](../../d.4.34%20Функции%20активации/d.4.1.1%20%D0%97%D0%B0%D1%82%D1%83%D1%85%D0%B0%D1%8E%D1%89%D0%B8%D0%B9%20%D0%B3%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%20%E2%80%94%20%D0%BF%D0%BE%D1%87%D0%B5%D0%BC%D1%83%20ReLU%20%D0%B2%20%D1%81%D0%BA%D1%80%D1%8B%D1%82%D1%8B%D1%85%2C%20%D0%B0%20%D0%BD%D0%B5%20sigmoid.md); функции σ/ReLU — [`d.4.1` §9.1–9.2](../../d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md#9-%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5-%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D0%B8-%D0%B1%D1%8B%D0%B2%D0%B0%D1%8E%D1%82) |

**Порядок ментора:** допиши код в подпапке → сверка с handbook → (для Deep-ML) NumPy ↔ PyTorch → submit на [deep-ml.com](https://www.deep-ml.com). Архив: [`13_deep_ml…`](../../../../../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/python_base/13_deep_ml_deep_learning.py).

Таблица ↔ конспекты: [`Deep-ML — задачи ↔ конспекты`](../../../Deep-ML%20%E2%80%94%20%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8%20%E2%86%94%20%D0%BA%D0%BE%D0%BD%D1%81%D0%BF%D0%B5%D0%BA%D1%82%D1%8B.md).