# conspects_ml — конспекты и связанные проекты

Все четыре проекта лежат на рабочем столе **на одном уровне**. Относительные ссылки между ними рассчитаны на эту раскладку. Если папки положить иначе, ссылки сломаются.

## Раскладка

```text
Desktop/
  conspects_ml/                    ← этот репозиторий (конспекты, Git: origin/main)
  homework_linear_models_and_knn/  ← домашка: линейный классификатор, KNN, формулы softmax+CE
  python_base/                     ← питон-задачи (например 13_deep_ml_deep_learning.py)
  pytorch/                         ← курс Дубинина и handbook по PyTorch
    pytorch дубинин/               ← ноутбуки 03–16, 17-23_cnn, 24_amp, project, 0_как_учить_pytorch.md
```

Внутри `pytorch/` номерные папки (`03`, `04`, …) лежат **внутри** `pytorch дубинин/`, а не рядом с ним.

## Что ссылается на что

| Откуда | Куда | Пример |
|---|---|---|
| `conspects_ml/d.Машинное обучение/…` | `pytorch/pytorch дубинин/…` | `d.4.35 Backpropagation.md` → `../../../../pytorch/pytorch%20дубинин/11/11_цикл_обучения.ipynb` |
| `conspects_ml/d.Машинное обучение/…` | `homework_linear_models_and_knn/…` | `d.2.1 Линейные модели.md` → `../../../../homework_linear_models_and_knn/формулы-конспект-код.md` |
| `conspects_ml/d.Машинное обучение/d.4 Deep Learning/…` | `python_base/…` | `d.4.34 Функции активации.md` → `../../../../python_base/13_deep_ml_deep_learning.py` |
| `pytorch/pytorch дубинин/…` | `homework_linear_models_and_knn/…` | `08_активации_потери_оптимизатор.ipynb` → `../../../homework_linear_models_and_knn/формулы-конспект-код.md` |
| `pytorch/0_как_учить_pytorch.md` | `homework_linear_models_and_knn/…` | `../homework_linear_models_and_knn/формулы-конспект-код.md` |

Ссылки на «все мои конспекты в ynote» в `pytorch` указывают на папку, которой на рабочем столе нет. Это известная проблема, она не решена.

## Проекты

- **conspects_ml** — конспекты по ML и DL. Структура: `d.Машинное обучение/d.0 … d.4 Deep Learning/…`. Ноутбуки практики лежат в `practice/`.
- **homework_linear_models_and_knn** — домашка: `linear_classifer.py`, `knn.py`, `metrics.py`, `формулы-конспект-код.md`, `Linear classifier.ipynb`, `KNN.ipynb`. Своего `requirements.txt` нет, список пакетов смотреть в самом файле.
- **python_base** — задачи по Python, файлы `01_…py`–`13_…py`.
- **pytorch** — ноутбуки курса Дубинина. Все номерные ноутбуки и `project` лежат в `pytorch дубинин/`.

## Окружение

- `.venv` в репозиторий не входит (в `.gitignore`), после клона её нужно создать заново.
- Ноутбуки запускаются на Python 3.12. Для PyTorch нужен пакет `torch`, для ноутбуков — `jupyter`, `ipykernel`, `nbclient`, `nbformat`, `nbconvert`, `numpy`, `matplotlib`.
