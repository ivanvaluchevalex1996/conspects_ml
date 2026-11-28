# Практика · handbook гл. 42 (transfer learning)

Теория: [d.5.42 … .md](../d.5.42%20Transfer%20learning.md) · [transfer-learning](https://mlhandbook-production.up.railway.app/parts/deep-learning/transfer-learning.html).

| Что | Где |
|-----|-----|
| заморозка, замена головы, ResNet18 (фрагменты) | [handbook_gl42_практика.ipynb](./handbook_gl42_практика.ipynb) · [handbook_gl42_практика_решения.ipynb](./handbook_gl42_практика_решения.ipynb) |
| **мини-проект:** пчёлы / муравьи (полное решение) | **[handbook_gl42_hymenoptera_решения.ipynb](./handbook_gl42_hymenoptera_решения.ipynb)** · [§6](../d.5.42%20Transfer%20learning.md#6-практика-handbook--мини-проект) |
| эталон upstream (длинная версия) | [PyTorch transfer learning tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) |
| разбор на видео (тот же датасет, **своя CNN**) | **🟠** [Дубинин · 23, с 5:44](https://www.youtube.com/watch?v=M0iB56Vwy64&t=344) · [плейлист](https://www.youtube.com/playlist?list=PLBP4Q3FNSLK2rtGPBsK-aMAetYj-8yg_1) · [`17-23_cnn_обзор`](../../../../pytorch/pytorch%20дубинин/17-23_cnn/17-23_cnn_обзор.md) §8 |

**В ноутбуке:** **Зачем этот фрагмент** + ссылка на конспект → **Что проверить** → код. Мини-проект — по шагам 1–3 с сайта ментора; длинный train loop не дублируем — туториал PyTorch или видео 23.

**Данные:** папка `practice/data/` (Hymenoptera и zip) в **`.gitignore`** — при `git add` / push не попадёт; качается локально из [hymenoptera_решения](./handbook_gl42_hymenoptera_решения.ipynb).

**NLP:** после механики `requires_grad` — `transformers` + BERT ([конспект §4](../d.5.42%20Transfer%20learning.md#4-nlp-и-lora-handbook-424)).