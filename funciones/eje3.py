#Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.

def elretorno():
    result = str(input("ingrese una cadena de texto"))
    return result

texto = elretorno()
print(f"la cadena ingresada es: {texto}")