# Deep-ML #1231 · bn_eval · **medium**
**Уровень:** medium (Deep-ML).


- [problems/1231](https://www.deep-ml.com/problems/1231) · [1231_bn_eval.ipynb](./1231_bn_eval.ipynb) · эталон [1231_bn_eval_решения.ipynb](./1231_bn_eval_решения.ipynb) **после** попытки

## Что это за задача

Поведение **BatchNorm в eval**: без пересчёта μ,σ по батчу — используются running stats.

## Зачем это в реальной жизни

В проде и на валидации батчи малые; статистика по одному батчу шумная. `bn_eval` / `model.eval()` — обязательный шаг перед деплоем.

