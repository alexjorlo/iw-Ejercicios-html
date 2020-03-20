class Robot():
    def __init__(self):
        self.posicionx=0
        self.posiciony=0

    def posicionactual(self):
        return (f"Su posicion actual es {self.posicionx} y {self.posiciony}")

    def moverse(self,orden):
        if orden.__init__("a"):
            self.posicionx=self.posicionx+1
        elif orden.__init__("r"):
            self.posicionx=self.posicionx-1
        elif orden.__init__("d"):
            self.posiciony=self.posiciony+1
        elif orden.__init__("i"):
            self.posiciony=self.posiciony-1
mirobot=Robot()        
orden=""
while orden!="fin":
    orden=input("que te quieres mover: ")
    mirobot.moverse(orden)
    print(mirobot.posicionactual())
