# Ejercicio 2.12
# Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
# devuelva las palabras que tengan más de n caracteres.

lista = []

n = int(input("Cuantas palabras vas a filtrar "))
l = int(input("Cual es la longitud minima de caracteres "))
listafinal = []

def filtrar_palabras(listafinal):
    conteo = 0
    numero = 0
    for i in range(0, n):
        cadena = input()
        lista.append(cadena)
    print(lista)
    for c in lista:
        for character in c:
            conteo = conteo + 1
        if l < conteo:
            listafinal.append(c)

filtrar_palabras(listafinal)
print(listafinal)
