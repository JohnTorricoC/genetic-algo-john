from random import choice
from random import choices
import random as rand
TAMGEN=20
TAMPOBLACION=100

##-------------------FUNCIONES-------------------##

def insertarGen(tamgen):
    cromosoma=[]
    for i in range(0, tamgen):
        cromosoma.append(choice([0,1]))
    return cromosoma

def insertarPoblacion(cromosoma, Poblacion):
    Poblacion.append(cromosoma)

def insertarCromosomaAPoblacion(TAMGEN, Poblacion):
    cromosoma=insertarGen(TAMGEN)
    insertarPoblacion(cromosoma, Poblacion)

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

def Seleccionar2(chromosomes , chromosomes_fitness):
    
    return choices(population=chromosomes, weights=chromosomes_fitness, k=2)

def Seleccionar(Poblacion):
    Individuos=[]
    num=rand.randrange(0,len(Poblacion))
    primerCromosona=Poblacion[num]
    Individuos.append(primerCromosona)

    num2=rand.randrange(0,len(Poblacion))
    segundoCromosoma=Poblacion[num2]
    Individuos.append(segundoCromosoma)
    return Individuos

def Cruzar(ParDeIndividuos):
    probDeCruzarrActual=rand.random()

    if(probDeCruzarrActual<=pc):

        #num=rand.randrange(1, TAMGEN/2) #Tamaño de cromosomas a intercambiar
        #numSegundoFor=num
        #InicioPrimerCorte=rand.randrange(0, TAMGEN/2)
        #InicioSegundoCorte=rand.randrange(TAMGEN/2, TAMGEN-num)
        #listaCromosomasAIntercamibiar=[]
        #listaCromosomasAIntercamibiar2=[]
        #listaAux=[]
        
        #primerCorte=InicioPrimerCorte
        #segundoCorte=InicioSegundoCorte
        #for i in range (0,num):
        #    num1=ParDeIndividuos[0][primerCorte]
        #    
        #    listaCromosomasAIntercamibiar.append(num1)
        #    primerCorte=primerCorte+1
            
        #    num2=ParDeIndividuos[1][segundoCorte]
            
        #    listaCromosomasAIntercamibiar2.append(num2)
        #    segundoCorte=segundoCorte+1

        #listaAux=listaCromosomasAIntercamibiar.copy()
        #listaCromosomasAIntercamibiar=listaCromosomasAIntercamibiar2
        #listaCromosomasAIntercamibiar2=listaAux
        
        #primerCorte2=InicioPrimerCorte
        #segundoCorte2=InicioSegundoCorte

        #for i in range(0,numSegundoFor):
        #   ParDeIndividuos[0][primerCorte2] = listaCromosomasAIntercamibiar[i]
        #  primerCorte2=primerCorte2+1
        #for i in range(0,numSegundoFor):
        #    ParDeIndividuos[1][segundoCorte2]= listaCromosomasAIntercamibiar2[i]
        #    segundoCorte2=segundoCorte2+1

        num=rand.randrange(1, TAMGEN-1)
        cromIntercambiar1=[]
        cromIntercambiar2=[]
        cromIntercambiar1=ParDeIndividuos[0][:num] + ParDeIndividuos[1][num:]
        cromIntercambiar2=ParDeIndividuos[1][:num] + ParDeIndividuos[0][num:]
        ParDeIndividuos[0]=cromIntercambiar1
        ParDeIndividuos[1]=cromIntercambiar2
    return ParDeIndividuos

def Mutar(DosHijos):
    probDeMutarActual=rand.random()
    cromosomaAMutar=rand.randrange(0, TAMGEN)

    if(probDeMutarActual<=pm):
        if(DosHijos[0][cromosomaAMutar]==0) and (DosHijos[1][cromosomaAMutar]==0):
            DosHijos[0][cromosomaAMutar]=1
            DosHijos[1][cromosomaAMutar]=1
        elif(DosHijos[0][cromosomaAMutar]==1) and (DosHijos[1][cromosomaAMutar]==1):
            DosHijos[0][cromosomaAMutar]=0
            DosHijos[1][cromosomaAMutar]=0
        elif(DosHijos[0][cromosomaAMutar]==1) and (DosHijos[1][cromosomaAMutar]==0):
            DosHijos[0][cromosomaAMutar]=0
            DosHijos[1][cromosomaAMutar]=1
        elif(DosHijos[0][cromosomaAMutar]==0) and (DosHijos[1][cromosomaAMutar]==1):
            DosHijos[0][cromosomaAMutar]=1
            DosHijos[1][cromosomaAMutar]=0
    return DosHijos

def Converge(Poblacion):
    fitness = cantidadDe1EnCromosoma(Poblacion)
    resp=False
    limite=len(Poblacion)
    for i in range (0,limite):
        if(fitness[i]==20):
            resp=True
    return resp

def Reducir(Poblacion):        
    fitness = cantidadDe1EnCromosoma(Poblacion)
    posicion=0
    tamlimite=len(Poblacion)
    
    while tamlimite>=100:
        num=rand.randrange(0, tamlimite)
        fitness.pop(num)
        Poblacion.pop(num)    
        tamlimite=tamlimite-1

def AlgoritmoGeneticoSimple(Poblacion):
    cont=0
    for i in range(0,TAMPOBLACION):
        insertarCromosomaAPoblacion(TAMGEN,Poblacion)
    
    while (Converge(Poblacion)==False):
        nueva_Poblacion=[]
        fitness=cantidadDe1EnCromosoma(Poblacion)
        
        for j in range(0,int(TAMPOBLACION/2)):
            DosIndividuos=Seleccionar2(Poblacion,fitness)
            DosHijos=Cruzar(DosIndividuos)
            DosHijos=Mutar(DosHijos)
            nueva_Poblacion.append(DosHijos[0])
            nueva_Poblacion.append(DosHijos[1])
        Poblacion=nueva_Poblacion
        cont=cont+1
    return cont,Poblacion


##-----------------------------------------------##

if __name__ == "__main__" :
    Poblacion=[]
    pc=0.7 #probabilidad de cruce
    pm=0.001 #probabilidad de mutación
    resp,resp2=AlgoritmoGeneticoSimple(Poblacion)
    print("Numero de eneraciones para encontrar el cromosoma mas fuerte: ")
    print(resp)
  

