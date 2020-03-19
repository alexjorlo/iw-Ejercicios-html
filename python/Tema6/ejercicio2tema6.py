import random

numero=random.randrange(10)
contador=0
usuario=-1




def adivinarNumero(usuario,numero):
    if usuario<numero:
        print("Tu número es mayor del que estamos pensando")
    elif usuario>numero: 
        print("Tu número es menor del que estamos pensando")
    elif usuario==numero:
        print(f"Has acetado el número has dicho es {usuario} y pensabamos en {numero} ")

while usuario!=numero:
    usuario=int(input("Escribe un número para adivinar: "))
    contador=contador+1
    
    adivinarNumero(usuario,numero)
print(f"Has hecho {contador} veces para resolverlo")
    