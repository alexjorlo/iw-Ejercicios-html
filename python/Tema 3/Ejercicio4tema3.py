
usuario=str("root")
contraseña=str("root")
intento=3
while(intento>0):
   X=str(input("Escriba el usuario: "))
   Y=str(input("Escriba la contraseña: "))
   if X.__eq__(usuario) and Y.__eq__(contraseña):
      print("Bienvenido")

   
   else:
      print("error")
      intento=intento-1
      print(f"Te quedan {intento} intentos")
   if (intento==0):
         print("Te has quedado sin oportunidades")
