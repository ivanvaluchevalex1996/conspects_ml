# Deep-ML #98 · PReLU forward + backward · **medium**
**Уровень:** medium (Deep-ML).


- [problems/98](https://www.deep-ml.com/problems/98) · [98_prelu.ipynb](./98_prelu.ipynb) · эталон [98_prelu_решения.ipynb](./98_prelu_решения.ipynb) · §9.4

| ☐ | `prelu_forward` / `prelu_backward` (примеры с сайта) → submit (в `13_…` пока нет) |

## Что это за задача

Реализовать **PReLU**: утечка с обучаемым коэффициентом α (или по каналу).

## Зачем это в реальной жизни

В глубоких сетях фиксированный leaky-ReLU не всегда оптимален; PReLU даёт модели подстроить наклон «мертвой» зоны. Встречается в backbone-сетях и когда дорога каждая доля качества.

