import math
import os
import matplotlib.pyplot as plt
import numpy as np
from block2_variants import block2

rng = np.random.default_rng(42)
N = 100000
os.makedirs("graphics", exist_ok=True)


def moments(z):
    c = z - z.mean()
    s = c.std()
    return z.mean(), z.var(), (c**3).mean() / s**3, (c**4).mean() / s**4 - 3


print("Блок 1. Перевірка ЦГТ, N =", N)
K_VALUES = [1, 2, 5, 12, 30]
grid = np.linspace(-4, 4, 400)
phi = np.exp(-grid**2 / 2) / math.sqrt(2 * math.pi)
fig, ax = plt.subplots(1, 5, figsize=(18, 4), sharey=True)
for i, k in enumerate(K_VALUES):
    s = rng.random((N, k)).sum(axis=1)
    z = (s - 0.5 * k) / math.sqrt(k / 12)
    m, d, skew, kurt = moments(z)
    print("k =", k, "M =", round(m, 4), "D =", round(d, 4), "Skewness =", round(skew, 4),
          "Kurtosis =", round(kurt, 4), "(теорія:", round(-1.2 / k, 4), ")")
    ax[i].hist(z, bins=80, range=(-4, 4), density=True, alpha=0.6, label="Гістограма Zk")
    ax[i].plot(grid, phi, color="red", label="φ(z)")
    ax[i].set_title(f"k = {k}")
    ax[i].set_xlabel("z")
ax[0].set_ylabel("Щільність")
ax[0].legend()
fig.suptitle("Блок 1. Збіжність Zk до N(0, 1)")
plt.tight_layout()
plt.savefig("graphics/block1_clt.png", dpi=150)

block2(N, rng)

print("\nБлок 3. Перцентильний аналіз затримок, N =", N)
gc = rng.random(N) < 0.10
latency = np.where(gc, rng.exponential(100, N), rng.normal(20, 4, N))
p = np.percentile(latency, [50, 90, 95, 99])
print("Середнє =", round(latency.mean(), 2), "мс, σ =", round(latency.std(), 2), "мс")
print("p50 =", round(p[0], 2), "p90 =", round(p[1], 2), "p95 =", round(p[2], 2), "p99 =", round(p[3], 2), "мс")

fig, ax = plt.subplots(1, 2, figsize=(14, 5))
ax[0].hist(latency, bins=200, range=(0, 300), density=True, alpha=0.6, label="Гістограма затримок")
xs = np.sort(latency)
ax[1].plot(xs, np.arange(1, N + 1) / N, label="F(x), емпірична")
for a in ax:
    for q, val, c in zip(["p50", "p90", "p95", "p99"], p, ["green", "orange", "red", "purple"]):
        a.axvline(val, color=c, ls="--", label=f"{q} = {val:.1f} мс")
    a.set_xlim(0, 300)
    a.set_xlabel("Затримка, мс")
    a.legend()
ax[0].set_title("Блок 3. Щільність розподілу затримок")
ax[0].set_ylabel("Щільність")
ax[1].set_title("Блок 3. Функція розподілу F(x)")
ax[1].set_ylabel("F(x)")
plt.tight_layout()
plt.savefig("graphics/block3_latency.png", dpi=150)

print("\nБлок 4. Час роботи від UPS, X ~ Exp(0.25), N =", N)
t = rng.exponential(1 / 0.25, N)
w4 = (t > 6).mean()
p4 = math.exp(-0.25 * 6)
print("M[X] =", round(t.mean(), 4), "P(X > 6): W =", round(w4, 4), "P =", round(p4, 4),
      "похибка:", round(abs(w4 - p4), 4))

plt.show()
