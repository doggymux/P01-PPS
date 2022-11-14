lista =[]
n = int(input("Cuantos numeros va a comparar: "))

# bucleciño
for i in range(0, n):
    numerico = int(input())
    lista.append(numerico)

print(lista)

def mayor(lista):
    max = lista[0];
    for x in lista:
        if x > max:
            max = x
    return max

print ("El número mayor es ", mayor(lista))