#Ejercicio 2.15
#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

lista = []
n = 10

def losviejos(n):

    losviejoslist = []

    for i in range(0, n):
        cadena = int(input("inserta la edad: "))
        lista.append(cadena)

    for e in lista:
        if e > 20:
            losviejoslist.append(e)
    print("El numero total de personas con mas de 20 años es: ", len(losviejoslist))


losviejos(n)