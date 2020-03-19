diccionario={"lorea":"lorea","ander":"montero","juan":"hola"}
contralorea=diccionario["lorea"]
contraander=diccionario["ander"]
contrajuan=diccionario["juan"]
try:
    nombre=input("Escribe el nombre que quieres: ")
    if nombre.__eq__("lorea"):
        contraseña=input("Escribe su contraseña: ")
        if contraseña==contralorea:
            print("Usuario correcto")
        else:
            print("Usuario incorrecto")
    elif nombre.__eq__("ander"):
        contraseña=input("Escribe su contraseña: ")
        if contraseña==contraander:
            print("Usuario correcto")
        else:
            print("Usuario incorrecto")
    elif nombre.__eq__("juan"):
        contraseña=input("Escribe su contraseña: ")
        if contraseña==contrajuan:
            print("Usuario correcto")
        else:
            print("Usuario incorrecto")
except KeyError:
    print(f"No existe el elemento con la clave '{nombre}' en el diccionario.")