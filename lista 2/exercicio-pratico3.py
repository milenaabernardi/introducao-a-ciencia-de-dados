import numpy as np

np.random.seed(42)

m = np.random.randn(5, 5)

print(f"Média geral: {m.mean():.3f}")
print(f"Desvio padrão geral: {m.std():.3f}")

print(f"Média por coluna: {m.mean(axis=0)}")

print(f"Máximo/Mínimo: {m.max():.2f} / {m.min():.2f}")

positivos = (m > 0).sum()
print(f"Quantidade de positivos: {positivos}")