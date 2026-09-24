# PYTHON INTERMEDIO
# Practica de Conjunto
# Quispe, Gerardo Fabián

# Ejercicio 3:
# Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.

A = {3, 5, 1, 7, 9}
B = {1, 4, 5, 6, 8, 3, 2}

print("A = ", A)
print("B = ", B)

print("\nElementos que se encuentran en A o en B, pero no en ambos:")
print(A.symmetric_difference(B))
