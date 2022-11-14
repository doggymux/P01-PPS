#Ejercicio 2.16
#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la
#letra a.
#También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)

lbus = input("buscar nombres que empiecen por: ")

def busquedanombres(lbus):
    listado = ['anacleto', "Leonardo Dantes", "Messirve", "Sherk", "Ricardo Milos"]
    resultado = []
    for i in listado:
        if i[0:1].lower() == lbus.lower():
            resultado.append(i)

    for r in resultado:
        print(r)
busquedanombres(lbus)