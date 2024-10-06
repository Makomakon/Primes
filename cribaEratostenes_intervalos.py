def criba_eratostenes(n):
    # Crear una lista booleana para marcar si los números son primos
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False  # 0 y 1 no son primos

    # Implementar la Criba de Eratóstenes
    for p in range(2, int(n**0.5) + 1):
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False

    # Devolver la lista de números primos
    return [p for p, is_prime in enumerate(primos) if is_prime]

def calcular_intervalos(primos):
    # Calcular los intervalos entre primos consecutivos
    intervalos = [primos[i+1] - primos[i] for i in range(len(primos) - 1)]
    return intervalos

def encontrar_maximo_intervalo(intervalos, primos):
    # Encontrar el intervalo máximo y los números entre los que ocurre
    max_intervalo = max(intervalos)
    indice_max = intervalos.index(max_intervalo)
    primo_1 = primos[indice_max]
    primo_2 = primos[indice_max + 1]
    return max_intervalo, primo_1, primo_2

# Función principal
def primos_y_intervalos(n):
    # Obtener los números primos hasta n usando la Criba de Eratóstenes
    primos = criba_eratostenes(n)
    
    # Calcular los intervalos entre primos consecutivos
    intervalos = calcular_intervalos(primos)
    
    # Encontrar el intervalo máximo
    max_intervalo, primo_1, primo_2 = encontrar_maximo_intervalo(intervalos, primos)
    
    # Resultados
    print(f"Primos hasta {n}: {primos}")
    print(f"Intervalos entre primos consecutivos: {intervalos}")
    print(f"Máximo intervalo: {max_intervalo} entre los primos {primo_1} y {primo_2}")

# Ejecutar con un valor máximo de n
n = 10000  # Puedes cambiar el valor de n para probar otros límites
primos_y_intervalos(n)
