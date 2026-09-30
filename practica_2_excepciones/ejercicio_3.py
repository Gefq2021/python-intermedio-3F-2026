# PYTHON INTERMEDIO
# Practica de Excepciones
# Quispe, Gerardo Fabián

# Ejercicio 3:
# Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra un mensaje de error al usuario.

dic = {"nombre": "Fabian", 
       "edad": 42, 
       "ciudad": "Monterrico"
       }

try:
    clave = input("Ingrese la clave que desea buscar en el diccionario: ")
    valor = dic[clave]

    print(f"\n'{clave}': {valor}\n")

except KeyError:
    print("\nError: La clave ingresada no existe en el diccionario.\n")
