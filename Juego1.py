import random
d=int(input("ingrese la fila. Debe ser un numero del 1 al 9"))
y=int(input("ingrese la columna. Debe ser un numero del 1 al 9"))
e=0
mtz=[]

for K in range (0,10):
    for j in range (0,10):
        n=random.randrange(0,99)
        mtz.append(n)
        print (n, end=" ")
            
        if d==K and y==j:
            jugada=n
        else:
            dy=(d,K)
    print(" ")
print('el numero ganador es:',jugada)
print('en la ubicación:',dy)
