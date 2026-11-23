# Deep-ML #23 · Softmax · **easy**
**Уровень:** easy (Deep-ML).


- [problems/23](https://www.deep-ml.com/problems/23) · [23_softmax.ipynb](./23_softmax.ipynb) · эталон [23_softmax_решения.ipynb](./23_softmax_решения.ipynb) · §9.3

| ☐ | Стабильный softmax (вычесть max) → `F.softmax` на том же z → submit |

## Что это за задача

Реализовать **softmax**: из вектора логитов — распределение вероятностей по классам (сумма = 1).

## Зачем это в реальной жизни

Многоклассовая классификация: выход сети → softmax → cross-entropy. Картинка «кот/собака/птица», токены в NLP — везде нормализация по классам.

