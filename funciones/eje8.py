
#Define una función que encuentre el máximo de tres números. 
# La función debe aceptar tres argumentos y devolver el número más grande



def mayor(a, b, c):
    if a >= b and a >= c:
     max = a 
    elif b >= c:
       max = b
    else:
        max = c  
        
    return max


a = int(input("ingrese un numero: "))
b = int(input("ingrese otro numero: "))
c = int(input("ingrese otro numero: "))    

print("el numero mas grande es: ", mayor(a,b,c))