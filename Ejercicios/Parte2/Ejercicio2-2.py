print("Escriba 3 numeros")
num1=int(input())
num2=int(input())
num3=int(input())
def mayor_3(num1,num2,num3):
    if num1 > num2:

       var=num1
    elif(num2>num1):

        var=num2
    else:
        var=num1
    if (var > num3):
      print(f'el numero {var} es mayor de los tres')
    else:
      print(f'el numero {num3} es mayor de los tres')
mayor_3(num1,num2,num3)