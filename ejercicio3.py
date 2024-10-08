import time

# Función para ejecutar la secuencia
def print_sequence(n):
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):
            pass  

# Lista de tamaños de entrada
input_sizes = [1, 10, 100, 1000, 10000, 100000]
execution_times = []

# Medición del tiempo de ejecución para cada tamaño
for n in input_sizes:
    start_time = time.perf_counter()  # Medición más precisa del tiempo
    print_sequence(n)
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    
    print(f"n = {n}, tiempo de ejecución = {execution_time:.5f} segundos")

# Mostrar los resultados en formato de tabla
print("\nTamaño de input (n) | Tiempo de ejecución (segundos)")
for n, execution_time in zip(input_sizes, execution_times):
    print(f"{n:<20} | {execution_time:.5f}")
