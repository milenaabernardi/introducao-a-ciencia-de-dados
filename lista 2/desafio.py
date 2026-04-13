import numpy as np

vendas = np.random.randint(100, 501, 12)

matriz_vendas = vendas.reshape(3, 4)

total_semana = matriz_vendas.sum(axis=1)

media_dia = matriz_vendas.mean(axis=0)

dias_acima_400 = np.sum(matriz_vendas > 400)

print(f"Matriz:\n{matriz_vendas}")
print(f"Total/Semana: {total_semana}")
print(f"Média/Dia: {media_dia}")
print(f"Dias > 400: {dias_acima_400}")