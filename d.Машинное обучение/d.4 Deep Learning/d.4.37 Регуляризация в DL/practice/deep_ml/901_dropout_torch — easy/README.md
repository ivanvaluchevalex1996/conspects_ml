# Deep-ML #901 · dropout (torch) · **easy**
**Уровень:** easy (Deep-ML).


- [problems/901](https://www.deep-ml.com/problems/901) · [901_dropout_torch.ipynb](./901_dropout_torch.ipynb) · эталон [901_dropout_torch_решения.ipynb](./901_dropout_torch_решения.ipynb) **после** попытки

## Что это за задача

Dropout в PyTorch: обнуление части нейронов при обучении + **inverted dropout** (масштаб 1/(1-p)).

## Зачем это в реальной жизни

Простейший способ борьбы с **переобучением**: сеть не может опереться на одни и те же нейроны. В `model.train()` dropout вкл, в `eval()` — выкл.

