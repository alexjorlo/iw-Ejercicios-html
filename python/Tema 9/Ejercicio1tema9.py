class vehículo:
    def __init__(self,km_recorridos):
        self.km_recorridos=0

class coche(vehículo):
    def __init__(self,km_recorridos,gasolina):
        self.gasolina=0
    
class bicicleta(vehículo):
    def __init__(self,km_recorridos,kilos):
        self.kilos=0
    
    def hincharruedas(self):
        if self.km_recorridos>=50:
            print("Hincha las ruedas vago")
        else:
            print("Continue")



decision=input("Que quieres escribir un coche o una bicicleta c/b: ")
if decision.__eq__("c"):
    x=input("Cuantos kilometros has recorrido: ")
    km_recorridos=int(x)
    y=input("Cuanta gasolina tiene: ")
    gasolina=int(y)
    micoche=coche(km_recorridos,gasolina)
    print(micoche)
    print(coche(km_recorridos,gasolina))
elif decision.__eq__("b"):
    x=input("Cuantos kilometros has recorrido: ")
    km_recorridos=int(x)
    y=input("Cuantos kilos pesa: ")
    kilos=int(y)
    mibici=bicicleta(km_recorridos,kilos)
    mibici.hincharruedas()
    print(mibici)
else:
    print("Te has confundido")



