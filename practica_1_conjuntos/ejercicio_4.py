# PYTHON INTERMEDIO
# Practica de Conjunto
# Quispe, Gerardo Fabián

# Ejercicio 4:
# Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.

A = {3, 5, 1, 7, 9}
B = {1, 4, 5, 6, 8, 3, 2}

print("A = ", A)
print("B = ", B)

print("A es subconjunto de B: " ,A.issubset(B))
print()

C = {1, 2, 3, 4}
D = {1, 2, 3, 4, 5, 6}

print("C = ", C)
print("D = ", D)

print("C es subconjunto de D: " , C.issubset(D))
