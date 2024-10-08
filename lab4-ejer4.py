# Función de búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Se retorna el índice si se encuentra el elemento
    return -1  # Se retorna -1 si no se encuentra el elemento

# Lista de ejemplo
lista = [10, 23, 45, 70, 11, 15, 30, 40, 55]

# Mejor caso: El objetivo está en la primera posición
objetivo_mejor = 10
print("Mejor caso:")
resultado_mejor = busqueda_lineal(lista, objetivo_mejor)
if resultado_mejor != -1:
    print(f"Elemento {objetivo_mejor} encontrado en el índice {resultado_mejor}.")
else:
    print(f"Elemento {objetivo_mejor} no encontrado.")

# Caso promedio: El objetivo está en alguna posición intermedia
objetivo_promedio = 30
print("\nCaso promedio:")
resultado_promedio = busqueda_lineal(lista, objetivo_promedio)
if resultado_promedio != -1:
    print(f"Elemento {objetivo_promedio} encontrado en el índice {resultado_promedio}.")
else:
    print(f"Elemento {objetivo_promedio} no encontrado.")

# Peor caso: El objetivo no está en la lista o está en la última posición
objetivo_peor = 100  # No existe en la lista
print("\nPeor caso:")
resultado_peor = busqueda_lineal(lista, objetivo_peor)
if resultado_peor != -1:
    print(f"Elemento {objetivo_peor} encontrado en el índice {resultado_peor}.")
else:
    print(f"Elemento {objetivo_peor} no encontrado.")
