# d.5.41 · Свёрточные сети (CNN)

**Конспект к ML Handbook · [гл. 41 — CNN на сайте](https://mlhandbook-production.up.railway.app/parts/deep-learning/cnn.html)** · [README.md](./README.md) · [карта d.5](../d.5%20advanced%20Deep%20Learning.md)

**Метки:** 🔵 **ментор (handbook)** — что учить по программе · 🟠 **Дубинин (PyTorch)** — видео 17–23 · без метки — твой конспект (§0, §8, NLP/recsys).

**Легенда**

| Источник | Как узнать в файле | Ссылка |
| --- | --- | --- |
| 🔵 **ML Handbook (ментор)** | `*(handbook 41.x)*` в заголовке §2–§7 · таблица ниже | [cnn.html](https://mlhandbook-production.up.railway.app/parts/deep-learning/cnn.html) |
| 🟠 **Дубинин · PyTorch** | таблица «Видео 17–23» · строка `🟠` в начале § | [плейлист](https://www.youtube.com/playlist?list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1) · [обзор CNN в репо](../../../../pytorch/pytorch%20дубинин/17-23_cnn/17-23_cnn_обзор.md) |
| **Конспект** | §0, §1, §8, §9–§10 | связки с d.5.40 / recsys, шпаргалка |

Превью 🔵/🟠: **Ctrl+K V** ([`.vscode/conspect-sources.css`](../../../../.vscode/conspect-sources.css)) — если в CSS добавлены стили для 🟠.

---

#### 🔵 **▸ Handbook (ментор)** · карта гл. 41

| § handbook | На сайте | Якорь в **этом** конспекте |
|:---:|:---|:---|
| 41.1 | свёртка, локальность, sharing | [§2](#2-свёртка-handbook-411) |
| 41.2 | каналы, feature maps | [§3](#3-каналы-и-карты-признаков-handbook-412) |
| 41.3 | padding, stride, размер | [§4](#4-padding-и-stride-handbook-413) |
| 41.4 | pooling | [§5](#5-пулинг-handbook-414) |
| 41.5 | сборка CNN | [§6](#6-из-чего-собрана-cnn-handbook-415) |
| 41.6 | аугментации | [§7](#7-аугментация-handbook-416) |

---

#### 🟠 **▸ Дубинин (PyTorch)** · видео 17–23 · [карта курса](../../../../pytorch/pytorch%20дубинин/0_как_учить_pytorch.md)

| № | Тема | YouTube | § конспекта |
| ---: | --- | --- | --- |
| 17 | Свёрточные слои, `Conv2d`, BCHW | [смотреть](https://www.youtube.com/watch?v=OKx1GsT1q9c&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=17) | [§2](#2-свёртка-handbook-411)–[§4](#4-padding-и-stride-handbook-413) |
| 18 | Сборка CNN (Conv → ReLU → …) | [смотреть](https://www.youtube.com/watch?v=gS48_UUq7VU&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=18) | [§6](#6-из-чего-собрана-cnn-handbook-415) |
| 19 | MaxPool, AvgPool | [смотреть](https://www.youtube.com/watch?v=8KzWA8v_uIU&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=19) | [§5](#5-пулинг-handbook-414) |
| 20 | VGG | [смотреть](https://www.youtube.com/watch?v=ss1oHfTeqic&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=20) | [§6](#6-из-чего-собрана-cnn-handbook-415) (эрудиция) |
| 21 | ResNet | [смотреть](https://www.youtube.com/watch?v=sHpw-8uWZGw&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=21) | [§6](#6-из-чего-собрана-cnn-handbook-415) · [d.5.45](../d.5.45%20Тонкости%20обучения%20нейросетей/d.5.45%20Тонкости%20обучения%20нейросетей.md) |
| 22 | U-Net | [смотреть](https://www.youtube.com/watch?v=atjA2iEpk1c&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=22) | [§6](#6-из-чего-собрана-cnn-handbook-415) |
| 23 | Transfer Learning | [смотреть](https://www.youtube.com/watch?v=M0iB56Vwy64&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=23) | [d.5.42](../d.5.42%20Transfer%20learning/d.5.42%20Transfer%20learning.md) |

**Практика handbook (сайт):** [practice/](./practice/README.md) · [handbook_gl41_практика.ipynb](./practice/handbook_gl41_практика.ipynb)

База: линейный слой, ReLU, softmax → [d.4.33](../../d.4%20Deep%20Learning/d.4.33%20Нейрон%20и%20полносвязная%20сеть/d.4.33%20Нейрон%20и%20полносвязная%20сеть.md), [d.4.34](../../d.4%20Deep%20Learning/d.4.34%20Функции%20активации/d.4.34%20Функции%20активации.md). Аугментации как регуляризация → [d.4.37](../../d.4%20Deep%20Learning/d.4.37%20Регуляризация%20в%20DL/d.4.37%20Регуляризация%20в%20DL.md) §2.3 · transforms в коде — Дубинин [видео 7](https://www.youtube.com/watch?v=9ZnQch_O6xE) + [§7](#7-аугментация-handbook-416).

> **Preview:** формулы в `$$`; в тексте — W_out, C_in, ŷ.

---

## 0. Зачем CNN (не для NLP/recsys в первую очередь, но обязательна на собесе)

*(**конспект**, не отдельный § handbook — твой контекст NLP/recsys.)*

Картинка 224×224×3 — **~150k** входов. Полносвязный слой на всё изображение → **миллиарды** весов и мгновенное переобучение. Плюс MLP **не видит** структуру: пиксель в углу и в центре для него «просто разные координаты».

**CNN** используют две идеи изображений:

1. **Локальность** — смысл в **окрестности** пикселя.
2. **Повторяемость паттернов** — граница/текстура может быть **где угодно** на кадре.

Для **NLP** основной зритель — трансформер ([d.5.40](../d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer/d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer.md)); для **recsys** — эмбеддинги ([d.5.43](../d.5.43%20Обучение%20представлений%20и%20metric%20learning/d.5.43%20Обучение%20представлений%20и%20metric%20learning.md)). CNN всё равно нужны: **мультимодальность** (текст + картинка товара), контентные рекомы, ViT как «CNN-наследник».

---

## 1. План главы

Свёртка → каналы → размер карты → пулинг → типовая сеть → аугментации → [§10 шпаргалка](#10-шпаргалка).

---

## 2. Свёртка *(handbook 41.1)*

> **🔵 Ментор:** [41.1](https://mlhandbook-production.up.railway.app/parts/deep-learning/cnn.html) · **🟠 Дубинин:** [видео 17](https://www.youtube.com/watch?v=OKx1GsT1q9c&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=17)

**Свёртка** — маленькое ядро (фильтр) k×k **скользит** по изображению; в каждой позиции — взвешенная сумма пикселей под окном.

| Идея | Смысл |
| --- | --- |
| **Локальное окно** | нейрон смотрит на k×k, не на всю картинку — как зрение |
| **Weight sharing** | **один** фильтр на **все** позиции — границу учим один раз, находим везде → **трансляционная инвариантность** |

Классические ручные фильтры (Собель) — вертикальные/горизонтальные границы; в обучаемой CNN фильтры **подбирает** SGD.

---

## 3. Каналы и карты признаков *(handbook 41.2)*

> **🔵 Ментор:** [41.2](https://mlhandbook-production.up.railway.app/parts/deep-learning/cnn.html) · **🟠 Дубинин:** [видео 17](https://www.youtube.com/watch?v=OKx1GsT1q9c&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=17)

RGB → **3 канала** входа. Один фильтр 3×k×k покрывает **все** входные каналы сразу.

- **C_in** — каналов на входе слоя
- **C_out** — число **фильтров** = число **карт признаков** (feature maps)

PyTorch: `nn.Conv2d(C_in, C_out, kernel_size=3, padding=1)`  
Формат тензора: **(батч, каналы, высота, ширина)** — BCHW.

**Иерархия признаков (суть CNN):** ранние слои — границы, углы; глубокие — части, объекты. Это и есть **representation learning** — см. [d.5.43](../d.5.43%20Обучение%20представлений%20и%20metric%20learning/d.5.43%20Обучение%20представлений%20и%20metric%20learning.md).

---

## 4. Padding и stride *(handbook 41.3)*

> **🔵 Ментор:** [41.3](https://mlhandbook-production.up.railway.app/parts/deep-learning/cnn.html) · **🟠 Дубинин:** [видео 17](https://www.youtube.com/watch?v=OKx1GsT1q9c&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=17)

| Параметр | Зачем |
| --- | --- |
| **padding** | дополнить края нулями; `padding=1` при ядре 3×3 — **сохранить** H×W |
| **stride** | шаг окна; `stride=2` — карта **вдвое** меньше (альтернатива пулингу) |

Размер по одной оси (высота или ширина):

$$
\Large
W_{\text{out}} = \left\lfloor \frac{W - k + 2p}{s} \right\rfloor + 1
$$

где k — размер ядра, p — padding, s — stride.

---

## 5. Пулинг *(handbook 41.4)*

> **🔵 Ментор:** [41.4](https://mlhandbook-production.up.railway.app/parts/deep-learning/cnn.html) · **🟠 Дубинин:** [видео 19](https://www.youtube.com/watch?v=8KzWA8v_uIU&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=19)

**Pooling** сжимает карту: окно 2×2 → одно число.

| Тип | Правило |
| --- | --- |
| **MaxPool** | максимум в окне (частый выбор) |
| **AvgPool** | среднее |

Эффект: меньше размер, чуть **устойчивее** к малым сдвигам, шире рецептивное поле следующих слоёв.

---

## 6. Из чего собрана CNN *(handbook 41.5)*

> **🔵 Ментор:** [41.5](https://mlhandbook-production.up.railway.app/parts/deep-learning/cnn.html) · **🟠 Дубинин:** [18](https://www.youtube.com/watch?v=gS48_UUq7VU&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=18) · [20–22](https://www.youtube.com/playlist?list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1) (VGG / ResNet / U-Net)

Типовый скелет:

$$\Large \text{вход} \to [\,\text{Conv} \to \text{ReLU} \to \text{Pool}\,] \times N \to \text{Flatten} \to \text{FC} \to \text{голова}$$

**Почему Conv дешевле FC** (главный аргумент на собесе):

| Слой | Параметры Conv2d(3→16, 3×3) | Linear(32·32·3 → 16) |
| --- | ---: | ---: |
| масштаб | **~сотни** (не зависят от H×W!) | **~десятки тысяч** |

`Conv2d` — одно ядро на все позиции; `Linear` — каждый пиксель в отдельный вес.

**Обучение:** тот же цикл, что в [d.4.39](../../d.4%20Deep%20Learning/d.4.39%20PyTorch%20практика/practice/README.md): `train`/`eval`, CE для классификации.

**Архитектуры (эрудиция):** LeNet → AlexNet → VGG (стек 3×3) → **ResNet** (residual y=F(x)+x) → EfficientNet. Задачи: YOLO/Faster R-CNN (детекция), U-Net (сегментация). С ~2020 ViT конкурирует с CNN, но CNN быстрее при малых данных.

**Рецептивное поле** — сколько пикселей входа влияет на один нейрон глубокого слоя; растёт с глубиной → глубокие слои «видят» крупное.

---

## 7. Аугментация *(handbook 41.6)*

> **🔵 Ментор:** [41.6](https://mlhandbook-production.up.railway.app/parts/deep-learning/cnn.html) · **🟠 Дубинин:** [видео 7 — Transforms](https://www.youtube.com/watch?v=9ZnQch_O6xE&list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1&index=8)

Поворот, отражение, кроп, яркость — **метка не меняется**, данных «как бы» больше. `torchvision.transforms`: `RandomHorizontalFlip`, `Normalize` под ImageNet — стандарт при [transfer learning](../d.5.42%20Transfer%20learning/d.5.42%20Transfer%20learning.md).

---

## 8. NLP / recsys — где CNN всплывает

| Область | Роль CNN |
| --- | --- |
| NLP (legacy) | TextCNN — свёртка по n-граммам; сейчас реже трансформера |
| Мультимодальные рекомы | эмбеддинг картинки товара (ResNet → вектор) |
| Поиск по изображению | тот же эмбеддинг + metric learning |

---

## 9. Практика (handbook, позже)

Deep-ML: свёртка NumPy; Conv2d shape; MNIST CNN accuracy ≥ 0.99. Документация: `nn.Conv2d`, `MaxPool2d`, `BatchNorm2d`, `torchvision`.

---

## 10. Шпаргалка

- **Conv:** локальное окно + **общие** веса → мало параметров, инвариантность к сдвигу паттерна.
- **BCHW:** batch, channels, height, width.
- **padding** сохраняет размер; **stride** и **pool** уменьшают.
- **Иерархия:** границы → … → объекты.
- **vs FC:** на больших картинках FC — переобучение и лишние веса.
- **ResNet / ViT** — знать названия; residual → [d.5.45](../d.5.45%20Тонкости%20обучения%20нейросетей/d.5.45%20Тонкости%20обучения%20нейросетей.md) §5.

Назад: [d.5.40](../d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer/d.5.40%20Последовательности%20RNN%20LSTM%20GRU%20Transformer.md) · Дальше: [d.5.42](../d.5.42%20Transfer%20learning/d.5.42%20Transfer%20learning.md)