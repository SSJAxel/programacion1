#Diseña una función que calcule la potencia de un número
# La función debe recibir la base y el exponente
# como argumentos y devolver el resultado.

def potencia(a,b):
    elevado = a ** b

    return elevado

numero = int(input("ingrese un numero: "))
elevar = int(input("ingrese la potencia: "))

print(f"el numero {numero} elevado por {elevar} es : {potencia(numero, elevar)}")