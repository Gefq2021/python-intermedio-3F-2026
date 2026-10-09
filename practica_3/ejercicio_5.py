# PYTHON INTERMEDIO
# Practica de Operadores Ternarios
# Quispe, Gerardo Fabián

# Ejercicio 5:
# Imprimir un mensaje de error si no se pasan suficientes argumentos

def imprimir_mensaje_error(*args):
    return "Error: No se han pasado suficientes argumentos." if len(args) < CANTIDAD_ARGUMENTOS else "Se han pasado suficientes argumentos."

CANTIDAD_ARGUMENTOS = 4

argumentos = list(input(f"Ingrese {CANTIDAD_ARGUMENTOS} elementos separados por espacios: ").split())

print(imprimir_mensaje_error(*argumentos))
