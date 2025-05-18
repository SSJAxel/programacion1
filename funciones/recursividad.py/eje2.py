#Realizar una función recursiva
#que calcule la potencia de un número:
from input import get_int
def potencia(num, potenciador):
    if potenciador == 0:
        return 1
    else:
        return num * potencia(num, potenciador - 1)

num1 = get_int("Ingrese el numero a elevar: ")
potenciador = int(input("Ingrese el exponente: "))
print(f"{num1} elevado a la {potenciador} es: {potencia(num1, potenciador)}")