# d.5.43 · ML Handbook гл. 43 — Обучение представлений и metric learning

Сайт: [representation-learning.html](https://mlhandbook-production.up.railway.app/parts/deep-learning/representation-learning.html) · [README.md](./README.md) · [карта d.5](../d.5%20advanced%20Deep%20Learning.md)

| § | Ментор | Якорь |
|:---:|:---|:---|
| 43.1 | эмбеддинг | [§2](#2-эмбеддинг-handbook-431) |
| 43.2 | contrastive, triplet | [§3](#3-metric-learning-handbook-432) |
| 43.3 | ArcFace, метрики 1:1 / 1:N | [§4](#4-arcface-handbook-433) |
| 43.4 | self-supervised, связка с поиском | [§5](#5-self-supervised-и-прод-handbook-434) |

**Практика:** [practice/](./practice/README.md) · [handbook_gl43_практика.ipynb](./practice/handbook_gl43_практика.ipynb)

Transfer / энкодеры: [d.5.42](../d.5.42%20Transfer%20learning/d.5.42%20Transfer%20learning.md). Трансформер как энкодер текста: [d.5.40](../d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer/d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer.md).

> **Для NLP и recsys это одна из главных в d.5.**

---

## 0. Зачем это тебе

| Задача | На чём стоит |
| --- | --- |
| Семантический поиск (NLP) | текст → **вектор** → ближайшие соседи |
| RAG | тот же векторный поиск + LLM |
| Рекомендации | user/item **эмбеддинги**, похожесть = dot / cosine |
| Дедуп, антифрод | «похоже ли на известное мошенничество» |
| Распознавание лиц | metric learning (ArcFace) |

Классификация учит **границу между классами**. Metric learning учит **геометрию**: близко — похоже, далеко — нет. Это нужно, когда классов **слишком много** или они **открытые** (новые товары/лица не были в train).

---

## 1. Эмбеддинг *(handbook 43.1)*

**Эмбеддинг** — вектор фиксированной длины d, где **семантика ≈ расстояние**.

Откуда берётся:

| Источник | Пример |
| --- | --- |
| предпоследний слой сети | CNN/трансформер без финальной головы |
| `nn.Embedding` | id товара, id пользователя, id слова |
| предобученные модели | BERT `[CLS]`, sentence-transformers |

```python
emb = nn.Embedding(num_embeddings=1000, embedding_dim=16)
# ids → (batch, 16)
```

**word2vec (идея):** «король − мужчина + женщина ≈ королева» — линейная арифметика в пространстве.

В recsys **matrix factorization** — по сути выученные эмбеддинги user и item.

---

## 2. Metric learning *(handbook 43.2)*

### 2.1. Contrastive loss

Пара объектов (a, b), метка y: 1 — один класс, 0 — разные. d = ‖f(a) − f(b)‖.

$$
\Large
L = y \cdot d^2 + (1-y) \cdot \max(0,\; m - d)^2
$$

m — зазор: разные не нужно отталкивать бесконечно, достаточно расстояния m.

### 2.2. Triplet loss

Тройка: **anchor** a, **positive** p (тот же класс), **negative** n (чужой).

$$
\Large
L = \max\big(0,\; d(a,p) - d(a,n) + m\big)
$$

Цель: a ближе к p, чем к n, хотя бы на m.

**Hard negative mining:** случайный «чужой» часто уже далеко — градиент ≈ 0. Берут **близкий** чужой, которого модель путает — обучение ускоряется.

### 2.3. Retrieval-метрика

После обучения: нормируем эмбеддинги, ищем **ближайшего соседа** (cosine = dot на единичной сфере). Доля случаев, когда сосед **того же класса** — sanity-check (handbook ~96% на digits).

---

## 3. ArcFace *(handbook 43.3)*

Triplet'ы капризны (майнинг, сходимость). При **миллионах классов** (лица) удобнее **margin-softmax**.

Идея: нормируем эмбеддинг f и веса классов W_j → логит = **cos θ_j**. К **своему** классу добавляют угловой зазор m:

$$
\Large
L = -\log \frac{e^{s \cos(\theta_y + m)}}{e^{s \cos(\theta_y + m)} + \sum_{j \neq y} e^{s \cos \theta_j}}
$$

s — масштаб (температура), m — margin.

| Семейство | Зазор |
| --- | --- |
| SphereFace | cos(mθ) — нестабильнее |
| CosFace | cos θ − m |
| **ArcFace** | cos(θ + m) — частый стандарт |

**Train:** backbone → эмбеддинг → ArcFace-голова + CE.  
**Inference:** голову выбрасывают, сравнивают **только эмбеддинги**.

### Метрики (открытое множество классов)

| Задача | Суть | Метрики |
| --- | --- | --- |
| **Верификация 1:1** | один и тот же человек? | ROC, TAR@FAR, EER |
| **Идентификация 1:N** | кто из галереи? | rank-1, CMC |

### Когда что брать

| Подход | Когда |
| --- | --- |
| ArcFace / CosFace | много размеченных классов |
| Triplet / contrastive | есть пары «похоже/нет», мало чистых классов |
| Self-supervised | разметки нет |

---

## 4. Self-supervised и прод *(handbook 43.4)*

**SimCLR / MoCo:** две аугментации одной картинки — позитив; остальной батч — негативы. Мощные визуальные эмбеддинги **без** меток → потом fine-tune.

**Текст:** sentence-transformers — семантический поиск, FAQ, RAG.

**Связка продакшена:**

```text
объект → энкодер → эмбеддинг → ANN (FAISS / HNSW) → топ-K похожих
```

Рекомендации, поиск, антифрод, дубликаты — один паттерн.

---

## 5. NLP vs recsys (как стыкуется)

| NLP | Recsys |
| --- | --- |
| запрос и документ в одном embedding space | user tower и item tower |
| cosine(query, doc) | dot(user, item) или cosine |
| fine-tune энкодера на NLU | доучить эмбеддинги на кликах / ALS hybrid |

Две башни — та же идея, что **siamese** энкодер в metric learning (общие веса на user/item или текст/картинку).

---

## 6. Практика (handbook, позже)

digits + triplet, PCA/t-SNE кластеры; hard negatives; contrastive vs raw pixels.

---

## 7. Шпаргалка

- **Эмбеддинг** = вектор; похожесть = расстояние/cosine.
- **Metric learning** — учим пространство, не softmax на 10⁶ классов.
- **Triplet:** d(a,p) + m < d(a,n).
- **ArcFace:** cos(θ+m) на свой класс; inference без головы.
- **ANN-поиск** — обязательная часть стека (RAG, recsys).

Назад: [d.5.42](../d.5.42%20Transfer%20learning/d.5.42%20Transfer%20learning.md) · Дальше: [d.5.44](../d.5.44%20Оптимизация%20нейросетей%20сжатие/d.5.44%20Оптимизация%20нейросетей%20—%20дистилляция%20квантование%20прунинг.md)