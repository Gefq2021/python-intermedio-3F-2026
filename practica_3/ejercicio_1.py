# PYTHON INTERMEDIO
# Practica de Operadores Ternarios
# Quispe, Gerardo Fabián

# Ejercicio 1:
# Calcular el mayor de dos números ingresados por teclado usando un operador ternario.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

mayor = num1 if num1 > num2 else num2

print(f"\nEl mayor de los dos números es: {mayor}\n")
