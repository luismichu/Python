#filtros selectivos
from random import randint

alumnos = ['Ana', 'Luis', 'Pedro', 'Marta', 'Nerea', 'Pablo']

iniciales = [alumno[0] for alumno in alumnos]

chicas = [alumno for alumno in alumnos if alumno.endswith('a')]
chicos = [set(alumnos) - set(chicas)]

notas = dict()
for alumno in alumnos:
    notas.update({alumno : randint(0,10)})
    
aprobados = [alumno for alumno in alumnos if notas.get(alumno) >= 5]