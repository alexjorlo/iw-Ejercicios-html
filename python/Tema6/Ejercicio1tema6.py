



def esPrimo(n1):
    i=2
    n=n1
    while i<n and n%i!=0:
        i=i+1
    if i==n1:
        print(f"{n} es primo")
    else:
        print(f"{n} no es primo")
  
  

x=input("Escribe un número: ")
n1=int(x)
esPrimo(n1)