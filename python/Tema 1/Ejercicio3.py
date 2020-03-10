palabrauno=input("Escriba una palabra cualquiera: ")
palabrados=input("Escriba otra palabra cualquiera: ")
resultadouno=palabrauno[:3] + palabrauno[len(palabrauno) -3 : len(palabrauno)]
resultadotres=palabrados[:3] + palabrados[len(palabrados) -3 : len(palabrados)]
print(f"El resultado de la primera palabra es {resultadouno}   y el resultado de la segunda palabra es {resultadotres} ")