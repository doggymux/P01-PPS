lista1=[10, 12, 80, 90]
lista2=[1, 2, 80, 0]

resultadosiguales = []

def superposicion(resultadosiguales):
    for item in lista1:
      if item in lista2:
        resultadosiguales.append(item)


superposicion(resultadosiguales)

if resultadosiguales == []:
    print("true")
print(resultadosiguales)

