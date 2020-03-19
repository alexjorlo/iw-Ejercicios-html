class Triangulo:
    def __init__(self,ladoA, ladoB, ladoC,tipo,altura):
        self.ladoA = 0.0
        self.ladoB = 0.0
        self.ladoC = 0.0
        self.tipo=tipo
        self.altura=0.0
    
    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    
    def tipo(self):
        if tipo.__eq__("e"):
            self.tipo="Equilátero"
        elif tipo.__eq__("is"):
            self.tipo="Isóscel"
        elif tipo.__eq__("ir"):
            self.tipo="Irregular"

    def area(self):
        return (self.ladoB*self.altura)/2
    
x=input("Escribe el ladoA: ")
ladoA=float(x)
y=input("Escribe el ladoB: ")
ladoB=float(y)
z=input("Escribe el ladoC: ")
ladoC=float(z)
i=input("Escribe la altura: ")
altura=float(i)
tipo=input("Que triángulo quieres equilátero, isóscel o irregular e/ir/is: ")
triangulo=Triangulo(ladoA,ladoB,ladoC,tipo,altura)
altura=triangulo.altura
perimetro=triangulo.perimetro
print(f"El ladoA es {ladoA}, el lado B {ladoB}, el lado C {ladoC} y la altura {altura} y su tipo {tipo} ")
print(f"Su altura es {altura} y su perimetro {perimetro}")