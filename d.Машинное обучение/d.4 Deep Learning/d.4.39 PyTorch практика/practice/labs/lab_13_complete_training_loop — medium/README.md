# Lab #13 · PyTorch: Build a Complete Training Loop · **medium**

**Уровень:** medium.

- [https://www.deep-ml.com/labs/13](https://www.deep-ml.com/labs/13) · [lab_13_complete_training_loop.ipynb](./lab_13_complete_training_loop.ipynb) · эталон [lab_13_complete_training_loop_решения.ipynb](./lab_13_complete_training_loop_решения.ipynb) **после** попытки

## Что это за задача

Собрать **целый цикл обучения** в PyTorch: модель, DataLoader, loss, оптимизатор, эпохи, проход по train (и обычно валидация / метрика).

## Зачем это в реальной жизни

Так выглядит **реальный скрипт обучения** до Hydra/Lightning: любой pet-project, fine-tune, Kaggle. Отдельные задачи (#1219, #1237) — кирпичики; lab — склеивает их в один рабочий pipeline.

