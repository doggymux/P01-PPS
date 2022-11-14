#Solicitar al usuario dos valores:
#● numero1 (int)
#● numero2 (int)
#Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que
#sigue):
#Proporciona el numero1:
#Proporciona el numero2:
#El numero mayor es:<numeroMayor>
#¿Cuál es el código del requerimiento solicitado?

num1 = int(input("Proporciona el numero1: "))

num2 = int(input("Proporciona el numero2: ")) 

def fun(num1,num2):
    if num1 > num2:
        print(f'El numero mayor es:{num1}' )
    elif(num2==num1):
        print(f'Los numeros son iguales')
    else:
        print(f'El numero mayor es:{num2}')

fun(num1,num2)
