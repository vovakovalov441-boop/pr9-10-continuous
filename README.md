# ПР 9-10. Неперервні випадкові величини, закони розподілу та статистичне моделювання в аналізі продуктивності ПЗ

Ковальов Володимир, група ЗІПЗ-25-1. Варіант 13: Блок 2 — варіант 2 (MTBF сервера, Exp), Блок 4 — варіант 2 (час від UPS, Exp).

## Що робить програма
| Блок | Файл | Зміст |
|---|---|---|
| 1 | `PythonApplication1.py` | Перевірка ЦГТ: Zk для сум k рівномірних величин, k = 1, 2, 5, 12, 30; гістограми з φ(z), M, D, асиметрія, ексцес |
| 2 | `block2_variants.py` | MTBF X ~ Exp(0,05): M[X], D[X], σ[X], P(X > 30), гістограма і щільність f(x) |
| 3 | `PythonApplication1.py` | Latency Tail Analysis: суміш N(20, 4²) і Exp(0,01), перцентилі p50, p90, p95, p99, графіки f(x) і F(x) |
| 4 | `PythonApplication1.py` | Час роботи від UPS X ~ Exp(0,25): P(X > 6) на 100 000 симуляцій |

## Запуск
```
pip install -r requirements.txt
cd PythonApplication1
python PythonApplication1.py
```
Результати виводяться в консоль, графіки зберігаються в `PythonApplication1/graphics/`.

## Структура
```
├── PythonApplication1.sln
├── PythonApplication1/
│   ├── PythonApplication1.py
│   ├── block2_variants.py
│   └── graphics/
│       ├── block1_clt.png
│       ├── block2_mtbf.png
│       └── block3_latency.png
├── report/
│   └── PR9-10_Report_Kovalov_Volodymyr.pdf
├── README.md
├── requirements.txt
└── .gitignore
```
