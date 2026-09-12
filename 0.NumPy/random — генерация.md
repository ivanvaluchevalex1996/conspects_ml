---

## 📌 Одна фраза

> В NumPy «случайность» — это **псевдослучайная цепочка**: равномерная (`rand` / `uniform` / `randint`), нормальная (`randn` / `normal`), перемешивание и выборка (`shuffle` / `permutation` / `choice`), а `seed` делает её **повторяемой**.

---

## 🔷 seed — воспроизводимость

`np.random.seed(число)` фиксирует старт генератора. Один и тот же seed → одна и та же последовательность.

```python
np.random.seed(42)
print(np.random.rand(3))
# [0.37454012 0.95071431 0.73199394]  — всегда так после seed(42)

np.random.seed(100)
print(np.random.rand(3))
# [0.54340494 0.27836939 0.42451759]  — другой seed → другие числа
```

Без seed — каждый запуск другие числа.  
После `seed(42)` цепочка идёт дальше: следующий `rand` даст **не** те же три, а следующие. Чтобы снова те же — снова `seed(42)`.

### Зачем / в ML

| зачем | смысл |
|:---|:---|
| отладка | баг и метрики повторяются |
| сравнение моделей | отличие из‑за идеи, а не «удачного» seed |
| веса / shuffle / сплит | один и тот же эксперимент при перезапуске |

> Seed делает эксперимент **воспроизводимым**, не обязательно «лучшим».

---

## 🔷 Равномерное: `rand` и `uniform`

Все значения из интервала **одинаково вероятны**.

### `np.random.rand` — только [0, 1)

Задаёшь **только форму** массива:

```python
np.random.rand()       # одно число в [0, 1)
np.random.rand(3)      # вектор длины 3
np.random.rand(2, 3)   # матрица 2×3
```

### `np.random.uniform` — любой [low, high)

```python
np.random.uniform()              # = rand(): [0, 1)
np.random.uniform(-10, 10)       # одно число в [-10, 10)
np.random.uniform(5, 15, 5)      # 5 чисел в [5, 15)
np.random.uniform(0, 1, (2, 3))  # матрица
```

|    | `rand` | `uniform` |
|:---|:---|:---|
| диапазон | всегда `[0, 1)` | любой `[low, high)` |
| аргументы | размеры | `low`, `high`, `size` |
| без параметров | одно число [0, 1) | то же |

> Верхняя граница **не входит** (`high` не включается).

---

## 🔷 Целые: `randint`

```python
np.random.randint(low, high=None, size=None)
```

Диапазон: `low <= число < high` (high **не входит**).

```python
np.random.randint(5)                 # 0..4
np.random.randint(2, 10)             # 2..9
np.random.randint(0, 10, size=(3, 4)) # матрица 3×4, числа 0..9
```

```python
# хочу 1, 2, 3
np.random.randint(1, 3)  # ❌ только 1 и 2
np.random.randint(1, 4)  # ✅ 1, 2, 3
```

|    | `randint` | `rand` / `uniform` |
|:---|:---|:---|
| тип | **целые** | **дробные** |
| диапазон | `[low, high)` | `[0,1)` или `[low, high)` |

---

## 🔷 Нормальное: `randn` и `normal`

Числа вокруг среднего, колоколообразная кривая (Гаусс).

### `np.random.randn` — среднее 0, разброс ~1

Только размерности:

```python
np.random.seed(42)
np.random.randn()       # одно число
np.random.randn(3)      # [ 0.49671415 -0.1382643   0.64768854]
np.random.randn(2, 3)   # матрица
```

Типично большинство значений между **-2** и **+2**.

### `np.random.normal` — своё среднее и разброс

```python
np.random.normal()           # = randn(): loc=0, scale=1
np.random.normal(5, 2, 3)    # среднее 5, стд 2, длина 3
np.random.normal(loc=0, scale=1, size=(2, 3))
```

|    | `randn` | `normal` |
|:---|:---|:---|
| среднее / стд | всегда 0 и 1 | любые `loc`, `scale` |
| аргументы | размеры | `loc`, `scale`, `size` |
| без параметров | одно число ~N(0,1) | то же |

> **randn** = rand + **n**ormal. Не путать с `rand` (равномерное 0..1).

---

## 🔷 Перемешивание: `shuffle` и `permutation`

|    | `shuffle` | `permutation` |
|:---|:---|:---|
| исходный массив | **меняет на месте** | **не трогает** |
| возвращает | `None` | новый массив |
| число `n` | — | массив `0..n-1` в случайном порядке |

```python
np.random.seed(42)
arr = np.array([5, 2, 18, 6, 10, 4, 52, 22, 7, 14])

np.random.shuffle(arr)
print(arr)   # исходный изменён

arr = np.array([5, 2, 18, 6, 10, 4, 52, 22, 7, 14])
permuted = np.random.permutation(arr)
# permuted — новый; arr как был

np.random.permutation(10)  # перемешанные индексы 0..9
```

---

## 🔷 Выборка: `choice`

Случайный выбор из массива или из `0..n-1`.

```python
np.random.seed(42)
arr = np.array([10, 20, 30, 40, 50])

np.random.choice(arr)                      # один элемент
np.random.choice(arr, 3)                   # 3 штуки, с повторениями
np.random.choice(arr, 3, replace=False)    # без повторений
np.random.choice(arr, 5, p=[0.4, 0.2, 0.2, 0.1, 0.1])  # свои вероятности
```

| параметр | смысл |
|:---|:---|
| `size` | сколько выбрать |
| `replace=True` | можно повторы (по умолчанию) |
| `replace=False` | без повторов |
| `p` | вероятности для каждого элемента (сумма = 1) |

`np.random.choice(10)` — случайное целое из `0..9` (как из `arange(10)`).

---

## 🔷 Сводная таблица

| функция | что даёт |
|:---|:---|
| `seed(n)` | зафиксировать цепочку |
| `rand(...)` | float равномерно в `[0, 1)` |
| `uniform(low, high, size)` | float равномерно в `[low, high)` |
| `randint(low, high, size)` | int в `[low, high)` |
| `randn(...)` | float ~ N(0, 1) |
| `normal(loc, scale, size)` | float ~ N(loc, scale) |
| `shuffle(a)` | перемешать `a` на месте |
| `permutation(a)` | новая перемешанная копия / индексы |
| `choice(a, size, ...)` | выборка из `a` |

---

## 🔷 Новый API (кратко)

```python
rng = np.random.default_rng(42)
rng.random(3)              # ≈ rand
rng.uniform(5, 15, 5)      # uniform
rng.integers(0, 10, size=5) # ≈ randint
rng.standard_normal(3)     # ≈ randn
rng.normal(5, 2, 3)        # normal
rng.shuffle(arr)
rng.permutation(10)
rng.choice(arr, 3, replace=False)
```

Старый `np.random.seed` + `rand` / `randn` в курсах всё ещё основной.

---

## ✅ Коротко запомнить

| # | Правило |
|:---|:---|
| 1 | `seed` → те же «случайные» числа при перезапуске |
| 2 | `rand` = uniform на `[0,1)`; `uniform` — любой интервал |
| 3 | `randint`: high **не входит** |
| 4 | `randn` = N(0,1); `normal` = своё среднее и стд |
| 5 | `shuffle` портит оригинал; `permutation` — копия |
| 6 | `choice` — выборка; `replace=False` без повторов |

