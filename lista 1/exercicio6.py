import math

def calcular_distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

ponto_a = (1, 2)
ponto_b = (4, 6)
print(f"Distância: {calcular_distancia(ponto_a, ponto_b)}")