#Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar

def par_no_par(numero):
    if numero % 2 == 0:
        print(f"el numero {numero} es par")
    else:
        print(f"el numero {numero} es impar")

numero = int(input("ingrese un numero: ")) 
par_no_par(numero)  