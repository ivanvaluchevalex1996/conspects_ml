# Deep-ML #39 · Log-softmax · **easy**
**Уровень:** easy (Deep-ML).


- [problems/39](https://www.deep-ml.com/problems/39) · [39_log_softmax.ipynb](./39_log_softmax.ipynb) · эталон [39_log_softmax_решения.ipynb](./39_log_softmax_решения.ipynb) · §9.3.1

| ☐ | `log_softmax` ndarray → `F.log_softmax` → submit |

## Что это за задача

Реализовать **log-softmax** (часто стабильнее, чем log(softmax)) и связь с softmax.

## Зачем это в реальной жизни

В PyTorch **NLLLoss** ждёт лог-вероятности: `log_softmax` + NLL = стабильный **CrossEntropyLoss**. Так считают лосс в классификаторах без переполнения float.

