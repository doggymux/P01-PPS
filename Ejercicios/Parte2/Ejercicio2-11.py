#Ejercicio 2.11
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.

lista = []
n = int(input("Cuantos cadenas quieres comparar en longitud: "))

def funcionmas_larga(n):
    for i in range(0, n):
        cadena = input()
        lista.append(cadena)
    conteo = 0
    max = 0
    for c in lista:

        print(c)
        for character in c:
            conteo = conteo + 1
            if max < conteo:
                max = conteo
    print(max)

funcionmas_larga(n)