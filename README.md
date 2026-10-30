# Curso de Python Intermedio - Tecno3F

Repositorio destinado a la entrega de prácticas y ejercicios del curso de Python Intermedio.

## Estudiante
* **Nombre:** Gerardo Fabián Quispe
* **Año:** 2026

## Información del curso

Este repositorio contiene las actividades prácticas desarrolladas durante el cursado.

### Contenido

| Práctica | Tema |
|-----------|------|
| Practica 1 | Conjuntos |
| Practica 2 | Excepciones |
| Practica 3 | Operadores Ternarios |
| Practica 4 | POO |

## Entregas

### Práctica 1 - Conjuntos

#### Ejercicio 1:

Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos.

**Archivo:** `ejercicio_1.py`

#### Ejercicio 2

Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A y en B.

**Archivo:** `ejercicio_2.py`

#### Ejercicio 3

Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.

**Archivo:** `ejercicio_3.py`

#### Ejercicio 4

Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.

**Archivo:** `ejercicio_4.py`

#### Ejercicio 5

Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto.

**Archivo:** `ejercicio_5.py`

### Practica 2 - Excepciones

#### Ejercicio 1:

Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

#### Ejercicio 2:

Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

#### Ejercicio 3:

Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra un mensaje de error al usuario.

#### Ejercicio 4:

Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.

#### Ejercicio 5:

Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

### Práctica 3 - Operadores Ternarios

#### Ejercicio 1:

Calcular el mayor de dos números ingresados por teclado usando un operador ternario.

**Archivo:** `./practica_3/ejercicio_1.py`

#### Ejercicio 2

Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario.

**Archivo:** `./practica_3/ejercicio_2.py`

#### Ejercicio 3

Determinar si un número es par o impar.

**Archivo:** `./practica_3/ejercicio_3.py`

#### Ejercicio 4

Calcular el promedio de una lista de números usando args y un operador ternario.

**Archivo:** `./practica_3/ejercicio_4.py`

#### Ejercicio 5

Imprimir un mensaje de error si no se pasan suficientes argumentos.

**Archivo:** `./practica_3/ejercicio_5.py`

### Práctica 4 - POO

#### Desafio Integrador: Sistema Bancario POO

1. Clase Base Abstracta: CuentaBancaria (ABC)
    - Atributos protegidos: _titular, _cbu, _saldo
    - Decoradores: @property y  @saldo.setter con validaciones
    - Método concreto: depositar(monto) y __str__()
2. Subclases que heredan y aplican Polimorfismo:
    - CuentaAhorro: extraer() solo si hay saldo suficiente. Agregar aplicar_interes() con tasa fija (ej: 0.1% -> 0.001).
    - CuentaCorriente: agrega limite_descuento. Permite extraer hasta agotar el saldo + descubierto.
    - CuentaCheque: cobra una comision administrativa fija por cada extracción exitosa.
