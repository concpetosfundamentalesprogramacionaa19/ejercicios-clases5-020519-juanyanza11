'''
	file: run3.py
	autor: juanyanza11
'''

'''
	nota mayor o igual a 18: Sobresaliente

	nota mayor igual a 16 y menor a 18: muy bueno

	nota mayor igual a 13 y meor a 16: buena
'''
from misvariables import *

# Uso de condicional simple

nota = input("Ingrese su nota 1: ")


# Convertir de String a Int

nota = int(nota)

# If anidado 

if nota >= 18:
	print("%s- nota: %d " % ("Sobresaliente", nota))
else:
	if (nota >= 16) and (nota < 18):
		print("%s- nota: %d" % ("Muy buena", nota))
	else:
		if (nota >= 13) and (nota < 16):
			print("%s- nota: %d" % ("Buena", nota))
		else:
			print("%s- nota: %d" % ("Insuficiente", nota))
		
