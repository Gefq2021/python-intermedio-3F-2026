# PYTHON INTERMEDIO
# Practica de Excepciones
# Quispe, Gerardo Fabián

# Ejercicio 4:
# Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.

try:
    archvivo = input("Ingrese el nombre del archivo que desea abrir, con su extensión: ")
    with open(archvivo, "r") as f:
        contenido = f.read()
        print(contenido)

except FileNotFoundError:
    print(f"Error: El archivo {archvivo} no existe.")
    try:
        with open(archvivo, "w") as f:
            f.write("Contenido del archivo.")
        print(f"\nEl archivo {archvivo} se ha creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")
