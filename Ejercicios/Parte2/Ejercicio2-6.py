#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
#cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
cadena=input()

def inversa(cadena):
    cadenaInvertida = cadena[::-1]
    print(cadenaInvertida)

inversa(cadena)
