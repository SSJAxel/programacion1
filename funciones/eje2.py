#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def elretorno():
    result = float(input("ingrese un numero flotante "))
    return result

numero = elretorno()
print(f"el numero flotante ingresado es:{numero}") 