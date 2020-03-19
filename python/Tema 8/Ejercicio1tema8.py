class coches:
    matricula="VI0959N"
    marca="Renault Clio"
    kilometros_recorridos=96518.14
    gasolina=35.8

    def avanzar(kilometros_recorridos,gasolina):
        x=input("Cuantos kilometros vas a recorrer: ")
        kilometros=float(x)
        kilometros_recorridos=(kilometros+kilometros_recorridos-gasolina)*0.1
        print(coches())
    def repostar(gasolina):
        y=input("Cuantos litro le vas a echar: ")
        litros=float(y)
        gasolina=gasolina+litros
        if gasolina>0:
            print("Hay que repostar")
        else:
            print("Todo correcto")

    print(f"La matricula es {coches.matricula}")
    print(f"La marca es {coches.marca}")
    print(f"Los kilometros recorridos son {coches.kilometros_recorridos}")
    print(f"La gasolina que tiene es {gasolina}")
