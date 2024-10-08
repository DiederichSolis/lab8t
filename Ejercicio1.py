import time

def function(n):
    counter = 0
    # Calculamos el número de iteraciones basado en el tamaño de n
    num_k_iterations = int(n).bit_length()  # Este valor no cambia, se calcula una vez
    for i in range(n//2, n+1):
        for j in range(1, n//2 + 1):
            counter += num_k_iterations
    return counter

def measure_execution_time(input_sizes):
    execution_times = []
    for size in input_sizes:
        print(f"Ejecutando función para tamaño de entrada: {size}")
        start_time = time.time()  # Inicia el temporizador
        function(size)            # Ejecuta la función con el tamaño actual
        end_time = time.time()    # Termina el temporizador
        exec_time = end_time - start_time
        execution_times.append(exec_time)  # Calcula el tiempo de ejecución
        print(f"Tamaño {size} completado en {exec_time:.6f} segundos")
    return execution_times

# Tamaños de input 
input_sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]

# Medimos los tiempos de ejecución
execution_times = measure_execution_time(input_sizes)

# Mostrar resultados en tabla
print("\nTamaño de input | Tiempo de ejecución (s)")
for size, exec_time in zip(input_sizes, execution_times):
    print(f"{size:<15} | {exec_time:.6f}")
