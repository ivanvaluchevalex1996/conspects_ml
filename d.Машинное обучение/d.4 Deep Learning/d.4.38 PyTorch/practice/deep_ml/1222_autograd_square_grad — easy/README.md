# Deep-ML #1222 · Gradient of a Square with Autograd · **easy**

**Уровень:** easy (Deep-ML).

- [problems/1222](https://www.deep-ml.com/problems/1222) · [1222_autograd_square_grad.ipynb](./1222_autograd_square_grad.ipynb) · эталон [1222_autograd_square_grad_решения.ipynb](./1222_autograd_square_grad_решения.ipynb) **после** попытки

## Что это за задача

Скаляр x², градиент **по autograd** (`requires_grad`, `backward`).

## Зачем это в реальной жизни

Проверка, что autograd даёт ∂(x²)/∂x = 2x — мостик от анализа к `loss.backward()` на любой сети.

