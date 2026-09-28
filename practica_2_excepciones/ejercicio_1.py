# PYTHON INTERMEDIO
# Practica de Excepciones
# Quispe, Gerardo Fabián

# Ejercicio 1:
# Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultado = num1 / num2

    print(f"El resultado de la división es: {resultado}")
    
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    print("Por favor, ingrese un número diferente de cero para el segundo número.")
