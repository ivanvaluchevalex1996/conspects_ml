# Deep-ML: решённые задачи ↔ конспекты

Центральная таблица: что уже **решаешь в коде** в `учеба мл/python_base/` и **где теория** в ynote.

**Файлы с решениями**

| Файл | Категория Deep-ML |
|------|-------------------|
| [`11_deep_ml_linear_algebra copy.py`](../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/python_base/11_deep_ml_linear_algebra%20copy.py) | Linear Algebra |
| [`12_deep_ml_machine_learning.py`](../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/python_base/12_deep_ml_machine_learning.py) | Machine Learning |
| [`13_deep_ml_deep_learning.py`](../../%D1%83%D1%87%D0%B5%D0%B1%D0%B0%20%D0%BC%D0%BB/python_base/13_deep_ml_deep_learning.py) | Deep Learning |

---

## Linear Algebra (`11_…`)

| # | Задача | Функция | Конспект |
|---|--------|---------|----------|
| [1](https://www.deep-ml.com/problems/1) | Matrix–vector dot | `matrix_dot_vector` | [`a.NumPy/11`](../a.NumPy/11.%D1%83%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20star%2C%20at%2C%20dot.md), [`5.матрицы`](../a.NumPy/5.%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D1%8B.md) |
| [2](https://www.deep-ml.com/problems/2) | Transpose | `transpose_matrix` | [`5.матрицы`](../a.NumPy/5.%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D1%8B.md) |
| [3](https://www.deep-ml.com/problems/3) | Reshape | `reshape_matrix` | [`4.многомерные`](../a.NumPy/4.%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D0%BC%D0%B5%D1%80%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B0%D1%81%D1%81%D0%B8%D0%B2%D1%8B.md) |
| [4](https://www.deep-ml.com/problems/4) | Mean by row/column | `calculate_matrix_mean` | [`6.агрегации`](../a.NumPy/6.%D0%B0%D0%B3%D1%80%D0%B5%D0%B3%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B8%20%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0.md) |
| [5](https://www.deep-ml.com/problems/5) | Scalar multiply matrix | `scalar_multiply` | [`5.матрицы`](../a.NumPy/5.%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D1%8B.md) |
| [8](https://www.deep-ml.com/problems/8) | Inverse 2×2 | `inverse_2x2` | [`5.матрицы`](../a.NumPy/5.%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D1%8B.md) |
| [27](https://www.deep-ml.com/problems/27) | Change of basis B→C | `transform_basis` | [`Базис`](../c.%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0/%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%B0%D1%8F%20%D0%B0%D0%BB%D0%B3%D0%B5%D0%B1%D1%80%D0%B0/%D0%91%D0%B0%D0%B7%D0%B8%D1%81.md) |
| [35](https://www.deep-ml.com/problems/35) | Vector → diagonal matrix | `make_diagonal` | [`5.матрицы`](../a.NumPy/5.%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D1%8B.md) |
| [65](https://www.deep-ml.com/problems/65) | CSR format | `compressed_row_sparse_matrix` | — (редкие матрицы; пока только код) |
| [66](https://www.deep-ml.com/problems/66) | Orthogonal projection | `orthogonal_projection` | [`Базис`](../c.%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0/%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%B0%D1%8F%20%D0%B0%D0%BB%D0%B3%D0%B5%D0%B1%D1%80%D0%B0/%D0%91%D0%B0%D0%B7%D0%B8%D1%81.md) |
| [67](https://www.deep-ml.com/problems/67) | CSC format | `compressed_col_sparse_matrix` | — |
| [76](https://www.deep-ml.com/problems/76) | Cosine similarity | `cosine_similarity` | [`d.2.2` §метрики](../d.%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5/d.2%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B/d.2.2%20%D0%9C%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B.md) |
| [83](https://www.deep-ml.com/problems/83) | Dot product | `calculate_dot_product` | [`11.…dot`](../a.NumPy/11.%D1%83%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20star%2C%20at%2C%20dot.md) |
| [84](https://www.deep-ml.com/problems/84) | Phi (полиномы) | `phi_transform` | [`d.1.3`](../d.%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5/d.1%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%BC%D0%BB/d.1.3%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%B0%D1%8F%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%B8%D0%BD%D0%BE%D0%BC%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F.md) |
| [121](https://www.deep-ml.com/problems/121) | Vector sum | `vector_sum` | [`11.…dot`](../a.NumPy/11.%D1%83%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20star%2C%20at%2C%20dot.md) |
| — | Cross product (3D) | `cross_product` | та же тренировка в `11_…` (отдельного # в Deep-ML в таблице нет) |

---

## Machine Learning (`12_…`)

| # | Задача | Функция | Конспект |
|---|--------|---------|----------|
| [14](https://www.deep-ml.com/problems/14) | Normal equation | `linear_regression_normal_equation` | [`d.3.9` §4–6](d.3%20Classic%20ML/d.3.9%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F%20%E2%80%94%20%D0%BD%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D1%83%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%B3%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D1%8B%D0%B9%20%D1%81%D0%BF%D1%83%D1%81%D0%BA.md) |
| [15](https://www.deep-ml.com/problems/15) | Linear regression GD | `linear_regression_gradient_descent` | [`d.3.9` §7–9](d.3%20Classic%20ML/d.3.9%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F%20%E2%80%94%20%D0%BD%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D1%83%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%B3%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D1%8B%D0%B9%20%D1%81%D0%BF%D1%83%D1%81%D0%BA.md), [`d.2.1.4`](../d.2%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B/d.2.1%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8/d.2.1.4%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%20MSE%20%D0%B8%20SGD%20%D0%B4%D0%BB%D1%8F%20%D0%BB%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%BE%D0%B9%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) |
| [16](https://www.deep-ml.com/problems/16) | Feature scaling | `feature_scaling` | [`d.4.3` §1](../d.4%20Deep%20Learning/d.4.3%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20Deep%20Learning/d.4.3%20%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B2%20Deep%20Learning.md) |
| [29](https://www.deep-ml.com/problems/29) | Shuffle X, y | `shuffle_data` | [`d.3.2` §2.1](d.3%20Classic%20ML/d.3.2%20%D0%9A%D1%80%D0%BE%D1%81%D1%81-%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%B0%D1%86%D0%B8%D1%8F/d.3.2%20%D0%9A%D1%80%D0%BE%D1%81%D1%81-%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D0%B0%D1%86%D0%B8%D1%8F.md), [`1.random`](../a.NumPy/1.random%20%E2%80%94%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F.md) |
| [30](https://www.deep-ml.com/problems/30) | Batch iterator | `batch_iterator` | [`d.4.1` §11.3](../d.4%20Deep%20Learning/d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md), [`d.4.2`](../d.4%20Deep%20Learning/d.4.2%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F.md) |
| [34](https://www.deep-ml.com/problems/34) | One-hot | `to_categorical` | [`d.2.1` one-hot](../d.2%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B/d.2.1%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8/d.2.1%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8.md) |
| [36](https://www.deep-ml.com/problems/36) | Accuracy | `accuracy_score` | [`d.3.1`](d.3%20Classic%20ML/d.3.1%20%D0%9C%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B8%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) |
| [43](https://www.deep-ml.com/problems/43) | Ridge loss | `ridge_loss` | [`d.4.3`](../d.4%20Deep%20Learning/d.4.3%20Регуляризация%20в%20Deep%20Learning/d.4.3%20Регуляризация%20в%20Deep%20Learning.md), L2 в [`d.2.4`](../d.2%20Линейные%20модели%20метрические%20методы/d.2.4%20Главное%20из%20дз%20по%20KNN%20и%20лин%20классификатору.md) |
| [45](https://www.deep-ml.com/problems/45) | Linear kernel | `kernel_function` | [`d.2.2`](../d.2%20Линейные%20модели%20метрические%20методы/d.2.2%20Метрические%20методы.md) |
| [46](https://www.deep-ml.com/problems/46) | Precision | `precision` | [`d.3.1`](d.3%20Classic%20ML/d.3.1%20%D0%9C%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B8%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) |
| [52](https://www.deep-ml.com/problems/52) | Recall | `recall` | [`d.3.1`](d.3%20Classic%20ML/d.3.1%20%D0%9C%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B8%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) |
| [61](https://www.deep-ml.com/problems/61) | Fβ / F1 | `f_score` | [`d.3.1`](d.3%20Classic%20ML/d.3.1%20%D0%9C%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B8%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) |
| [64](https://www.deep-ml.com/problems/64) | Gini impurity | `gini_impurity` | [`d.3.3`](d.3%20Classic%20ML/d.3.3%20Решающие%20деревья.md) |
| [69](https://www.deep-ml.com/problems/69) | R² | `r_squared` | [`d.3.1` §регрессия](d.3%20Classic%20ML/d.3.1%20%D0%9C%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B8%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) |
| [71](https://www.deep-ml.com/problems/71) | RMSE | `rmse` | [`d.3.1`](d.3%20Classic%20ML/d.3.1%20%D0%9C%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B8%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) |

---

## Deep Learning (`13_…`)

| # | Задача | Функция | Конспект |
|---|--------|---------|----------|
| [22](https://www.deep-ml.com/problems/22) | Sigmoid | `sigmoid` | [`d.4.1` §5, §8–9](../d.4%20Deep%20Learning/d.4.1%20Полносвязные%20нейронные%20сети.md) |
| [23](https://www.deep-ml.com/problems/23) | Softmax | `softmax` | [`d.4.1` §9.3](../d.4%20Deep%20Learning/d.4.1%20Полносвязные%20нейронные%20сети.md), [`a.NumPy/11`](../a.NumPy/11.%D1%83%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20star%2C%20at%2C%20dot.md) |
| [24](https://www.deep-ml.com/problems/24) | Single neuron + MSE | `single_neuron_model` | [`d.4.1` §5](../d.4%20Deep%20Learning/d.4.1%20Полносвязные%20нейронные%20сети.md), [`11.…dot`](../a.NumPy/11.%D1%83%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%E2%80%94%20star%2C%20at%2C%20dot.md) |
| [39](https://www.deep-ml.com/problems/39) | Log-softmax | `log_softmax` | [`d.4.1` §9.3.1](../d.4%20Deep%20Learning/d.4.1%20Полносвязные%20нейронные%20сети.md) |
| [42](https://www.deep-ml.com/problems/42) | ReLU | `relu` | [`d.4.1` §8–9](../d.4%20Deep%20Learning/d.4.1%20Полносвязные%20нейронные%20сети.md) |
| [44](https://www.deep-ml.com/problems/44) | Leaky ReLU | `leaky_relu` | [`d.4.1`](../d.4%20Deep%20Learning/d.4.1%20Полносвязные%20нейронные%20сети.md), [`d.4.3.3`](../d.4%20Deep%20Learning/d.4.3%20Регуляризация%20в%20Deep%20Learning/d.4.3.3%20Пример%20—%20Dropout%20и%20чем%20он%20отличается%20от%20ReLU.md) |
| [96](https://www.deep-ml.com/problems/96) | Hard Sigmoid | `hard_sigmoid` | [`d.4.1` §9.2](../d.4%20Deep%20Learning/d.4.1%20Полносвязные%20нейронные%20сети.md#92-sigmoid--%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D1%8F-%D0%B2%D1%8B%D1%85%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE-%D1%81%D0%BB%D0%BE%D1%8F-%D0%B1%D0%B8%D0%BD%D0%B0%D1%80%D0%BD%D0%B0%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0) |
| [97](https://www.deep-ml.com/problems/97) | ELU | `elu` | [`d.4.1` §9.4](../d.4%20Deep%20Learning/d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md#94-%D1%80%D0%B5%D0%B4%D0%BA%D0%B8%D0%B5-%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D0%B8-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%BE--deep-ml) |
| [99](https://www.deep-ml.com/problems/99) | Softplus | `softplus` | [`d.4.1` §9.4](../d.4%20Deep%20Learning/d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md#94-%D1%80%D0%B5%D0%B4%D0%BA%D0%B8%D0%B5-%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D0%B8-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%BE--deep-ml) |
| [100](https://www.deep-ml.com/problems/100) | Softsign | `softsign` | [`d.4.1` §9.4](../d.4%20Deep%20Learning/d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md#94-%D1%80%D0%B5%D0%B4%D0%BA%D0%B8%D0%B5-%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D0%B8-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%BE--deep-ml) |
| [102](https://www.deep-ml.com/problems/102) | Swish | `swish` | [`d.4.1` §9.4](../d.4%20Deep%20Learning/d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md#94-%D1%80%D0%B5%D0%B4%D0%BA%D0%B8%D0%B5-%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D0%B8-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%BE--deep-ml) |
| [113](https://www.deep-ml.com/problems/113) | Residual block | `residual_block` | [`d.4.1` §9.5.1](../d.4%20Deep%20Learning/d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md#951-%D0%BE%D1%81%D1%82%D0%B0%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9-%D0%B1%D0%BB%D0%BE%D0%BA-shortcut--deep-ml-113) |
| [134](https://www.deep-ml.com/problems/134) | Multi-class CE (batch) | `compute_cross_entropy_loss` | [`d.4.1` §10.2](../d.4%20Deep%20Learning/d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md), [`d.2.4`](../d.2%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B/d.2.4%20%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D0%B5%20%D0%B8%D0%B7%20%D0%B4%D0%B7%20%D0%BF%D0%BE%20KNN%20%D0%B8%20%D0%BB%D0%B8%D0%BD%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D1%80%D1%83.md) |
| [263](https://www.deep-ml.com/problems/263) | Binary CE | `binary_cross_entropy` | [`d.4.1` §10.2](../d.4%20Deep%20Learning/d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md), #22 sigmoid |
| [217](https://www.deep-ml.com/problems/217) | σ′ sigmoid/tanh/ReLU | `activation_derivatives` | [`d.4.1` §backprop](../d.4%20Deep%20Learning/d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md) |
| [146](https://www.deep-ml.com/problems/146) | Momentum step | `momentum_optimizer` | [`d.4.2`](../d.4%20Deep%20Learning/d.4.2%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F.md), [`d.2.1.4`](../d.2%20%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B/d.2.1.4%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%20MSE%20%D0%B8%20SGD%20%D0%B4%D0%BB%D1%8F%20%D0%BB%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%BE%D0%B9%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D0%B8.md) (заготовка) |

---

## Как пользоваться

1. Читаешь конспект — в начале темы ищи блок **«Deep-ML: решено в коде»** (или ссылку на эту таблицу).
2. Открываешь файл `11_…` / `12_…` / `13_…` → функция с тем же именем, что в таблице.
3. На сайте Deep-ML номер задачи = `#N` в комментариях у функции (в `13_…` уже проставлены; в `11_…` и `12_…` — смотри эту таблицу).

Обновляй этот файл, когда добавляешь новые решения в `python_base/`.
