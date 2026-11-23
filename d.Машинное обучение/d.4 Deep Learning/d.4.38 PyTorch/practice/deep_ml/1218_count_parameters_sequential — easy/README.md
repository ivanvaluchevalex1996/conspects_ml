# Deep-ML #1218 · Count Parameters of a Sequential Model · **easy**

**Уровень:** easy (Deep-ML).

- [problems/1218](https://www.deep-ml.com/problems/1218) · [1218_count_parameters_sequential.ipynb](./1218_count_parameters_sequential.ipynb) · эталон [1218_count_parameters_sequential_решения.ipynb](./1218_count_parameters_sequential_решения.ipynb) **после** попытки

## Что это за задача

Посчитать **число обучаемых параметров** у `nn.Sequential` (веса + bias).

## Зачем это в реальной жизни

Оценка **VRAM, время обучения, лицензионные/продуктовые лимиты** («модель 7B параметров»). Два одинаковых по смыслу слоя с разным `in_features` — разный размер чекпоинта.

