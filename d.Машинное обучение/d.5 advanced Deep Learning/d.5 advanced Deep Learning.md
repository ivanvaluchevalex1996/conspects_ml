# d.5 · Advanced Deep Learning

**Сейчас в папке:** **теория** по ML Handbook **гл. 40–45** (блок «Продвинутый Deep Learning»). Практика и Deep-ML — позже, как в [d.4](../d.4%20Deep%20Learning/d.4%20Deep%20Learning.md).

**База:** [d.4 Deep Learning](../d.4%20Deep%20Learning/d.4%20Deep%20Learning.md) (гл. 33–39) · [d.0](../d.0%20Градиент%20и%20правило%20цепочки.md)

## Карта handbook ↔ папки

| гл. | Папка | Сайт | Теория | Практика |
|:---:|:---|:---|:---|:---|
| **40** | [d.5.40](d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer/d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer.md) | [sequences](https://mlhandbook-production.up.railway.app/parts/deep-learning/sequences.html) | §0–§11 | *(нет)* |
| **41** | [d.5.41](d.5.41%20Свёрточные%20сети%20CNN/d.5.41%20Свёрточные%20сети%20CNN.md) | [cnn](https://mlhandbook-production.up.railway.app/parts/deep-learning/cnn.html) | §0–§10 | *(нет)* |
| **42** | [d.5.42](d.5.42%20Transfer%20learning/d.5.42%20Transfer%20learning.md) | [transfer-learning](https://mlhandbook-production.up.railway.app/parts/deep-learning/transfer-learning.html) | §0–§7 | *(нет)* |
| **43** | [d.5.43](d.5.43%20Обучение%20представлений%20и%20metric%20learning/d.5.43%20Обучение%20представлений%20и%20metric%20learning.md) | [representation-learning](https://mlhandbook-production.up.railway.app/parts/deep-learning/representation-learning.html) | §0–§7 | *(нет)* |
| **44** | [d.5.44](d.5.44%20Оптимизация%20нейросетей%20сжатие/d.5.44%20Оптимизация%20нейросетей%20—%20дистилляция%20квантование%20прунинг.md) | [nn-optimization](https://mlhandbook-production.up.railway.app/parts/deep-learning/nn-optimization.html) | §0–§7 | *(нет)* |
| **45** | [d.5.45](d.5.45%20Тонкости%20обучения%20нейросетей/d.5.45%20Тонкости%20обучения%20нейросетей.md) | [training-tricks](https://mlhandbook-production.up.railway.app/parts/deep-learning/training-tricks.html) | §0–§9 | *(нет)* |

## Порядок чтения (рекомендация)

1. **40** — если цель NLP / сессионные рекомы  
2. **43** — эмбеддинги и поиск (NLP + recsys)  
3. **42** — fine-tune BERT / ResNet  
4. **45** — когда учишь или fine-tune глубокую модель  
5. **41** — vision / мультимодальные рекомы  
6. **44** — вывод в прод (после того как модель уже учится)

## Связь с d.4

| Нужно | Куда |
|:---|:---|
| MLP, loss, цикл обучения | [d.4.33–39](../d.4%20Deep%20Learning/d.4%20Deep%20Learning.md) |
| Затухающий градиент, σ, softmax | [d.4.34](../d.4%20Deep%20Learning/d.4.34%20Функции%20активации/d.4.34%20Функции%20активации.md) |
| Инициализация, BN, Adam, warmup (база) | [d.4.36](../d.4%20Deep%20Learning/d.4.36%20Оптимизация%20и%20обучение%20в%20DL/d.4.36%20Оптимизация%20и%20обучение%20в%20DL.md) |
| Аугментации, Dropout | [d.4.37](../d.4%20Deep%20Learning/d.4.37%20Регуляризация%20в%20DL/d.4.37%20Регуляризация%20в%20DL.md) |

Дальше по handbook — блок **«Специализация»** (отдельные конспекты по мере появления).