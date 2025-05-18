#Crear una función que imprima la tabla de multiplicar de 
# un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales 
# (inicio y fin) para definir el rango de multiplicación. 
#Por defecto es del 1 al 10.

def tabla_multi(num,iniciar=1, final=10):
    for i in range(iniciar, final + 1):
        print(f"{num} x {i} = {num * i}")
num = int(input("Ingrese el número para ver su tabla: "))
inicio = int(input("Ingrese desde qué número quiere las tablas: "))
fin = int(input("Ingrese hasta qué número: "))
tabla_multi(num, inicio, fin)