diccionario={"Mikel":3,"Ane":8, "Amaia":12, "Unai":5, "Jon":8, "Ainhoa":7, "Maite":5}
for elemento in diccionario:
    print(diccionario[elemento])
print("-------------------")
diccionario.pop("Jon")
for elemento in diccionario:
    print(diccionario[elemento])