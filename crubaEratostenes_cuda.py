import numpy as np
from numba import njit

@njit
def criba_eratostenes(n):
    # Crear un array booleano de tamaño n+1, inicialmente lleno de True
    primos = np.full(n + 1, True, dtype=np.bool_)
    primos[0] = primos[1] = False  # 0 y 1 no son primos
    
    # Aplicar el algoritmo de la criba
    for p in range(2, int(n ** 0.5) + 1):
        if primos[p]:
            # Marcar los múltiplos de p como no primos
            primos[p * p: n + 1: p] = False
    
    # Obtener los números primos
    return np.nonzero(primos)[0]

# Configurar numpy para mostrar todos los elementos sin truncarlos
np.set_printoptions(threshold=np.inf)

# Ejemplo: Encontrar los números primos hasta 10,000
n = 10000
primos_hasta_n = criba_eratostenes(n)
print(primos_hasta_n)
