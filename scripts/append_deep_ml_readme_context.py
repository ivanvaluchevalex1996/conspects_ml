# Одноразовый скрипт: дописать блоки «Что это» / «Зачем» в README Deep-ML (d.4)
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "d.Машинное обучение/d.4 Deep Learning"

# path_suffix -> (что, зачем)  — path relative to ROOT
BLOCKS = {
    "d.4.33 Нейрон и полносвязная сеть/practice/1224_single_neuron/README.md": (
        "Реализовать **один нейрон**: линейная комбинация входов + смещение (и при необходимости активация). Сверка с формулой из конспекта и submit на Deep-ML.",
        "Любая нейросеть — слой из нейронов. Понимание «одного шага» (взвешенная сумма → нелинейность) — база для MLP, CNN и трансформеров: ты видишь, откуда берутся размерности и что именно обучается.",
    ),
    "d.4.34 Функции активации/practice/deep_ml/22_sigmoid — easy/README.md": (
        "Функция **σ(z)** и её производная; часто на NumPy с проверкой `need`.",
        "Сигмоида ограничивает выход (0,1) — классика для **бинарной классификации** и «вероятности» в старых сетях; понимание производной нужно для backprop. Сейчас в скрытых слоях реже, но в выходе и в RNN/LSTM ещё встречается.",
    ),
    "d.4.34 Функции активации/practice/deep_ml/42_relu — easy/README.md": (
        "Реализовать **ReLU**: max(0, z) и производную (с оговоркой для z=0).",
        "ReLU — дефолт для скрытых слоёв в CV и большинстве MLP: быстро считается, уменьшает затухание градиента по сравнению с сигмоидой. В PyTorch тот же смысл, что в `F.relu` / `nn.ReLU`.",
    ),
    "d.4.34 Функции активации/practice/deep_ml/44_leaky_relu — easy/README.md": (
        "Реализовать **Leaky ReLU**: для отрицательных z небольшой наклон αz вместо нуля.",
        "Если много нейронов «умирают» (всегда 0 на отрицательной полуплоскости), обучение тормозится. Leaky/PReLU подпускают градиент — в GAN, некоторых детекторах и когда обычный ReLU нестабилен.",
    ),
    "d.4.34 Функции активации/practice/deep_ml/23_softmax — easy/README.md": (
        "Реализовать **softmax**: из вектора логитов — распределение вероятностей по классам (сумма = 1).",
        "Многоклассовая классификация: выход сети → softmax → cross-entropy. Картинка «кот/собака/птица», токены в NLP — везде нормализация по классам.",
    ),
    "d.4.34 Функции активации/practice/deep_ml/39_log_softmax — easy/README.md": (
        "Реализовать **log-softmax** (часто стабильнее, чем log(softmax)) и связь с softmax.",
        "В PyTorch **NLLLoss** ждёт лог-вероятности: `log_softmax` + NLL = стабильный **CrossEntropyLoss**. Так считают лосс в классификаторах без переполнения float.",
    ),
    "d.4.34 Функции активации/practice/deep_ml/98_prelu — medium/README.md": (
        "Реализовать **PReLU**: утечка с обучаемым коэффициентом α (или по каналу).",
        "В глубоких сетях фиксированный leaky-ReLU не всегда оптимален; PReLU даёт модели подстроить наклон «мертвой» зоны. Встречается в backbone-сетях и когда дорога каждая доля качества.",
    ),
    "d.4.35 Backpropagation/practice/deep_ml/25_single_neuron_backprop — medium/README.md": (
        "Обучить **один нейрон** с MSE и сигмоидой: прямой проход, градиенты, шаг градиентного спуска по батчу.",
        "Мини-версия **полного цикла обучения** без autograd: так понимают, что делает `loss.backward()` и `optimizer.step()`. Полезно при отладке «почему не учится» на маленькой модели.",
    ),
    "d.4.35 Backpropagation/practice/deep_ml/26_basic_autograd — medium/README.md": (
        "Свой мини-движок **autograd** (как Karpathy micrograd): класс `Value`, ребро графа, `backward()`.",
        "PyTorch под капотом строит **граф вычислений** и рассылает градиенты. Реализация руками показывает, почему нужны `zero_grad`, зачем не держать лишние ссылки и как из одного скаляра loss течёт ∂ к весам.",
    ),
    "d.4.36 Оптимизация и обучение в DL/practice/deep_ml/49_adam_optimizer — medium/README.md": (
        "Реализовать **Adam** на NumPy: моменты m, v, bias correction, обновление веса.",
        "Adam (и AdamW) — **стандартный оптимизатор** в NLP, CV, табличных задачах: адаптивный шаг, устойчивее чистого SGD. Понимание сутев помогает выбирать lr и не путать с momentum.",
    ),
    "d.4.36 Оптимизация и обучение в DL/practice/deep_ml/146_momentum — easy/README.md": (
        "Один шаг **SGD с momentum** в NumPy: накопление скорости по градиенту.",
        "Momentum сглаживает шум в стохастических батчах и быстрее идёт по «долинам» лосса. Основа перед Adam; в SGD+nesterov ещё используется в CV.",
    ),
    "d.4.36 Оптимизация и обучение в DL/practice/deep_ml/1234_sgd_step — easy/README.md": (
        "Один шаг **SGD** в PyTorch: `w -= lr * grad` через тензоры.",
        "Тот же шаг, что `optimizer.zero_grad(); loss.backward(); optimizer.step()` при SGD — только явно. Нужно сверять свою логику с `torch.optim.SGD` при кастомном обучении.",
    ),
    "d.4.36 Оптимизация и обучение в DL/practice/deep_ml/1235_momentum_step — medium/README.md": (
        "Один шаг **momentum** в PyTorch (буфер скорости + обновление веса).",
        "Соответствует `torch.optim.SGD(momentum=…)` или SGDM. В цикле обучения momentum — один из главных рычагов после learning rate.",
    ),
    "d.4.36 Оптимизация и обучение в DL/practice/deep_ml/1236_adam_step — medium/README.md": (
        "Один шаг **Adam** в PyTorch: m, v, коррекция, обновление параметра.",
        "Проверка, что ты понимаешь, что делает `torch.optim.Adam` за один `step()` — важно при написании своих мета-оптимизаторов и отладке обучения.",
    ),
    "d.4.37 Регуляризация в DL/practice/deep_ml/batchnorm1d_numpy — easy/README.md": (
        "BatchNorm **1D руками** на NumPy: среднее/дисперсия по батчу, нормализация, γ и β.",
        "BatchNorm стабилизирует активации, позволяет **больший lr** и ускоряет сходимость в CNN/MLP. В проде важно знать разницу train (статистика батча) vs eval (скользящее среднее).",
    ),
    "d.4.37 Регуляризация в DL/practice/deep_ml/901_dropout_torch — easy/README.md": (
        "Dropout в PyTorch: обнуление части нейронов при обучении + **inverted dropout** (масштаб 1/(1-p)).",
        "Простейший способ борьбы с **переобучением**: сеть не может опереться на одни и те же нейроны. В `model.train()` dropout вкл, в `eval()` — выкл.",
    ),
    "d.4.37 Регуляризация в DL/practice/deep_ml/151_dropout_layer — medium/README.md": (
        "Слой **Dropout** на NumPy (маска, train/eval).",
        "До `nn.Dropout` полезно реализовать механику самому: почему при инференсе ничего не «выкидываем», а только масштабируем при обучении.",
    ),
    "d.4.37 Регуляризация в DL/practice/deep_ml/1230_dropout_demo — medium/README.md": (
        "Показать разницу **train vs eval** для dropout: разные маски / поведение.",
        "Типичный баг: забыли `model.eval()` перед валидацией или прод-инференсом — метрики «плывут», предсказания шумные. Задача фиксирует правильную семантику режимов.",
    ),
    "d.4.37 Регуляризация в DL/practice/deep_ml/1231_bn_eval — medium/README.md": (
        "Поведение **BatchNorm в eval**: без пересчёта μ,σ по батчу — используются running stats.",
        "В проде и на валидации батчи малые; статистика по одному батчу шумная. `bn_eval` / `model.eval()` — обязательный шаг перед деплоем.",
    ),
    "d.4.38 PyTorch/practice/deep_ml/1218_count_parameters_sequential — easy/README.md": (
        "Посчитать **число обучаемых параметров** у `nn.Sequential` (веса + bias).",
        "Оценка **VRAM, время обучения, лицензионные/продуктовые лимиты** («модель 7B параметров»). Два одинаковых по смыслу слоя с разным `in_features` — разный размер чекпоинта.",
    ),
    "d.4.38 PyTorch/practice/deep_ml/1220_create_inspect_tensor — easy/README.md": (
        "Создать тензор, вывести **shape, dtype, device** — базовая «разведка».",
        "90% багов в DL — «не тот shape/dtype/device». Перед обучением привычка смотреть `x.shape`, `x.dtype`, `x.device` экономит часы.",
    ),
    "d.4.38 PyTorch/practice/deep_ml/1221_reshape_transpose_tensor — easy/README.md": (
        "**reshape / view** и **transpose / permute**: привести данные к форме, которую ждёт слой (NCHW, NT, …).",
        "Картинки, батчи, attention — всё через правильные оси. Ошибка permute ломает свёртки и loss; в DataLoader коллатор тоже про формы.",
    ),
    "d.4.38 PyTorch/practice/deep_ml/1222_autograd_square_grad — easy/README.md": (
        "Скаляр x², градиент **по autograd** (`requires_grad`, `backward`).",
        "Проверка, что autograd даёт ∂(x²)/∂x = 2x — мостик от анализа к `loss.backward()` на любой сети.",
    ),
    "d.4.38 PyTorch/practice/deep_ml/1223_autograd_weighted_sum_squares — medium/README.md": (
        "Градиент **взвешенной суммы квадратов** по нескольким переменным.",
        "Loss часто — сумма по батчу/признакам с весами (MSE с маской, взвешенные классы). Нужно уметь читать, **какой тензор накопил `.grad`** после одного `backward()`.",
    ),
    "d.4.38 PyTorch/practice/deep_ml/1225_mlp_two_layer_forward — medium/README.md": (
        "Прямой проход **двухслойного MLP**: линейный → активация → линейный.",
        "Типичный **табличный классификатор / MLP** перед softmax. Forward отдельно — без backward — чтобы не смешивать «что считает сеть» и «как учится».",
    ),
    "d.4.38 PyTorch/practice/deep_ml/1226_relu_leaky_relu — easy/README.md": (
        "ReLU и Leaky ReLU через **PyTorch** (тензоры, без ручного цикла по элементам).",
        "В реальном коде активации — **векторизованно** на GPU; задача приучает использовать `F.relu` / `nn.ReLU`, а не Python-циклы.",
    ),
    "d.4.38 PyTorch/practice/deep_ml/1227_softmax_stable — medium/README.md": (
        "Численно **устойчивый softmax** (вычитание max по оси).",
        "На больших логитах naive softmax → overflow/NaN. Та же идея в `F.softmax` и в cross-entropy внутри PyTorch — без неё прод-модели падают на выбросах.",
    ),
    "d.4.39 PyTorch практика/practice/deep_ml/1237_batch_tensor_dataloader — easy/README.md": (
        "Собрать **TensorDataset + DataLoader**, пройти батчи и вернуть число батчей и shape первого батча X.",
        "Любое обучение: `for xb, yb in train_loader` → GPU → forward. Батчи дают **память + SGD**; без DataLoader пришлось бы резать индексы вручную.",
    ),
    "d.4.39 PyTorch практика/practice/deep_ml/1228_mse_from_scratch — easy/README.md": (
        "Реализовать **MSE (mean squared error)** между предсказанием и целью.",
        "Регрессия (цена, траектория, скор), реконструкция — базовый лосс. Понимание mean vs sum важно: такой же масштаб лосса при разном batch_size.",
    ),
    "d.4.39 PyTorch практика/practice/deep_ml/1219_one_training_step — medium/README.md": (
        "Один полный **training step**: forward, loss, `zero_grad`, `backward`, `step` (и часто eval ветка не нужна).",
        "Это **атом обучения**, который повторяют миллионы раз в `for epoch` / `for batch`. Весь прод-пайплайн (DDP, mixed precision) оборачивает тот же шаг.",
    ),
    "d.4.39 PyTorch практика/practice/labs/lab_13_complete_training_loop — medium/README.md": (
        "Собрать **целый цикл обучения** в PyTorch: модель, DataLoader, loss, оптимизатор, эпохи, проход по train (и обычно валидация / метрика).",
        "Так выглядит **реальный скрипт обучения** до Hydra/Lightning: любой pet-project, fine-tune, Kaggle. Отдельные задачи (#1219, #1237) — кирпичики; lab — склеивает их в один рабочий pipeline.",
    ),
    "d.4.39 PyTorch практика/practice/labs/lab_mlp_dropout_batchnorm — medium/README.md": (
        "Построить **MLP с Dropout и BatchNorm**, обучить на данных, сравнить поведение с/без регуляризации.",
        "Типичный **tabular / небольшой MLP** в проде: BN ускоряет и стабилизирует, dropout снижает переобучение. Паттерн `Linear → BN → ReLU → Dropout` до сих пор встречается в baseline-моделях и головах поверх энкодеров.",
    ),
}


def append_block(path: Path, what: str, why: str) -> None:
    text = path.read_text(encoding="utf-8")
    marker = "## Что это за задача"
    if marker in text:
        return
    block = f"""

## Что это за задача

{what}

## Зачем это в реальной жизни

{why}
"""
    path.write_text(text.rstrip() + block + "\n", encoding="utf-8")


def main() -> None:
    for rel, (what, why) in BLOCKS.items():
        p = ROOT / rel
        if not p.is_file():
            print("SKIP missing:", p)
            continue
        append_block(p, what, why)
        print("OK", rel)


if __name__ == "__main__":
    main()