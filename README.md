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

## Окружение (один Python на весь компьютер)

Библиотеки ставятся **не в папку проекта**, а в **глобальный Python 3.12**. Тогда ноутбуки и скрипты работают в `conspects_ml`, `python_base`, `pytorch` и в любом новом репозитории с тем же интерпретатором в Cursor.

| Что | Где |
|-----|-----|
| Список пакетов | `requirements.txt` в этом репо |
| Интерпретатор в Cursor | `.vscode/settings.json` → `${env:LOCALAPPDATA}/Programs/Python/Python312/python.exe` |
| Папка `.venv` | **не нужна** — в Git её нет (см. `.gitignore`). Локальную `.venv` можно **удалить** |

Путь `${env:LOCALAPPDATA}` не привязан к имени пользователя (`Иван`, `HUAWEI` и т.д.) — только к стандартной установке Python 3.12 с [python.org](https://www.python.org/downloads/) в профиль Windows.

### Быстрое восстановление после клона (или после «всё сломалось»)

**1. Python 3.12** (если ещё нет на машине)

- Скачай установщик с [python.org](https://www.python.org/downloads/).
- В мастере включи **Add python.exe to PATH**.
- Проверка в PowerShell: `py -3.12 --version`

**2. Клон репозиториев** (для раскладки Desktop как в начале README — **все соседние папки**, иначе ссылки между конспектами и ноутбуками не сойдутся)

```powershell
cd $env:USERPROFILE\Desktop   # или куда кладёшь проекты
git clone <url> conspects_ml
git clone <url> python_base
git clone <url> pytorch
cd conspects_ml
```

**3. Один раз установить все пакеты на компьютер** (не в `.venv`)

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup-global.ps1
```

Или вручную:

```powershell
py -3.12 -m pip install -r requirements.txt
```

Дождись окончания (torch качается долго). Повторять после каждого клона **не нужно**, если Python и пакеты на диске не удаляли.

**4. Cursor**

- Открой папку `conspects_ml` (или multi-root: `conspects_ml` + `python_base` + `pytorch`).
- **Developer: Reload Window** — подтянется интерпретатор из settings.
- В ноутбуке: **Notebook: Select Kernel** → **Python 3.12.x** → путь `...\Python312\python.exe` (не `.venv`).

**5. Чтобы везде был один интерпретатор без копирования settings**

Один раз в **User Settings** Cursor (Settings → **Python › Default: Interpreter Path**), значение:

`"${env:LOCALAPPDATA}/Programs/Python/Python312/python.exe"`

Тогда любой открытый проект по умолчанию использует тот же Python с уже установленными пакетами. Это особенно важно для **`python_base` и `pytorch`**: там нет своего `.vscode/settings.json`, только в `conspects_ml` он лежит в репозитории.

**6. Проверка**

```powershell
py -3.12 -c "import torch, numpy; print(torch.__version__, numpy.__version__)"
```

### После переустановки Windows (на GitHub только код)

Windows сносит **Python, pip-пакеты, Desktop, Cursor** — это нормально. В GitHub остаётся **код** репозиториев (`conspects_ml`, `python_base`, `pytorch` …). Порядок:

1. Поставь **Windows**, залогинься в GitHub (браузер / `gh auth login` / SSH-ключ).
2. Установи **Git for Windows** и **Cursor**. Расширения для ноутбуков и settings (из `.vscode/extensions.json`):

   ```powershell
   cd conspects_ml
   powershell -ExecutionPolicy Bypass -File .\scripts\install-cursor-extensions.ps1
   ```

   Или в Cursor: откроешь проект → «Install Recommended Extensions».
3. Установи **Python 3.12** с [python.org](https://www.python.org/downloads/) → **Add python.exe to PATH**. Проверка: `py -3.12 --version` (если `py` нет — `python --version`).
4. Клонируй репозитории **рядом на Desktop** (иначе относительные ссылки не работают):

   ```powershell
   cd $env:USERPROFILE\Desktop
   git clone <url> conspects_ml
   git clone <url> python_base
   git clone <url> pytorch
   # при необходимости: git clone <url> homework_linear_models_and_knn
   ```

5. **Один раз** поставь библиотеки на весь компьютер (хватает `requirements.txt` из `conspects_ml`):

   ```powershell
   cd $env:USERPROFILE\Desktop\conspects_ml
   powershell -ExecutionPolicy Bypass -File .\scripts\setup-global.ps1
   ```

6. В **User Settings** Cursor задай **Python › Default: Interpreter Path** = `${env:LOCALAPPDATA}/Programs/Python/Python312/python.exe` (см. шаг 5 выше в разделе «Быстрое восстановление»).
7. Cursor: **File → Add Folder to Workspace** — `conspects_ml`, `python_base`, `pytorch` (multi-root). При желании сохрани `.code-workspace`.
8. В ноутбуках: **Select Kernel** → **Python 3.12.x** (`...\Python312\python.exe`), не `.venv`.
9. Проверка: `py -3.12 -c "import torch; print('ok')"`.

- **Не нужно** снова запускать `setup-global.ps1` после обычного `git clone`, если Python и пакеты на диске не трогали.
- **Нужно снова** после каждой переустановки Windows или удаления Python 3.12.

Устаревший вариант с локальной папкой `.venv`: `scripts/setup-venv.ps1` (изоляция только для одного репо — сейчас не используем).
