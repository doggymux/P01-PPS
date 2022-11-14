#Ejercicio 2.14
#Construir un pequeño programa que convierta números binarios en enteros

numero_binario = '1010111'

def binario_a_decimal(numero_binario):
	numero_decimal = 0

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	print(numero_decimal)

binario_a_decimal(numero_binario)
