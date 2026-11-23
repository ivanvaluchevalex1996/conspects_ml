# Deep-ML #1223 · Gradient of a Weighted Sum of Squares · **medium**

**Уровень:** medium (Deep-ML).

- [problems/1223](https://www.deep-ml.com/problems/1223) · [1223_autograd_weighted_sum_squares.ipynb](./1223_autograd_weighted_sum_squares.ipynb) · эталон [1223_autograd_weighted_sum_squares_решения.ipynb](./1223_autograd_weighted_sum_squares_решения.ipynb) **после** попытки

## Что это за задача

Градиент **взвешенной суммы квадратов** по нескольким переменным.

## Зачем это в реальной жизни

Loss часто — сумма по батчу/признакам с весами (MSE с маской, взвешенные классы). Нужно уметь читать, **какой тензор накопил `.grad`** после одного `backward()`.

