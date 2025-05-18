#Crear una función que reciba un número y
#retorne True si el número es primo, False en caso contrario.

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
num = int(input("Ingrese un número: "))

if es_primo(num):
    print(f"El número {num} es primo")
else:
    print(f"El número {num} NO es primo")