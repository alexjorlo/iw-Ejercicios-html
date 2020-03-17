usuario={ 
    "iperurena":{
        "nombre":"Iñaki",
            "apellido":"Perurena",
            "contraseña":"123123"
    },
    "fmuguruza":{
        "nombre":"Fermin",
            "apellido":"Muguruza",
            "contraseña":"654321"
    },
    "solaizola":{
        "nombre":"Aimar",
            "apellido":"Olaizola",
            "contraseña":"123456"
    }
}
intentos=3
while intentos!=0:
    nombre=input("Escribe su nombre: ")
    contraseña=input("Escribe su contraseña: ")
    if nombre.__eq__("iñaki") and contraseña.__eq__("123123"):
        for i in usuario:
            datos1=usuario["iperurena"]
        print(f"Sus datos son: {datos1}")
   
    elif nombre.__eq__("fermin") and contraseña.__eq__("654321"):
        for i in usuario:
            datos2=usuario["fmuguruza"]
        print(f"Sus datos son: {datos2}")
   
    elif nombre.__eq__("aimar") and contraseña.__eq__("123456"):
        for i in usuario:
            datos3=usuario["solaizola"]
        print(f"Sus datos son: {datos3}")
    else:
        intentos=intentos-1
        print(f"Te quedan {intentos} intentos")

