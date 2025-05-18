#Crear una función que (utilizando el algoritmo del ejercicio de la guia de for)
#muestre todos los números primos comprendidos entre
#la unidad y un número ingresado como parámetro. 
#La función retorna la cantidad de números primos encontrados. 
#Modularizar todo lo posible.
def es_primo(num1):
    for i in range (2, num1):
        if num1 % i == 0:
            return False
    return True
def todos_primos(num):
    contadordeprimos = 0
    for i in range(2, num + 1):
        if es_primo(i):
            print(i)
            contadordeprimos += 1
    return contadordeprimos
num = int(input("Ingrese un número: "))
cantidad = todos_primos(num)
print(f"Se encontraron {cantidad} números primos.")