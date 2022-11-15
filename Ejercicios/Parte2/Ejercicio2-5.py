#Escribir una función sum() y una función multip() que sumen y multipliquen
#respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
#devolver 10 y multip([1,2,3,4]) debería devolver 24.


n = int(input("Cuantos numeros quieres multipiclicar mi rey: "))

suma = 0
multi = 1

# bucleciño

for i in range(0, n):
    numerico = int(input())
    suma += numerico
    multi *= numerico
    
print(suma)
print(multi)
