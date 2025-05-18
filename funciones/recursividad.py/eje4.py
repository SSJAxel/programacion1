#Realizar una función para calcular el número de Fibonacci 
#de un número ingresado por consola. 
#La función deberá seguir el siguiente prototipo:
from input import get_int
def calcular_fibonacci(numero: int):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)


num2 = get_int("Ingrese un número: ")
print(f"El número de Fibonacci en la posición {num2} es: {calcular_fibonacci(num2)}")