class poligono():
    def __init__(self,color):
        self.color=color

class cuadrado(poligono):
    def __init__(self,color,lado):
        self.lado=int(lado)
    def area(self):
        return self.lado*self.lado
    def perimetro(self):
        return self.lado+self.lado+self.lado+self.lado

class triangulo(poligono):
    def __init__(self,color,ladoA,ladoB,ladoC,altura):
        self.ladoA=int(ladoA)
        self.ladoB=int(ladoB)
        self.ladoC=int(ladoC)
        self.altura=int(altura)
    
    def area(self):
        return (self.ladoB*self.altura)/2
    def perimetro(self):
        return self.ladoA+self.ladoB+self.ladoC


figura=input("Que quieres añadir cuadrado o triangulo c/t: ")
if figura.__eq__("c"):
    x=input("Cuanto quieres que valga el lado: ")
    lado=int(x)
    colorcuadrado=input("De que color quieres que sea: ")
    micuadrado=cuadrado(colorcuadrado,lado)
    print(f"El lado que has puesto es {lado} m y su color es {colorcuadrado}")
    print(f"Su area es {micuadrado.area()}")
    print(f"Su perimetro es {micuadrado.perimetro()}")

elif figura.__eq__("t"):
    a=input("Cuanto quieres que valga el ladoA: ")
    ladoA=int(a)
    b=input("Cuanto quieres que valga el ladoB: ")
    ladoB=int(b)
    c=input("Cuanto quieres que valga el ladoC: ")
    ladoC=int(c)
    r=input("Cuanto quieres que valga el altura: ")
    altura=int(r)
    colortriangulo=input("De que color quieres que sea: ")
    mitriangulo=triangulo(colortriangulo,ladoA,ladoB,ladoC,altura)
    print(f"El ladoA que has puesto es {ladoA}, El ladoB que has puesto es {ladoB} y El ladoC que has puesto es {ladoC}")
    print(f"Su altura es {altura} m y su color es {colortriangulo}")
    print(f"Su area es {mitriangulo.area()}")
    print(f"Su perimetro es {mitriangulo.perimetro()}")

else:
    print("no has elegido ninguno")
