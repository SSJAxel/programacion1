#Realizar una función recursiva que permita
#realizar la suma de los dígitos de un número:
from input import get_int
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
num = get_int("Ingrese un número: ")
print(f"La suma de los dígitos es: {suma_digitos(num)}")