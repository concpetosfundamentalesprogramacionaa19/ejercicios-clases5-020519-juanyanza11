'''
	file: run4.py
	autor: juanyanza11
'''

'''
	Deseamos obtener el costo de una carrera univesitaria, el valor promedio de cada ciclo es de
	1200 dólares, el valor promedio del seguro educativo es de POR CICLO 100 dólares si la edad del estudiantes
	es menor o igual a 20 caso contrario será de 150 dólares si el estudiante tiene una modalidad a distancia
	el numero de ciclos a seguir es de 10, caso contrario deberá seguir 8 ciclos. 

	OBTENER LA PROYECCION DEL COSTO TOTAL DE LA CARRERA DEL ESTUDIANTE 

'''
from misvariables import *

edad = input("Ingrese su edad\n")
edad = int(edad)
seguro1= 100
seguro2=150
valorc= 1200
modalidad = input("Ingrese su modalidad\n")

if (modalidad == "distancia") and (edad <=20):
	costo = seguro1*10 + valorc*10
	print("El costo de su matricula es: %d" % (costo))
else:
	if (modalidad == "distancia") and (edad >20):
		costo = seguro2*10 + valorc*10
		print("El costo de su matricula es: %d" % (costo))
	else:
		if (modalidad == "presencial") and (edad <=20):
			costo = seguro1*8 + valorc*8
			print("El costo de su matricula es: %d" % (costo))
		else:
			if (modalidad == "presencial") and (edad > 20):
				costo = seguro2*8 +valorc*8
				print("El costo de su matricula es: %d" % (costo))



