# d.5.42 · Transfer learning (трансферное обучение)

**🔵 ML Handbook (ментор):** [transfer-learning.html · гл. 42](https://mlhandbook-production.up.railway.app/parts/deep-learning/transfer-learning.html) · [README.md](./README.md) · [карта d.5](../d.5%20advanced%20Deep%20Learning.md)

**Метки:** 🔵 **ментор (handbook)** · 🟣 **лекция YouTube** · 🟠 **Дубинин (PyTorch)** · без метки — конспект (§0, §5 recsys, шпаргалка).

#### 🔵 **▸ Handbook (ментор)** · карта гл. 42

| § handbook | На сайте | Якорь |
|:---:|:---|:---|
| 42.1 | универсальные ранние признаки | [§1](#1-почему-работает-handbook-421) |
| 42.2 | feature extraction vs fine-tuning | [§2](#2-два-режима-handbook-422) |
| 42.3 | сколько размораживать | [§3](#3-таблица-данные--похожесть-handbook-423) |
| 42.4 | NLP, LoRA | [§4](#4-nlp-и-lora-handbook-424) |

---

#### 🟣 **▸ Лекция (YouTube)** · [Transfer Learning](https://www.youtube.com/watch?v=oLpREso27Zw) (Deep Learning School)

Теория трансфера поверх handbook — **не** сайт ментора, **не** курс Дубинина.

| Тема в конспекте | Смысл лекции |
| --- | --- |
| [§1](#1-почему-работает-handbook-421) | зачем претрейн, ранние vs поздние слои |
| [§2](#2-два-режима-handbook-422) | feature extraction vs fine-tuning |
| [§3](#3-таблица-данные--похожесть-handbook-423) | сколько данных, похожесть домена |
| [§4](#4-nlp-и-lora-handbook-424) | NLP / адаптеры (если есть в ролике) |

#### 🟠 **▸ Дубинин (PyTorch)** · плейлист [«Нейросети с PyTorch»](https://www.youtube.com/playlist?list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1) · [видео 23 — Transfer Learning](https://www.youtube.com/watch?v=M0iB56Vwy64&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=23)

Та же **практика по смыслу**, что handbook: датасет **пчёлы / муравьи** (статья [transfer learning в доке PyTorch](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)), сравнение **с нуля vs transfer**, заморозка **`features`**, учится **`classifier`**, `requires_grad`, ~**10 эпох**. Модель — **своя CNN** из курса (`features` + `classifier`), не `ResNet18.layer4` как на сайте ментора.

| Время | О чём |
| --- | --- |
| [0:00](https://www.youtube.com/watch?v=M0iB56Vwy64&t=0) | введение |
| [0:42](https://www.youtube.com/watch?v=M0iB56Vwy64&t=42) | transfer при классификации (в т.ч. идея `ResNet`) |
| [5:44](https://www.youtube.com/watch?v=M0iB56Vwy64&t=344) | **код:** датасет, обучение с нуля vs transfer |
| ~6:20 | два класса: пчёлы и муравьи |
| ~12:50+ | `features` заморожен, учится классификатор |

Полный код в ролике + ноутбук курса (ссылка в описании видео). У себя под **handbook / ментор:** [handbook_gl42_hymenoptera_решения.ipynb](./practice/handbook_gl42_hymenoptera_решения.ipynb) (**ResNet-18**, шаги 1–2–3). Обзор CNN-блока: [17–23](../../../../pytorch/pytorch%20дубинин/17-23_cnn/17-23_cnn_обзор.md) · [§6](#6-практика-handbook--мини-проект).

**Практика handbook (сайт):** [practice/](./practice/README.md) · [handbook_gl42_практика.ipynb](./practice/handbook_gl42_практика.ipynb)

CNN-база: [d.5.41](../d.5.41%20Свёрточные%20сети%20CNN/d.5.41%20Свёрточные%20сети%20CNN.md). Трансформеры: [d.5.40](../d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer/d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer.md). Маленький lr, scheduler → [d.4.36](../../d.4%20Deep%20Learning/d.4.36%20Оптимизация%20и%20обучение%20в%20DL/d.4.36%20Оптимизация%20и%20обучение%20в%20DL.md).

---

## 0. Зачем тебе (NLP / recsys)

> **🟣 Лекция:** [Transfer Learning](https://www.youtube.com/watch?v=oLpREso27Zw) · **🔵 Ментор:** [гл. 42](https://mlhandbook-production.up.railway.app/parts/deep-learning/transfer-learning.html)

**Правило продакшена:** почти **никогда** не учат BERT/ResNet с нуля на своих данных.

| Направление | Типичный transfer |
| --- | --- |
| **NLP** | `bert-base`, `ruRoberta`, LLM + fine-tune / LoRA на свою разметку |
| **Recsys (контент)** | ResNet/EfficientNet на фото товара → вектор в двухбашенной модели |
| **Recsys (текст)** | эмбеддинг описания через предобученный трансформер |

Это глава про **как** заморозить, что доучить, какой lr — без этого fine-tune «убьёт» претрейн.

---

## 1. Почему работает *(handbook 42.1)*

Глубокая сеть учит **ступени абстракции**:

| Глубина | Типичное (vision) |
| --- | --- |
| ранние слои | границы, цвет, текстуры — **универсально** |
| поздние | части, объекты — **специфика** задачи |

Перенос: **тело** сети уже извлекает полезные признаки; на своей задаче меняют **голову** и чуть подкручивают верхние слои.

В **тексте** то же: нижние слои трансформера — морфология/синтаксис; верхние — под задачу (тональность, NER).

---

## 2. Два режима *(handbook 42.2)*

| Режим | Что делаем | Когда |
| --- | --- | --- |
| **Feature extraction** | `requires_grad=False` на теле; учим **только новую голову** | мало данных |
| **Fine-tuning** | размораживаем часть/всё; **малый lr**, чтобы не «забить» признаки | больше данных, нужен выигрыш в качестве |

**PyTorch (идея):**

```python
for p in model.parameters():
    p.requires_grad = False
model.fc = nn.Linear(model.fc.in_features, num_classes)  # голова учится
opt = torch.optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=1e-3)
```

Vision: `torchvision.models.resnet18(weights=DEFAULT)` → заменить `fc`.

**Fine-tune с разными lr (param groups):**

| Группа | lr |
| --- | --- |
| новая голова | ~1e-3 |
| предобученные блоки (напр. `layer4`) | ~1e-5 |

---

## 3. Таблица: данные × похожесть *(handbook 42.3)*

| Данных | Задача похожа на претрейн | Действие |
| --- | --- | --- |
| мало | да | заморозить всё, учить голову |
| мало | нет | заморозить ранние, доучить поздние |
| много | да | fine-tune всего с малым lr |
| много | нет | fine-tune всего (или с нуля, но с претрейном быстрее) |

**Ошибка новичка:** большой lr на всей BERT → катастрофическое забывание претрейна.

**Нормализация входа:** для ImageNet-моделей — те же mean/std, что при обучении ResNet.

---

## 4. NLP и LoRA *(handbook 42.4)*

**Стандарт NLP:**

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
# training loop, lr ~ 2e-5
```

**LoRA / PEFT:** LLM огромные — полный fine-tune дорог. Замораживают базу, учат **низкоранговые адаптеры** к весам. Память и время ↓, качество часто близко к полному fine-tune. Связь со сжатием → [d.5.44](../d.5.44%20Оптимизация%20нейросетей%20сжатие/d.5.44%20Оптимизация%20нейросетей%20—%20дистилляция%20квантование%20прунинг.md) §доп.

---

## 5. Recsys: two-tower и претрейн

Типичный пайплайн:

1. Предобученный **текстовый** энкодер → эмбеддинг названия/описания.
2. Предобученная **vision** сеть → эмбеддинг фото.
3. ID пользователя/товара → `nn.Embedding` ([d.5.43](../d.5.43%20Обучение%20представлений%20и%20metric%20learning/d.5.43%20Обучение%20представлений%20и%20metric%20learning.md)).
4. Обучение **поверх** (dot product, битовая кросс-энтропия) — transfer на каждой башне.

---

## 6. Практика (handbook · мини-проект)

> **🔵 Ментор:** [transfer-learning.html · практика](https://mlhandbook-production.up.railway.app/parts/deep-learning/transfer-learning.html) · **🟠 Дубинин:** [видео 23](https://www.youtube.com/watch?v=M0iB56Vwy64) · **код у себя:** [practice/](./practice/README.md) · [handbook_gl42_практика.ipynb](./practice/handbook_gl42_практика.ipynb)

**Датасет:** [Hymenoptera](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) (пчёлы / муравьи, ~240 train). **Модель:** `torchvision` **ResNet-18**, веса ImageNet.

| ☐ | Шаг handbook | Что делаешь | Теория |
|---|--------------|-------------|--------|
| ☐ | **1. Feature extraction** | заморозить всё (`requires_grad=False`), заменить `fc` на 2 класса, учить **только голову**, записать **accuracy** на val | [§2](#2-два-режима-handbook-422) |
| ☐ | **2. Fine-tuning** | разморозить **`model.layer4`**, дообучить с **`lr=1e-4`** (handbook), сравнить с шагом 1 | [§2](#2-два-режима-handbook-422) · [§3](#3-таблица-данные--похожесть-handbook-423) |
| ☐ | **3. Аугментации** | `RandomResizedCrop`, `RandomHorizontalFlip`, **`Normalize`** — mean/std **ImageNet** (как у ResNet) | [§3](#3-таблица-данные--похожесть-handbook-423) |

**Официальный эталон кода:** [PyTorch · Transfer Learning tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) (то, на что ссылается handbook).

**У себя в конспекте:** [handbook_gl42_практика.ipynb](./practice/handbook_gl42_практика.ipynb) (фрагменты) → **[handbook_gl42_hymenoptera_решения.ipynb](./practice/handbook_gl42_hymenoptera_решения.ipynb)** (полный train/val, **ResNet-18**, шаги handbook 1–2–3).

| Источник | Код практики |
| --- | --- |
| **🔵 handbook / ноутбук** | `ResNet18`, `fc`, fine-tune **`layer4`**, аугментации ImageNet |
| **🟠 Дубинин, [видео 23](https://www.youtube.com/watch?v=M0iB56Vwy64&t=344)** | тот же **hymenoptera_data**, своя сеть **`features` + `classifier`**, сравнение с обучением с нуля |
| **PyTorch tutorial** | эталон, близко к handbook | Цикл обучения: [d.4.35](../../d.4%20Deep%20Learning/d.4.35%20Backpropagation/d.4.35%20Backpropagation.md), DataLoader/transforms: Дубинин `04–07`, `11`.

**Два этапа во времени (если val после шага 1 слабый):** сначала только `fc`, потом `layer4` + новый `optimizer` — см. обсуждение param groups в [§2](#2-два-режима-handbook-422).

---

## 7. Шпаргалка

- С нуля на ImageNet — **не делают**; берут веса + свою голову.
- **Заморозка** = нет градиента в теле.
- **Fine-tune** = маленький lr на предобученное.
- **NLP** = Hugging Face + 2e-5 порядок.
- **LoRA** = дешёвый fine-tune LLM.

Назад: [d.5.41](../d.5.41%20Свёрточные%20сети%20CNN/d.5.41%20Свёрточные%20сети%20CNN.md) · Дальше: [d.5.43](../d.5.43%20Обучение%20представлений%20и%20metric%20learning/d.5.43%20Обучение%20представлений%20и%20metric%20learning.md)