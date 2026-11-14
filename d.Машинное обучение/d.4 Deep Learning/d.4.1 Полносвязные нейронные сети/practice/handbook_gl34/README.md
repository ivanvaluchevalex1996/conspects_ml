# ML Handbook гл. 34 · Функции активации

Источник: [Функции активации](https://mlhandbook-production.up.railway.app/parts/deep-learning/activations.html)

**Теория** — [`d.4.1 … .md`](../../d.4.1%20Полносвязные%20нейронные%20сети.md) **§8–9**.

| Часть | Папка |
|--------|--------|
| Handbook §34.4–advanced | [`handbook/`](./handbook/README.md) |
| Deep-ML #22…#98 | [`deep_ml/`](./deep_ml/README.md) |

---

## Карта handbook → конспект

| Handbook | О чём | В `d.4.1` |
|----------|--------|-----------|
| §34.1 | σ, tanh, vanishing gradient | §8, §9.2 |
| §34.2 | ReLU | §8, §9.1 |
| §34.3 | Leaky ReLU, ELU, GELU… | §9.4 |
| §34.4 | softmax на выходе | §9.3, §10.2 |
| §34.5 | затухание σ′ по слоям | §8, §11 (смысл) |
| §34.6 | «мёртвый» ReLU, Leaky/ELU/GELU | §9.4 |
| Advanced | устойчивый softmax | §9.3.1 |
| Шпаргалка «что брать» | ReLU скрытые / σ·softmax выход | §8, §10 |

§34.1–34.3, 34.6 (картинки) на сайте — **прочитать/посмотреть**; ячейки с кодом — в ноутбуке.

---

## Домашка · Deep-ML

Таблица задач и порядок — **только** в [`deep_ml/README.md`](./deep_ml/README.md) (здесь не дублируем).

Кратко: сначала [`handbook/`](./handbook/) по разделам → затем `deep_ml/` по номеру на [deep-ml.com](https://www.deep-ml.com) → архив [`13_deep_ml…`](../../../../../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/python_base/13_deep_ml_deep_learning.py).

Полная таблица ↔ конспекты: [`Deep-ML — задачи ↔ конспекты`](../../../Deep-ML%20%E2%80%94%20%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8%20%E2%86%94%20%D0%BA%D0%BE%D0%BD%D1%81%D0%BF%D0%B5%D0%BA%D1%82%D1%8B.md).

**PyTorch-курс:** после handbook — [`pytorch/08`](../../../../../../учеба%20мл/pytorch/08/08_активации_потери_оптимизатор.ipynb).