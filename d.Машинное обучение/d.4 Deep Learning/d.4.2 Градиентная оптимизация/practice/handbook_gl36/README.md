# Практика · handbook гл. 36 (DL optimization)

Теория — [`d.4.2 … .md`](../../d.4.2%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/d.4.2%20%D0%93%D1%80%D0%B0%D0%B4%D0%B8%D0%B5%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F.md) **§1–2**. На сайте: [dl-optimization](https://mlhandbook-production.up.railway.app/parts/deep-learning/dl-optimization.html).

| Что | Где |
|-----|-----|
| §36.3 BatchNorm (форма) | [`site/36_3_batchnorm/`](./site/36_3_batchnorm/) |
| §36.5 He init — std сигнала | [`site/36_5_he_init/`](./site/36_5_he_init/) |
| §36.6 BN vs без BN (loss) | [`site/36_6_bn_training/`](./site/36_6_bn_training/) |
| сравнение Adam NumPy ↔ torch | [`site/36_compare_optimizers/`](./site/36_compare_optimizers/) |
| Домашка Deep-ML | [`deep_ml/`](./deep_ml/) |

§36.1–36.2, §36.4 (AdamW, warmup, residual) — **прочитать** на сайте / в §2 конспекта; residual подробнее в `d.4.1` §9.5.

**Порядок ментора:** He init (§36.5) → BatchNorm (§36.3) → Adam NumPy [#49](https://www.deep-ml.com/problems/49) → PyTorch steps [#1234](https://www.deep-ml.com/problems/1234)→[#1236](https://www.deep-ml.com/problems/1236) → сравнение сходимости (`36_compare_optimizers`) → `pytorch/12` (scheduler).

Чеклист: [`handbook_gl36_практика.ipynb`](./handbook_gl36_практика.ipynb).