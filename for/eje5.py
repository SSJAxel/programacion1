#Ingresar un número y mostrar la tabla de multiplicar de ese número. 

num = int(input("ingrese un numero "))
result = 0
for numero in range(0, 11):
    result = numero * num
    print(num,"x",numero,"=",result)