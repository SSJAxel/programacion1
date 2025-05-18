#Realizar una función recursiva que calcule 
# la suma de los primeros números naturales:
from input import get_int
def suma_naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_naturales(n - 1)

num = get_int("ingrese un numero: ")
print(suma_naturales(num))