import numpy as np

arr = np.array([3, 7, 1, 9, 4, 6, 2, 8, 5, 10])

media = arr.mean()
soma  = arr.sum()
dp    = arr.std()

print(f"Média:         {media:.2f}")
print(f"Soma:          {soma}")
print(f"Desvio Padrão: {dp:.2f}")