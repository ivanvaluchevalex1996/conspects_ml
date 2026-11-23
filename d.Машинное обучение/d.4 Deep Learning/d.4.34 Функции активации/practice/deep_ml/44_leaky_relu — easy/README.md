# Deep-ML #44 · Leaky ReLU · **easy**
**Уровень:** easy (Deep-ML).


- [problems/44](https://www.deep-ml.com/problems/44) · [44_leaky_relu.ipynb](./44_leaky_relu.ipynb) · эталон [44_leaky_relu_решения.ipynb](./44_leaky_relu_решения.ipynb) · §9.4

| ☐ | NumPy/scalar → `F.leaky_relu` → submit |

## Что это за задача

Реализовать **Leaky ReLU**: для отрицательных z небольшой наклон αz вместо нуля.

## Зачем это в реальной жизни

Если много нейронов «умирают» (всегда 0 на отрицательной полуплоскости), обучение тормозится. Leaky/PReLU подпускают градиент — в GAN, некоторых детекторах и когда обычный ReLU нестабилен.

