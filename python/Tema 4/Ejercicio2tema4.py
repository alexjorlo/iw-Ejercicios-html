lista1=[]
lista2=[]
lista3=[]
a=input("Escribe un número: ")
n1=int(a)
b=input("Escribe un número: ")
n2=int(b)
c=input("Escribe un número: ")
n3=int(c)
d=input("Escribe un número: ")
n4=int(d)
e=input("Escribe un número: ")
n5=int(e)
lista1=[n1,n2,n3,n4,n5]
print(lista1)

f=input("Escribe un número: ")
n6=int(f)
g=input("Escribe un número: ")
n7=int(g)
h=input("Escribe un número: ")
n8=int(h)
i=input("Escribe un número: ")
n9=int(i)
j=input("Escribe un número: ")
n10=int(j)
lista2=[n6,n7,n8,n9,n10]
print(lista2)
for elemento1 in lista1:
    for elemento2 in lista2:
        if elemento1==elemento2:
            lista3.append(elemento1)
print(lista3)

