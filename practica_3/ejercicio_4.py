# PYTHON INTERMEDIO
# Practica de Operadores Ternarios
# Quispe, Gerardo Fabián

# Ejercicio 4:

# Calcular el promedio de una lista de números usando args y un operador ternario

def calcular_promedio(*args):
    return sum(args) / len(args) if len(args) > 0 else 0

numeros = list(input("Ingrese una lista de números separados por espacios: ").split())

lista_numeros = [float(num) for num in numeros]

print(f"El promedio de los números es: {calcular_promedio(*lista_numeros)}")