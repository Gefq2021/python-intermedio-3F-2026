# PYTHON INTERMEDIO
# Practica de Excepciones
# Quispe, Gerardo Fabián

# Ejercicio 5:
# Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    resultado = num1 / num2

    print(f"\nEl resultado de la división es: {resultado}\n")

except ZeroDivisionError:
    print("\nError: No se puede dividir entre cero.\n")
except ValueError:
    print("\nError: Ingrese un número válido.\n")
