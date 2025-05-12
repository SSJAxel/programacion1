#Crea una función que verifique si un número dado es par o impar. 
# La función retorna True si el número es par, False en caso contrario

def par_no_par(numero):
    if numero % 2 == 0:
        print(f"true")
    else:
        print(f"false")

numero = int(input("ingrese un numero: ")) 
par_no_par(numero)