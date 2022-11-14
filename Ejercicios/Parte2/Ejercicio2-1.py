print("prueba de insert")
num1=int(input())
num2=int(input())


def fun(num1,num2):
    if num1 > num2:
       print(f'el numero {num1} es mayor que {num2}' )
    elif(num2==num1):
        print(f'Los numeros son iguales')
    else:
        print(f'El numero {num2} es mayor que el {num1}')
fun(num1,num2)