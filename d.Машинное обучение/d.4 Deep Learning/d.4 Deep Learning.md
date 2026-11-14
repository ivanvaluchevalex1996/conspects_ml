# d.4 Deep Learning

Порядок как в роадмапе / лекциях: сеть → оптимизация → регуляризация.
База градиента «с нуля»: [d.0](../d.0%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%20%D0%B8%20%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%BE%20%D1%86%D0%B5%D0%BF%D0%BE%D1%87%D0%BA%D0%B8.md#0-%D0%B7%D0%B0%D1%87%D0%B5%D0%BC-%D1%8D%D1%82%D0%BE-%D0%B2%D1%81%D1%91).

## Карта раздела

| # | Файл | О чём |
|:---|:---|:---|
| d.4.1 | [d.4.1](d.4.1%20Полносвязные%20нейронные%20сети/d.4.1%20Полносвязные%20нейронные%20сети.md) | MLP, активации, backprop; handbook [гл.33](d.4.1%20Полносвязные%20нейронные%20сети/practice/handbook_gl33/README.md), [гл.34](d.4.1%20Полносвязные%20нейронные%20сети/practice/handbook_gl34/README.md), [гл.35](d.4.1%20Полносвязные%20нейронные%20сети/practice/handbook_gl35/README.md) |
| d.4.2 | [d.4.2](d.4.2%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/d.4.2%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F.md); handbook [гл.36](d.4.2%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/practice/handbook_gl36/README.md) | SGD, Momentum, Adam, LR, батчи |
| d.4.3 | [d.4.3](d.4.3%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20Deep%20Learning/d.4.3%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20Deep%20Learning.md); [гл.37](d.4.3%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20Deep%20Learning/practice/handbook_gl37/README.md) | Нормализация, dropout, BatchNorm, early stop… |
| d.4.3.1 | [d.4.3.1](d.4.3%20Регуляризация%20в%20Deep%20Learning/d.4.3.1%20Пример%20—%20нормализация%20и%20один%20шаг%20обучения.md) | пример: нормализация входа, один шаг |
| d.4.3.2 | [d.4.3.2](d.4.3%20Регуляризация%20в%20Deep%20Learning/d.4.3.2%20Пример%20—%20зачем%20BatchNorm.md) | пример: зачем BatchNorm (W¹, h, W²) |
| d.4.3.3 | [d.4.3.3](d.4.3%20Регуляризация%20в%20Deep%20Learning/d.4.3.3%20Пример%20—%20Dropout%20и%20чем%20он%20отличается%20от%20ReLU.md) | пример: Dropout vs ReLU (3 нейрона) |
| d.4.4 | [d.4.4](d.4.4%20Разбор%20backword%20и%20простой%20нейросети/d.4.4%20Разбор%20backword%20и%20простой%20нейросети.md) | micrograd (Карпати): backprop руками, MLP с нуля; ноутбук по шагам |

## Связь с соседними разделами

| Нужно | Куда |
|:---|:---|
| Градиент, цепочка, шаг α | [d.0](../d.0%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%20%D0%B8%20%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%BE%20%D1%86%D0%B5%D0%BF%D0%BE%D1%87%D0%BA%D0%B8.md) |
| Loss / эмпирический риск | [d.1.2](../d.1%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%BC%D0%BB/d.1.2%20Loss%20%D0%B8%20%D1%8D%D0%BC%D0%BF%D0%B8%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%80%D0%B8%D1%81%D0%BA.md) |
| Линейная модель + MSE/SGD | [d.2.1.4](../d.2%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B/d.2.1%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8/d.2.1.4%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%20MSE%20%D0%B8%20SGD%20%D0%B4%D0%BB%D1%8F%20%D0%BB%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%BE%D0%B9%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) |
| Classic ML | [d.3](../d.3%20Classic%20ML/d.3%20Classic%20ML.md) |

PDF лекции по оптимизации/регуляризации лежит в корне `d.Машинное обучение/` — при желании можно потом перенести в `d.4/materials/`.

## Практика PyTorch (курс Дубинина)

Смысл — здесь в `d.4.x`. Код — [`pytorch/pytorch дубинин`](../../../учеба%20мл/pytorch/pytorch%20дубинин/0_как_учить_pytorch.md) (видео). Практика handbook на сайте: гл.38 [`handbook_gl38`](../../../учеба%20мл/pytorch/pytorch%20handbook/handbook_gl38/README.md), гл.39 [`handbook_gl39`](../../../учеба%20мл/pytorch/pytorch%20handbook/handbook_gl39/README.md). Гайд курса = `0_как_учить_pytorch.md`.

| Конспект | Что открыть в PyTorch |
| --- | --- |
| **d.4.1** §5–11 (MLP, активации, loss, обучение) | handbook гл.33 — [`handbook_gl33/`](d.4.1%20Полносвязные%20нейронные%20сети/practice/handbook_gl33/README.md); гл.34 — [`practice/handbook_gl34/`](d.4.1%20Полносвязные%20нейронные%20сети/practice/handbook_gl34/README.md); курс — [`08/`](../../../учеба%20мл/pytorch/pytorch%20дубинин/08/08_активации_потери_оптимизатор.ipynb), [`09/`](../../../учеба%20мл/pytorch/pytorch%20дубинин/09/09_классы_нейросетей.ipynb); формулы softmax+CE — [`homework…/формулы-конспект-код.md`](../../../учеба%20мл/homework_linear_models_and_knn/формулы-конспект-код.md); loss/метрики — `d.1.2`, `d.3.1`; цикл — видео 11 |
| **d.4.2** (SGD, Adam, lr) | [`handbook_gl36/`](d.4.2%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/practice/handbook_gl36/README.md); `08/` блок 5; видео 12 |
| **d.4.3** (нормализация, dropout, BN, early stop) | [`handbook_gl37/`](d.4.3%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20Deep%20Learning/practice/handbook_gl37/README.md); [`07/`](../../../учеба%20мл/pytorch/pytorch%20дубинин/07/07_transforms_v2.ipynb); `14`–`16` |
| **d.4.4** (micrograd / backprop руками) | смысл → [`08/`](../../../учеба%20мл/pytorch/pytorch%20дубинин/08/08_активации_потери_оптимизатор.ipynb) блок 5 (`backward`/`step`) |
| батчи / Dataset | [`04/`](../../../учеба%20мл/pytorch/pytorch%20дубинин/04/04_dataset_dataloader_1.ipynb)–[`06/`](../../../учеба%20мл/pytorch/pytorch%20дубинин/06/06_dataset_dataloader_3.ipynb) (+ отсылка в intro `06/`) |
| train/val/test, переобучение | видео 2; конспекты `d.1.4`, `d.3.2` |
| сквозной проект | [`project/fashion_mnist.ipynb`](../../../учеба%20мл/pytorch/pytorch%20дубинин/project/fashion_mnist.ipynb) |
| сайт **гл.38** PyTorch intro | [`handbook_gl38`](../../../учеба%20мл/pytorch/pytorch%20handbook/handbook_gl38/README.md) → практика на сайте; теория в коде курса `03/`–`10/` |
| сайт **гл.39** PyTorch на практике | [`handbook_gl39/README`](../../../учеба%20мл/pytorch/pytorch%20handbook/handbook_gl39/README.md) (статус + Deep-ML; проект — `pytorch дубинин/project`); курс `04/`–`14/` |
