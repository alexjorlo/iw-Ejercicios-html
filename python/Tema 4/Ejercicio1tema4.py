lista=[12,23,5,29,92,64]
lista.pop()
lista.insert(0,64)
print(lista)
lista.pop(1)
lista.insert(5,12)
print(lista)
lista.insert(0,14)
print(lista)
suma=0
for i in lista:
    suma=suma+i
print(suma)
lista.append(suma)
print(lista)
lista2=[4,11,32]
lista.extend(lista2)
print(lista)
while i < len(lista):
    if lista%2!=0:
        del lista[i]
print(lista)
lista.sort()
print(lista)
lista.clear()
print(lista)
