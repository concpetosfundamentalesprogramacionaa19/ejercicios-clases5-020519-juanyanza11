'''
	file: run2.py
	autor: juanyanza11
'''
from misvariables import *

# Uso de condicional simple

nota = 18
nota2 = 17

nota = input("Ingrese su nota 1: ")
nota2= input("Ingrese su nota 2: ")

# Convertir de String a Int

nota = int(nota)
nota2 = int(nota2)

# Condicional 1
if nota >= 18:
	print("%s, su nota es: %d" % (mensaje, nota))
else:
	print("%s, su nota es: %d" % (mensaje2, nota))

# Condicional 2

if nota2 >= 18:
	print(mensaje)
else:
	print(mensaje2)