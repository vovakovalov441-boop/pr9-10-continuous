import math
import numpy as np
import matplotlib.pyplot as plt

LAM = 0.05
M_X, D_X = 1 / LAM, 1 / LAM**2
SIGMA = math.sqrt(D_X)
P_GT_30 = math.exp(-LAM * 30)


def block2(n, rng):
    x = rng.exponential(1 / LAM, n)
    m, d = x.mean(), x.var()
    p = (x > 30).mean()
    print("\nБлок 2. MTBF сервера, X ~ Exp(0.05), N =", n)
    print("M[X]: W =", round(m, 4), "P =", round(M_X, 4), "похибка:", round(abs(m - M_X), 4))
    print("D[X]: W =", round(d, 4), "P =", round(D_X, 4), "похибка:", round(abs(d - D_X), 4))
    print("σ[X]: W =", round(math.sqrt(d), 4), "P =", round(SIGMA, 4), "похибка:", round(abs(math.sqrt(d) - SIGMA), 4))
    print("P(X > 30): W =", round(p, 4), "P =", round(P_GT_30, 4), "похибка:", round(abs(p - P_GT_30), 4))

    t = np.linspace(0, 150, 500)
    plt.figure(figsize=(9, 5))
    plt.hist(x, bins=150, range=(0, 150), density=True, alpha=0.6, label="Гістограма вибірки")
    plt.plot(t, LAM * np.exp(-LAM * t), color="red", label="f(x) = 0,05·e^(-0,05x)")
    plt.axvline(30, color="black", ls="--", label="x = 30 год")
    plt.title("Блок 2. Щільність розподілу MTBF, Exp(0,05)")
    plt.xlabel("Час безвідмовної роботи, год")
    plt.ylabel("Щільність f(x)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("graphics/block2_mtbf.png", dpi=150)
    return m, d, p