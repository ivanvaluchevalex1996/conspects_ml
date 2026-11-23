# Deep-ML #1219 · One Training Step · **medium**

**Уровень:** medium.

- [https://www.deep-ml.com/problems/1219](https://www.deep-ml.com/problems/1219) · [1219_one_training_step.ipynb](./1219_one_training_step.ipynb) · эталон [1219_one_training_step_решения.ipynb](./1219_one_training_step_решения.ipynb) **после** попытки

## Что это за задача

Один полный **training step**: forward, loss, `zero_grad`, `backward`, `step` (и часто eval ветка не нужна).

## Зачем это в реальной жизни

Это **атом обучения**, который повторяют миллионы раз в `for epoch` / `for batch`. Весь прод-пайплайн (DDP, mixed precision) оборачивает тот же шаг.

