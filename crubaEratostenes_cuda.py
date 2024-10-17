import cupy as cp

def criba_eratostenes(n):
    # Crear un array booleano de tamaño n+1, inicialmente lleno de True
    primos = cp.full(n + 1, True, dtype=cp.bool_)
    primos[0] = primos[1] = False  # 0 y 1 no son primos
    
    # Aplicar el algoritmo de la criba
    for p in range(2, int(n ** 0.5) + 1):
        if primos[p]:
            # Marcar los múltiplos de p como no primos
            primos[p * p: n + 1: p] = False
    
    # Obtener los números primos
    return cp.nonzero(primos)[0]

# Configurar cupy para mostrar todos los elementos sin truncarlos
cp.set_printoptions(threshold=cp.inf)

# Ejemplo: Encontrar los números primos hasta 10,000
n = 10000
primos_hasta_n = criba_eratostenes(n)
print(primos_hasta_n)
