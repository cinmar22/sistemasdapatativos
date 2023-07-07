from random import randint
import math
import random

############################################### GENERACION DE POBLACION ###############################################
iteraciones = int( input("Por favor ingresa el numero de iteraciones ") )

aptitudTotal = 0
mejorAptitud = 0
mejorIndividuo = ""

diccAptitudes = {}
listaAptitudes = []
objetosInput = 10 
objetos = pow(objetosInput, 2) - 1
poblacion = [303, 1003, 588, 39, 729, 750]

print("\n")
print("*************************************************")
print(f"*\tGeneracion de la poblacion inicial\t*")
print("*************************************************")
print(f"Poblacion")
print(f"{poblacion}")


numerosBinarios = []
for i in poblacion:
  binario = bin(i)[2:] 
  binario = binario.zfill(objetosInput) 
  numerosBinarios.append(binario)
 
print("\n")
print(f"Lista de cromosomas con su numero decimal")
for i in range(len(numerosBinarios)):
    print( f"[{poblacion[i]}] \t {numerosBinarios[i]}" )


capacidadMochila = 220
pesoObjetos= [47, 43, 44, 35, 33, 36, 24, 49, 41, 29]
gananciaObjetos = [67, 15, 33, 75, 81, 44, 17, 72, 91, 16]  


print("*********************************************************")
print(f"*\tFin de generacion de la poblacion inicial\t*")
print("*********************************************************")
############################################# FIN GENERACION DE POBLACION ###############################################



####################################################### EVALUACION #####################################################
for i in range(iteraciones):
  aptitudTotal=0
  for cromosoma in numerosBinarios:
      aptitud = 0.0
      peso = 0.0
      for i in range(0, objetosInput):
          aptitud += int(cromosoma[i]) * gananciaObjetos[i]
          peso += int(cromosoma[i]) * pesoObjetos[i]
      if peso > capacidadMochila:
          aptitud = 0.0
      if aptitud > mejorAptitud:
        mejorAptitud = aptitud
        mejorIndividuo = cromosoma
      listaAptitudes.append(aptitud)
      diccAptitudes[cromosoma] = aptitud
      aptitudTotal += aptitud

  print("\n")
  print("*************************************************")
  print(f"*\t\t   Evaluacion   \t\t*")
  print("*************************************************")
  print(f"Lista de cromosomas con su aptitud")
  for i in range(len(listaAptitudes)):
    print(f"[{listaAptitudes[i]}]   \t {numerosBinarios[i]}")
  print(f"\nAptitud Total === {aptitudTotal}")
  print("*************************************************")
  print(f"*\t\tFin de evaluacion\t\t*")
  print("*************************************************")
#################################################### FIN EVALUACION #####################################################


####################################################### SELECCION #####################################################
  lista_ruleta = []
  lista_ruleta2= []
  for i in listaAptitudes:
    lista_ruleta.append( round( (i / aptitudTotal) * 100 ) )
  ruleta_unit=0
  for cromosoma in diccAptitudes:
    ruleta_unit = int( round( (diccAptitudes[cromosoma] / aptitudTotal) * 100) )
    for i in range(0,ruleta_unit):
      lista_ruleta2.append(cromosoma)
  random.shuffle(lista_ruleta2)

  print("\n")
  print("*************************************************")
  print(f"*\t\t     Seleccion     \t\t*")
  print("*************************************************")
  print(f"Ruleta")
  for i in range(len(numerosBinarios)):
    print(f"{numerosBinarios[i]} tiene {lista_ruleta[i]} boletos")
  papas = []
  mamas = []
  parejas = 3
  for  i in range(parejas):
    madre = random.choice(lista_ruleta2)
    while True:
      padre = random.choice(lista_ruleta2)
      if(padre != madre):
        break
    papas.append(padre)
    mamas.append(madre)
  print("\n")
  print(f"Parejas")
  for i in range(parejas):
    print(f"{papas[i]}   \t {mamas[i]}")
  print("*************************************************")
  print(f"*\t\tFin de seleccion\t\t*")
  print("*************************************************")
####################################################### FIN SELECCION #####################################################



####################################################### CRUZA #####################################################
  punto_cruce = 3
  hijos=[]
  print("\n")
  print("*********************************************************")
  print(f"*\t\t\t     Cruza     \t\t\t*")
  print("*********************************************************")
  print(f"Punto cruce === 3")
  for  i in range(parejas):
    primerHijo = mamas[i][:punto_cruce] + papas[i][punto_cruce:]
    segundoHijo = papas[i][:punto_cruce] + mamas[i][punto_cruce:]
    hijos.append(primerHijo)
    hijos.append(segundoHijo)
    print(f"Padre: {papas[i]} Madre: {mamas[i]} \t Hijo 1: {segundoHijo} Hijo 2:{primerHijo}")
  lista_ruleta.clear()
  lista_ruleta2.clear()
  print("*********************************************************")
  print(f"*\t\t\tFin de cruza\t\t\t*")
  print("*********************************************************")
####################################################### FIN CRUZA #####################################################


####################################################### MUTACION #####################################################
  pobabilidadMutacion = 0.1
  print(f"Punto cruce === 0.1")
  numerosBinarios.clear()
  for cromosoma in hijos:
    cromosomaMutado=''
    for gen in cromosoma:
      resultado = random.randint(1,10) / 10.0
      if(resultado <= pobabilidadMutacion):
        cromosomaMutado += str( abs( int(gen)-1 ) )
      else:
        cromosomaMutado += gen
    numerosBinarios.append(cromosomaMutado)
  print("\n")
  print("*************************************************")
  print(f"*\t\t     Mutacion     \t\t*")
  print("*************************************************")
  for i in range( len(numerosBinarios) ):
    print(f"Hijo mutado \t {numerosBinarios[i]}")
  print("*************************************************")
  print(f"*\t\t  Fin de mutacion  \t\t*")
  print("*************************************************")
  hijos.clear()
  listaAptitudes.clear()
####################################################### FIN MUTACION #####################################################



####################################################### RESULTADOS #####################################################

aptitudTotal = 0
for cromosoma in numerosBinarios:
  aptitud = 0.0
  peso = 0.0
  for i in range(0, objetosInput):
    aptitud += int(cromosoma[i]) * gananciaObjetos[i]
    peso += int(cromosoma[i]) * pesoObjetos[i]
  if peso > capacidadMochila:
    aptitud = 0.0
  if aptitud > mejorAptitud:
    mejorAptitud = aptitud
    mejorIndividuo = cromosoma
  listaAptitudes.append(aptitud)
  diccAptitudes[cromosoma] = aptitud
  aptitudTotal += aptitud
print("\n")
print("*************************************************")
print(f"*\t\t     Resultados     \t\t*")
print("*************************************************") 
print(f"Mejor individuo: {mejorIndividuo}")
print(f"Mejor aptitud: {mejorAptitud}")
print(f"*************************************************")
print(f"*\t\tFin de resultados\t\t*")
print("*************************************************") 
####################################################### FIN RESULTADOS #####################################################
