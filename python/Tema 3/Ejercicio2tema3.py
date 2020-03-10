n1=input("Escribe un número entero de principio: ")
X=int(n1)
n2=input("Escribe otro número entero: ")
Y=int(n2)
contador=0
while(X<=Y):
    contador=contador + X
    X=X+1
print(f"La diferencia es: {contador}")
        