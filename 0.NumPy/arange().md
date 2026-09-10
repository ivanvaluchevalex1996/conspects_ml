
---

## 📌 Одна фраза

> `np.arange` — **последовательность чисел** с заданным шагом: индексы картинок, точки разреза батчей, номера строк.

---

## 🔷 Что делает

```python
np.arange(stop)              →  0, 1, 2, ..., stop-1
np.arange(start, stop)       →  start, ..., stop-1  (stop не входит!)
np.arange(start, stop, step) →  start, start+step, ...  пока < stop
```

| вызов | результат |
|:---|:---|
| `np.arange(5)` | `[0, 1, 2, 3, 4]` |
| `np.arange(2, 5)` | `[2, 3, 4]` |
| `np.arange(0, 10, 3)` | `[0, 3, 6, 9]` |
| `np.arange(32, 100, 32)` | `[32, 64, 96]` |

> ⚠️ **stop не включается** — как срез `a[start:stop]`.

> 💡 Не путать с `range()` Python — `arange` сразу **numpy-массив**, удобен для индексации и `array_split`.

---

|    | `arange` | `linspace` |
|:---|:---|:---|
| шаг | фиксированный | фиксированное **число** точек |
| stop | не входит | **входит** последняя точка |
| в домашке | индексы, батчи | почти не используется |

---

## 🔷 Пример «на пальцах»

```python
num_train = 10
batch_size = 3

indices = np.arange(num_train)           # [0,1,2,3,4,5,6,7,8,9]
sections = np.arange(3, 10, 3)             # [3, 6, 9]
# array_split → [0:3], [3:6], [6:9], [9:10]
```

Последний кусок — 1 элемент (хвост).

---

## ✅ Коротко запомнить

| # | Правило |
|:---|:---|
| 1 | `arange(stop)` → 0 .. stop-1 |
| 2 | `arange(a, b, step)` → a, a+step, ... **строго меньше b** |
| 3 | fit: `arange(num_train)` + shuffle → случайный порядок |
| 4 | fit: `arange(batch, num_train, batch)` → точки для `array_split` |
| 5 | батч: `arange(shape[0])` → номера строк для `probs[rows, cols]` |
| 6 | Результат — **numpy-массив**, не list |


