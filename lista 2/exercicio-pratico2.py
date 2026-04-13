import numpy as np

arr = np.array([14, 3, 22, 8, 17, 5, 30, 11, 25, 9])

media = arr.mean()
print(f"Média: {media}")

acima = arr[arr > media]
print(f"Valores acima da média: {acima}")

contagem = len(acima)
print(f"Quantidade de valores acima da média: {contagem}")