# genetic-algo-john

## Algotirmo Genetico

**¿De que trata el proyecto?**
La premisa de esta practica es hacer correr el algoritmo genetico visto en clases utilizando los metodos: selection, crossover y mutation.  Cada cromosoma x tiene un tamanio de 20 genes y esta formado por 0s y 1s solamente.

Utilizando una probabilidad de crossover pc = 0.7 y una probabilidad de mutation pm = 0.001 para crear nuevas generaciones de cromosomas iniciando con una poblacion inicial de 100 cromosomas generados al azar, hasta que te devuelva la generacion en la cual se encontro el cromosoma mas fuerte.

(Se adjuntaron imagenes para aclarecer mas las dudas)

*Primer Ejemplo*

Ejemplo: NumeroDeGeneraciones.png


## Experimentos

**Primer experimento**
    Ejecutar el algoritmo 20 veces, para cada ejecucion (run) reporta en que generacion se encontro al cromosoma mas fuerte. Reporta la media de este valor.

    Ejemplo: PrimerExperimento.png

**Sefundo experimento**
    Ejecuta el mismo experimento, pero esta vez sin crossover (pc = 0, pm = 0.001).

    Advertencia: Cabe recalcar que la funcion toma mucho tiempo para hacer correr incluso una iteracion, asi que se dejo corriendolo pero sin muestra alguna, ya que la probabilidad de cossover es 0.

    Ejemplo: SegundoExperimento.png

**Tercer experimento**
    Ejecuta el mismo experimento, pero esta vez sin mutation (pc = 0.7, pm = 0).

    Ejemplo: TercerExperimento.png

**Cuarto experimento**
    Ejecuta el mismo experimento, pero esta vez con estos valores:

    * pc = 0.9, pm = 0.001
        Ejemplo: CuartoExperimento-1.png
    * pc = 0.3, pm = 0.001
        Ejemplo: CuartoExperimento-2.png
    * pc = 0.2, pm = 0.001
        Ejemplo: CuartoExperimento-3.png
    * pc = 0.05, pm = 0.001
        Ejemplo: CuartoExperimento-4.png


**Quinto experimento**
    ¿Cual es la mejor opcion de parametros segun los resultados obtenidos anteriormente? ¿Por que?

        Respuesta: La mejor opcion es la primera, que tiene una pc=0.9, porque con una probabilidad de crossove mas cercana a 1 hay mas probabilidades de que podamos encontrar el cromosoma mas fuerte.
    
**Sexto experimento**
    Ejecuta el algoritmo 20 veces, para cada ejecucion (run) reporta en que generacion se encontro al cromosoma mas fuerte. Reporta la media de este valor. Varıa el tamano de la poblacion. Prueba con 50, 100, 500, 1000 cromosomas. ¿Cual es la mejor opcion? ¿Por que?

    pc = 0.7, pm = 0.001

    * Poblacion:50
        Ejemplo: SextoExperimento-1.png
    * Poblacion:100
        Ejemplo: SextoExperimento-2.png
    * Poblacion:500
        Ejemplo: SextoExperimento-3.png
    * Poblacion:1000
        Ejemplo: SextoExperimento-4.png

        Respuesta: La mejor opcion es la cuarta, con una poblacion de 1000; porque con una poblacion mas grande tenemos mas probabilidades de encontrar el cromosoma mas fuerte en menos generaciones, ya que tomamos en cuenta mas gente para el experimento.
    
**Septimo experimento**
    Ejecuta el algoritmo por 100 generaciones y grafica el mejor, el peor y el promedio del fitness function encontrado en cada generacion vs el numero de generacion.


    Ejemplo: SeptimoExperimento.png



## Guia

**Instalaciones**

- [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
- [Visual code](https://code.visualstudio.com/download)

Nota: Visual Code no es completamente necesario, si se quiere se puede utilizar otro editor de codigo que usted elija.

**Pasos para hacer correr el codigo**

Una vez conseguido el codigo hacer lo siguiente:

    *Abrir una terminal con la siguiente ruta como ejemplo: "C:\Users\PC\Desktop\Sistemas Inteligentes\algoritmo_genetico\" (Sin las comillas)
    *En la terminal escribir la siguiente linea: "py main.py" (Sin las comillas)