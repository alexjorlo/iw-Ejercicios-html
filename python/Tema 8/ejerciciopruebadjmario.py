class futbol():
    def __init__(self):
        self.capitan=70000
        self.jugador=40000
        self.rival=30000

    def dineroconseguido(self,golesc,golesj):
        dinerocapitan=0
        dinerojugador=0
        dinerototal=0
        if golesc>=3:
            dinerocapitan=(golesc*self.capitan)+100000
            dinerojugador=golesj*self.jugador
            dinerototal=dinerocapitan+dinerojugador
            return dinerototal
            

        else:
            dinerocapitan=golesc*self.capitan
            dinerojugador=golesj*self.jugador
            dinerototal=dinerocapitan+dinerojugador
            return dinerototal

    def dineroperdido(self,goles):
        golesmetidos=0
        golesmetidos=goles*self.rival
        return golesmetidos


x=input("Cuantos goles has metido con el capitan: ")
golesc=int(x)
y=input("Cuantos goles has metido con el jugador: ")
golesj=int(y)
z=input("Cuantos goles te han metido : ")
goles=int(z)
mifutbol=futbol()
print(f"Has metido con el capitan {golesc} con el jugador {golesj} y goles en contra {goles}")
print(f"Has conseguido {mifutbol.dineroconseguido(golesc,golesj)} y has perdido {mifutbol.dineroperdido(goles)}")



