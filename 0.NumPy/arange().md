
---

## 📌 Одна фраза

> `np.arange` — **последовательность чисел** с заданным шагом (как `range`, но сразу numpy-массив).

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

> 💡 Не путать с `range()` Python — `arange` сразу **numpy-массив**.

---

## 🔷 arange vs linspace

|    | `arange` | `linspace` |
|:---|:---|:---|
| шаг | фиксированный | фиксированное **число** точек |
| stop | не входит | **входит** последняя точка |

---

## 🔷 Пример

```python
np.arange(10)          # [0, 1, 2, ..., 9]
np.arange(3, 10, 3)    # [3, 6, 9]
```

---

## ✅ Коротко запомнить

| # | Правило |
|:---|:---|
| 1 | `arange(stop)` → 0 .. stop-1 |
| 2 | `arange(a, b, step)` → a, a+step, ... **строго меньше b** |
| 3 | Результат — **numpy-массив**, не list |


