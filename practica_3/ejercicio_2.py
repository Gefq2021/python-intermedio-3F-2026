# PYTHON INTERMEDIO
# Practica de Operadores Ternarios
# Quispe, Gerardo Fabián

# Ejercicio 2:

# Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario.

def buscar_palabra(palabra, *args):
    return f'La palabra "{palabra}" SI se encuentra en la lista.' if palabra in args else f'La palabra "{palabra}" NO se encuentra en la lista.'

palabra = input("Ingrese la palabra a buscar: ")
lista = list(input("Ingrese una lista de palabras separadas por espacios: ").split())

print(buscar_palabra(palabra, *lista))
