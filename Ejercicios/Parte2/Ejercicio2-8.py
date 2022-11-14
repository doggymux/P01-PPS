"""Ejercicio 2.8
Definir una función generar_n_caracteres() que tome un entero n y devuelva el
caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver
"xxxxx"""

cantidad=int(input())
def generar_n_caracteres(num,letra):
    nume=0
    nletras=""
    while nume<num:

       nletras+=letra
       nume+=1
    if nume==num:

        return nletras


print("La cadena es:", generar_n_caracteres(cantidad,"a"))