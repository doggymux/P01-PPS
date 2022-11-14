#Ejercicio 2.17
#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
#tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

palabra = input("inserte palabra para contar vocales: ")

def contar_vocales(palabra):
    conteo = 0
    numero = 0
    for character in palabra:
        if character in ["a", "e", "i", "o", "u"]:
            numero+=1
            conteo=+numero

    print(conteo)

contar_vocales(palabra)

