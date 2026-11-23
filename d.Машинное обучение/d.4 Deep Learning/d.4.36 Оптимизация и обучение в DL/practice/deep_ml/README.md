# Handbook гл.36 · домашка Deep-ML

В README каждой папки — пояснение **смысла задачи** и **где это в реальном training loop**.

Handbook: [dl-optimization](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-optimization.html) · [../handbook_gl36_практика.ipynb](../handbook_gl36_практика.ipynb) → эталон [../handbook_gl36_практика_решения.ipynb](../handbook_gl36_практика_решения.ipynb). Deep-ML: в каждой папке `*_решения.ipynb` **после** попытки.

Суффикс в **имени папки** (`— easy` / `— medium`) совпадает с уровнем в таблице (для #1235 и #1236 в названии **medium** — как на Deep-ML).

На сайте handbook в блоке **🎯 Домашка · DeepML**:
- **medium** — [#49](https://www.deep-ml.com/problems/49) Adam целиком (NumPy);
- **easy** — шаги оптимизаторов на PyTorch ([#1234](https://www.deep-ml.com/problems/1234)–[#1236](https://www.deep-ml.com/problems/1236)).

У [#1235](https://www.deep-ml.com/problems/1235) и [#1236](https://www.deep-ml.com/problems/1236) на Deep-ML помечено **medium** (сложнее #1234); в конспекте ниже для них указаны оба ярлыка.

| ☐ | Папка | Deep-ML | Уровень | Заметка |
|---|--------|---------|---------|---------|
| ☐ | [49_adam_optimizer — medium](./49_adam_optimizer%20—%20medium/) | [#49](https://www.deep-ml.com/problems/49) | **medium** | `adam_optimizer`, m/v + bias correction (NumPy); handbook + Deep-ML |
| ☐ | [146_momentum — easy](./146_momentum%20—%20easy/) | [#146](https://www.deep-ml.com/problems/146) | **easy** | один шаг momentum (NumPy); **доп.** (нет в блоке handbook), Deep-ML easy |
| ☐ | [1234_sgd_step — easy](./1234_sgd_step%20—%20easy/) | [#1234](https://www.deep-ml.com/problems/1234) | **easy** | `sgd_step` (torch); handbook + Deep-ML |
| ☐ | [1235_momentum_step — medium](./1235_momentum_step%20—%20medium/) | [#1235](https://www.deep-ml.com/problems/1235) | **easy** (handbook) / **medium** (Deep-ML) | `momentum_step` (torch) |
| ☐ | [1236_adam_step — medium](./1236_adam_step%20—%20medium/) | [#1236](https://www.deep-ml.com/problems/1236) | **easy** (handbook) / **medium** (Deep-ML) | `adam_step` (torch) |

**Порядок:** #49 NumPy → #1234 → #1235 → #1236 → submit → сверка с §36.4 в [handbook_gl36_практика.ipynb](../handbook_gl36_практика.ipynb).

Архив решений: [13_deep_ml…](../../../../../../python_base/13_deep_ml_deep_learning.py) (#49, #146 пока нет).