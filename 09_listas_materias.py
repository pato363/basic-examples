"""Ejercicio N°1
materias = ['matematicas','Historia','Quimica','Castellano' ]
puntuaciones = []

for materia in materias:
    puntuacion = input ('Escribe la nota que has sacado en la asignatura ' + materia +'=>')
    puntuaciones.append(puntuacion)
for i in range (len(materias)):
    print ('la nota que obtuviste en'+ materias[i] + 'es', puntuaciones[i])
"""
#Ejercicio N°2

materias = ['matematicas','Historia','Quimica','Castellano' ]
reprobada = []

for materia in materias:
    puntuacion = float(input ('Escribe la nota que has sacado en la asignatura ' + materia +'=>'))
    if puntuacion <= 4:
        reprobada.append(puntuacion)

for materia in reprobada: 
    materias.remove(materia)
    print ('las materias que reprobaste fue'+ str(materias))
