# PYTHON INTERMDIO
# Practica de Excepciones
# Quispe, Gerardo Fabián

# Ejercicio 2:
# Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

try:
    num_1 = int(input("Ingrese un número: "))
    cadena = input("Ingrese una cadena: ")

    resultado = num_1 + cadena

    print("El resultado de la suma es:", resultado)
    
except TypeError:
    print("Error: No se puede sumar un número y una cadena. Por favor, ingrese valores válidos.")
