#1Crear una función que le solicite al usuario el 
# ingreso de un número entero y lo retorne.
#2Crear una función que le solicite al usuario el 
# ingreso de un número flotante y lo retorne.
#3Crear una función que le solicite al usuario el 
# ingreso de una cadena y la retorne. 

#Especializar las funciones del punto 1, 2 y 3 
#para hacerlas reutilizables. Agregar validaciones

def enteros(valor="ingrese un valor entero: "):
    while True:
        try:
            return int(input(valor))
        except ValueError:
            print("¡Error! Debe ingresar un número entero válido.")


def flotantes(valor_f="ingres un valor flotante"):
    while True:
        try:
            return float(input(valor_f))
        except ValueError:
            print("¡Error! Debe ingresar un número flotante válido.")


def cadenas_texto(texto="ingrese una cadena de texto: "):
    while True:
        resultado = input(texto)
        if resultado.strip() != "":
            return resultado
        print("¡Error! Debe ingresar una cadena de texto no vacía.")

print(f"prueba {enteros()},{flotantes()}, {cadenas_texto()}")