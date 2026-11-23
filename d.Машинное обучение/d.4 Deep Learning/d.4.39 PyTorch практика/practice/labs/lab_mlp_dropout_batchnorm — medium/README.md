# Lab #3480 · MLP with Dropout and BatchNorm · **medium**

**Уровень:** medium.

- [https://www.deep-ml.com/labs/3480fd6b-ee7a-4afd-ba4b-5c934aeab10b](https://www.deep-ml.com/labs/3480fd6b-ee7a-4afd-ba4b-5c934aeab10b) · [lab_mlp_dropout_batchnorm.ipynb](./lab_mlp_dropout_batchnorm.ipynb) · эталон [lab_mlp_dropout_batchnorm_решения.ipynb](./lab_mlp_dropout_batchnorm_решения.ipynb) **после** попытки

## Что это за задача

Построить **MLP с Dropout и BatchNorm**, обучить на данных, сравнить поведение с/без регуляризации.

## Зачем это в реальной жизни

Типичный **tabular / небольшой MLP** в проде: BN ускоряет и стабилизирует, dropout снижает переобучение. Паттерн `Linear → BN → ReLU → Dropout` до сих пор встречается в baseline-моделях и головах поверх энкодеров.

