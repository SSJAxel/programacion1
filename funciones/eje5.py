#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como
#parámetro y devolver el área

def Calcular_area_circulo(radio):
    pi = 3.1416 #aproximacion nada mas
    return pi * radio**2

radio = float(input("ingrese el radio del circulo: "))
area = Calcular_area_circulo(radio)
print(f"el area del circulo es: {area}") 