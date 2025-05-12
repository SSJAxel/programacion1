# Escribir una función que calcule el área de un rectángulo. 
# La función recibe la base y la altura y retorna el área

def rectanguloide(base_rectanguloide, altura_rectanguloide):
    return base_rectanguloide * altura_rectanguloide

base_rectanguloide = float(input("ingrese la base del rectanguloide: "))
altura_rectanguloide = float(input("ingrese la altura del rectanguloide: "))
area = rectanguloide(base_rectanguloide, altura_rectanguloide)
print(f"el area del rectanguloide es: {area}")