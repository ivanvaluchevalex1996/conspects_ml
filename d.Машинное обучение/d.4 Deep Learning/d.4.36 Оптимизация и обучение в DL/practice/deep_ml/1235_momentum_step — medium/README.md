# Deep-ML #1235 · momentum_step (torch) · **easy** / **medium** · **medium**

**Уровень:** easy в [handbook](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-optimization.html) (блок PyTorch Basics); **medium** на Deep-ML.

- [problems/1235](https://www.deep-ml.com/problems/1235) · [1235_momentum_step.ipynb](./1235_momentum_step.ipynb) · эталон [1235_momentum_step_решения.ipynb](./1235_momentum_step_решения.ipynb) **после** попытки

## Что это за задача

Один шаг **momentum** в PyTorch (буфер скорости + обновление веса).

## Зачем это в реальной жизни

Соответствует `torch.optim.SGD(momentum=…)` или SGDM. В цикле обучения momentum — один из главных рычагов после learning rate.

