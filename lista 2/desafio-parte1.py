import numpy as np

exercicio_1 = np.arange(10)
print("1. Array 0 a 9:", exercicio_1)

exercicio_2 = np.full((3, 3), True, dtype=bool)
print("\n2. Matriz 3x3 Booleana:\n", exercicio_2)

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
exercicio_3 = arr[arr % 2 != 0]
print("\n3. Apenas números ímpares:", exercicio_3)

arr_sub = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_sub[arr_sub % 2 != 0] = -1
exercicio_4 = arr_sub
print("\n4. Ímpares substituídos por -1:", exercicio_4)

exercicio_5 = np.random.randint(1, 101, (5, 5))
print("\n5. Matriz Aleatória 5x5:\n", exercicio_5)

exercicio_6 = np.sum(exercicio_5, axis=0)
print("\n6. Soma por coluna:", exercicio_6)

exercicio_7 = np.max(exercicio_5, axis=1)
print("\n7. Valor máximo por linha:", exercicio_7)

a = np.array([1, 2, 3, 4, 5])
exercicio_8 = a + 2
print("\n8. Resultado do Broadcasting (a + 2):", exercicio_8)

arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
exercicio_9 = np.concatenate([arr_a, arr_b])
print("\n9. Arrays concatenados:", exercicio_9)

arr_inv = np.array([10, 20, 30, 40])
exercicio_10 = arr_inv[::-1]
print("\n10. Array invertido:", exercicio_10)