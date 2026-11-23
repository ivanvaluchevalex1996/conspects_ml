# Deep-ML #1234 · sgd_step (torch) · **easy** · **easy**

**Уровень:** easy (handbook блок PyTorch Basics · Deep-ML).

- [problems/1234](https://www.deep-ml.com/problems/1234) · [1234_sgd_step.ipynb](./1234_sgd_step.ipynb) · эталон [1234_sgd_step_решения.ipynb](./1234_sgd_step_решения.ipynb) **после** попытки

## Что это за задача

Один шаг **SGD** в PyTorch: `w -= lr * grad` через тензоры.

## Зачем это в реальной жизни

Тот же шаг, что `optimizer.zero_grad(); loss.backward(); optimizer.step()` при SGD — только явно. Нужно сверять свою логику с `torch.optim.SGD` при кастомном обучении.

