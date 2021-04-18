from random import random, choice
Poblacion=[]
TAMGEN=20
TAMPOBLACION=100

pc=0.7 #probabilidad de cruce
pm=0.001 #probabilidad de mutación

##-------------------FUNCIONES-------------------##

def insertarGen(tamgen):
    cromosoma=[]
    for i in range(0, tamgen):
        cromosoma.append(choice([0,1]))
    return cromosoma

def insertarPoblacion(cromosoma):
    Poblacion.append(cromosoma)

def insertarCromosomaAPoblacion(TAMGEN):
    cromosoma=insertarGen(TAMGEN)
    insertarPoblacion(cromosoma)

def contarCant1EnGen(gen):
    cont=0
    for i in range(0, TAMGEN):
        if (gen[i]==1):
            cont=cont+1
    return cont

def cantidadDe1EnCromosoma(poblacion):
    fitnessDeCadaCromosoma=[]
    cont=0
    for i in range(0, len(poblacion)):
        cantidad1=contarCant1EnGen(poblacion[i])
        fitnessDeCadaCromosoma.append(cantidad1)
    return fitnessDeCadaCromosoma

##-----------------------------------------------##

#crear poblacion
for i in range(0,TAMPOBLACION):
        insertarCromosomaAPoblacion(TAMGEN)
print(Poblacion)
print(len(Poblacion))

print ("\n")
fitnessXCrosomosa=cantidadDe1EnCromosoma(Poblacion)
print(fitnessXCrosomosa)