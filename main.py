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

def funcionDeAdaptacion(CantidadDe1EnCromosoma, CantidadDe1EnCromosomaOrdenado):
    fitnessDeCadaCromosoma=[]
    for i in range(0,len(CantidadDe1EnCromosoma)):
        fitness=CantidadDe1EnCromosomaOrdenado[-1]-CantidadDe1EnCromosoma[i]
        fitnessDeCadaCromosoma.append(fitness)
    return fitnessDeCadaCromosoma

def cantidadDe1XCromosomaOrdenado():
    CantidadDe1XCromosoma=cantidadDe1EnCromosoma(Poblacion)
    CantidadDe1XCromosomaOrdenado=CantidadDe1XCromosoma.copy()
    CantidadDe1XCromosomaOrdenado.sort()
    return CantidadDe1XCromosomaOrdenado

def Seleccionar(Poblacion):
    CantidadDe1XCromosoma=cantidadDe1EnCromosoma(Poblacion)
    CantidadDe1XCromosomaOrdenado=cantidadDe1XCromosomaOrdenado()
    fitness=funcionDeAdaptacion(CantidadDe1XCromosoma,CantidadDe1XCromosomaOrdenado)

    Individuos=[]
    num=random.randrange(0,len(Poblacion))
    primerCromosona=Poblacion[num]
    Individuos.append(primerCromosona)

    num2=random.randrange(0,len(Poblacion))
    segundoCromosoma=Poblacion[num2]
    Individuos.append(segundoCromosoma)
    

##-----------------------------------------------##

#Crear poblacion
print("Poblacion de cromosomas: ")
for i in range(0,TAMPOBLACION):
        insertarCromosomaAPoblacion(TAMGEN)
print(Poblacion)
print(len(Poblacion))
print("\n")

#Contar unos de las poblacion de cromosomas
print("Numero de unos de la problacion de cromosomas: ")
fitnessXCrosomosa=cantidadDe1EnCromosoma(Poblacion)
print(fitnessXCrosomosa)
print("\n")

#
CantidadDe1XCromosoma=cantidadDe1EnCromosoma(Poblacion)
CantidadDe1XCromosomaOrdenado=cantidadDe1XCromosomaOrdenado()
print(CantidadDe1XCromosomaOrdenado)
print("\n")
fitness=funcionDeAdaptacion(CantidadDe1XCromosoma,CantidadDe1XCromosomaOrdenado)
print(fitness)