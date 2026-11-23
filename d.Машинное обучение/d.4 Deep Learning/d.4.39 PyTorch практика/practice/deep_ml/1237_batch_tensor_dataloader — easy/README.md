# Deep-ML #1237 · Batch a TensorDataset with DataLoader · **easy**

**Уровень:** easy.

- [https://www.deep-ml.com/problems/1237](https://www.deep-ml.com/problems/1237) · [1237_batch_tensor_dataloader.ipynb](./1237_batch_tensor_dataloader.ipynb) · эталон [1237_batch_tensor_dataloader_решения.ipynb](./1237_batch_tensor_dataloader_решения.ipynb) **после** попытки

## Что это за задача

Собрать **TensorDataset + DataLoader**, пройти батчи и вернуть число батчей и shape первого батча X.

## Зачем это в реальной жизни

Любое обучение: `for xb, yb in train_loader` → GPU → forward. Батчи дают **память + SGD**; без DataLoader пришлось бы резать индексы вручную.

