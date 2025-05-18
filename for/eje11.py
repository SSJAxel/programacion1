#Ingresar un número. Determinar si el número es primo o no.

num = int(input("Ingrese un número: "))
es_primo = True

if num <= 1:
    es_primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break