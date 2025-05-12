# Ejercicio 1: Función que suma dos números
def sumar(a, b):
    return a + b

# Prueba
print(sumar(3, 5))  # Salida: 8


# Ejercicio 2: Función que verifica si un número es par
def es_par(numero):
    return numero % 2 == 0

# Prueba
print(es_par(4))  # Salida: True
print(es_par(7))  # Salida: False


# Ejercicio 3: Función que calcula el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Prueba
print(factorial(5))  # Salida: 120


# Ejercicio 4: Función que invierte una cadena
def invertir_cadena(cadena):
    return cadena[::-1]

# Prueba
print(invertir_cadena("hola"))  # Salida: "aloh"


# Ejercicio 5: Función que encuentra el mayor de tres números
def mayor_de_tres(a, b, c):
    return max(a, b, c)

# Prueba
print(mayor_de_tres(3, 7, 5))  # Salida: 7


# Ejercicio 6: Función que cuenta las vocales en una cadena
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cadena if letra in vocales)

# Prueba
print(contar_vocales("programacion"))  # Salida: 5


# Ejercicio 7: Función que verifica si una palabra es un palíndromo
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# Prueba
print(es_palindromo("anita lava la tina"))  # Salida: True
print(es_palindromo("hola"))  # Salida: False