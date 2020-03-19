lista=[6,14,11,3,2,1,15,19]
try:
    x=input("Escribe un número para la lista recuerda que empieza en 0 y acaba en 7: ")
    numero=int(x)
    recorrer=lista[numero]
    print(recorrer)
except IndexError:
    print("Numero fuera de rango")