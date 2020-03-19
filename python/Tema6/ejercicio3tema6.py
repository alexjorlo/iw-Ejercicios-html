def numeroEnRango(min, max, numero):
    return numero <= max and numero >=min

def numeroEnLista(lista, numero):
    for el in lista:
        if el == numero:
            return True

lista = [6,14,11,3,2,1,15,19]
min = 1
max = 20
numero = int(input(f"Escribe un número entre el {min} y el {max}: "))
if numeroEnRango(min, max, numero):
   if numeroEnLista(lista, numero):
       print("El número está en la lista")
   else:
       print("el número no está en la lista")
else:
    print("El número no se encuentra en el rango indicado.")
