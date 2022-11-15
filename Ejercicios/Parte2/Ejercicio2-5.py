#Escribir una función sum() y una función multip() que sumen y multipliquen
#respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
#devolver 10 y multip([1,2,3,4]) debería devolver 24.
import numpy 

lista = []
n = int(input("Cuantos numeros quieres multipiclicar mi rey: "))
  
# bucleciño
for i in range(0, n):
    numerico = int(input())
    suma =+ numerico
    multi =* numerico
    
    lista.append(numerico)
      
print(numpy.prod(lista))
print(sum(lista))

print(suma)
print(multi)
