import numpy as np

temps = np.array([22, 24, 21, 23, 25, 20, 22])
print(f"1. Média: {temps.mean():.2f} | Máxima: {temps.max()}")

vendas = np.random.randint(50, 201, (3, 4))
total_por_produto = vendas.sum(axis=1)
print(f"\n2. Total por produto: {total_por_produto}")

notas = np.array([75, 88, 92, 65, 70, 80, 95, 60, 85, 78])
print(f"\n3. Mínima: {notas.min()} | Máxima: {notas.max()}")

leituras = np.random.rand(20)
acima_setenta = leituras[leituras > 0.7]
print(f"\n4. Leituras > 0.7: {acima_setenta}")

precos = np.array([120.50, 121.00, 119.80, 122.30, 120.00])
variacao = (np.diff(precos) / precos[:-1]) * 100
print(f"\n5. Variação percentual diária: {variacao}")

identidade = np.eye(4)
print(f"\n6. Matriz Identidade 4x4:\n{identidade}")

zeros = np.zeros((3, 3))
uns = np.ones((2, 5))
print(f"\n7. Zeros 3x3:\n{zeros}\nUns 2x5:\n{uns}")

dados_img = np.random.randint(0, 256, 25)
matriz_img = dados_img.reshape(5, 5)
print(f"\n8. Matriz 5x5:\n{matriz_img}")

arr_9 = np.arange(10)
pares = arr_9[arr_9 % 2 == 0]
print(f"\n9. Números pares: {pares}")

arr_10 = np.array([1, 2, 3, 4, 5])
acumulada = np.cumsum(arr_10)
print(f"\n10. Soma acumulada: {acumulada}")

arr_11 = np.array([1, 2, 2, 3, 4, 4, 4, 5])
unicos = np.unique(arr_11)
print(f"\n11. Valores únicos: {unicos}")

espacados = np.linspace(0, 10, 5)
print(f"\n12. Linspace (0 a 10, 5 elementos): {espacados}")

notas_p = np.array([80, 90, 70])
pesos = np.array([0.3, 0.5, 0.2])
media_pond = np.average(notas_p, weights=pesos)
print(f"\n13. Média ponderada: {media_pond}")

matriz_2x3 = np.array([[1, 2, 3], [80, 90, 85]]) # ex: tempo vs nota
transposta = matriz_2x3.T
print(f"\n14. Matriz transposta (agora 3x2):\n{transposta}")

matriz_3x4 = np.arange(12).reshape(3, 4)
invertida_eixo0 = np.flip(matriz_3x4, axis=0)
print(f"\n15. Matriz original:\n{matriz_3x4}\nInvertida no eixo 0:\n{invertida_eixo0}")

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
iguais = (a == b)
print(f"\n16. Onde os arrays são iguais? {iguais}")

arr_rand = np.random.randint(0, 101, 10)
mascara = arr_rand > 50
print(f"\n17. Array: {arr_rand} | Maiores que 50: {arr_rand[mascara]}")

arr_setes = np.array([1, 7, 3, 7, 5, 7])
contagem = np.count_nonzero(arr_setes == 7)
print(f"\n18. O número 7 aparece {contagem} vezes.")

decimais = np.array([1.23, 2.78, 3.50, 4.11])
arredondados = np.round(decimais)
print(f"\n19. Arredondados: {arredondados}")

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
combinado = np.vstack((v1, v2))
print(f"\n20. Arrays empilhados verticalmente:\n{combinado}")