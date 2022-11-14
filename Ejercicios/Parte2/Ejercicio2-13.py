#Ejercicio 2.13
#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
#que evaluar la cadena y decir cuantas letras mayúsculas tiene.

cadenaorigen = input("introduce una cadena para contar las mayusculas: ")

def contarmayusculas(cadenaorigen):
    cadena = cadenaorigen.lower()
    contador = 0
    num = len(cadenaorigen)
    for l in range(0, len(cadenaorigen)):
        print(l)
        if cadena[l:l+1] != cadenaorigen[l:l+1]:
            num = contador + 1
            contador = num
    print(contador)
contarmayusculas(cadenaorigen)