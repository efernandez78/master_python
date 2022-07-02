import csv # Se importa la libreria csv para poder leer el archivo de entrada.
import matplotlib.pyplot as plt # Se importa la libreria para poder dibujar la gráfica.

 
try:
    fichero = open('finanzas2020.csv', 'r') #Se intenta abrir el fichero en la misma carpeta donde se está ejecutando el programa.
except:
    print("No se ha podido acceder al fichero. Se detiene la ejecución.") # Si no se encuentra o no se puede acceder a él se muestra el mensaje de error correspondiente.
    exit() #Salimos del programa en caso de error de acceso al archivo.

finanzas = csv.reader(fichero, delimiter='\t') #Creamos el objeto de tipo csv con tabulador como delimitador a partir del fichero abierto.
for j in finanzas: #Bucle para acceder a la primera fila del objeto y ver cuantas columnas tiene.
    if len(j)!=12: # Si no tiene 12 columnas el formato del archivo no será correcto.
        print("El número de columnas del archivo de entrada es distinto a 12 (meses del año).\nSe detiene la ejecución.") # Mensaje de error en el caso de no tener 12 columnas.
        fichero.close() # Cerramos el archivo antes de salir del programa al no tener el formato correcto.
        exit() #Salimos del programa
    else:
        print("Se ha comprobado que el archivo tiene 12 columnas (meses del año). Se prosigue la ejecución.\n")
        break #Interrumpimos el bucle de lectura del archivo para no entrar en la zona de datos (ingresos/gastos)

ingresos= [0,0,0,0,0,0,0,0,0,0,0,0] #Definimos la lista donde guardaremos los ingresos de cada mes.
gastos= [0,0,0,0,0,0,0,0,0,0,0,0] #Definimos la lista donde guardaremos los gastos de cada mes.
ahorro=[0,0,0,0,0,0,0,0,0,0,0,0] #Definimos la lista donde guardaremos los ahorros de cada mes.
totalgasto=0 # Variable para guardar el total del gasto de los 12 meses.
totalingreso=0 # Variable para guardar el total del ingreso de los 12 meses.
mediagasto=0 # Variable para el cálculo de la media de los gastos.
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'] # Lista con los meses del año.



for j in finanzas: #Bucle que recorrera las 100 filas donde se encuentra la información de los ingresos/gastos de cada mes.
    for i in range(12): # Bucle que recorre las 12 columnas de cada fila correspondiente a los 12 meses del año.
        try:
            dato=int(j[i]) # Se intenta capturar el dato correspondiente a la fila/columna que toca.
        except:
            print(f"No se ha podido leer el dato {j[i]} del mes de {meses[i]}.\nCompruebe su validez.\nSe prosigue con la ejecución por el siguiente dato.\n") # Si hay error al leerlo, se avisa y se prosigue.
            continue #Se finaliza la iteración actual del bucle de lectura de la fila, tomando el siguiente dato de la misma.
        if dato>0: # Si el dato es mayor que cero será un ingreso.
            ingresos[i]+=dato # Se incrementa el valor del ingreso del mes correspondiente con el valor del dato leido del archivo.
        else: # En caso contrario será un gasto (en caso que sea cero es irrelevante considerarlo gasto o ingreso.)
            gastos[i]+=-dato # Se incrementa el valor del gasto del mes correspondiente con el valor del dato leido del archivo, cambiándole el signo.
for i in range(12): # Bucle para calcular el ahorro de cada mes.
    ahorro[i]+=ingresos[i]-gastos[i] # Una vez calculdo el ingreso y el gasto de cada mes, su ahorro será la diferencia de ambos.
               

gastomax=max(gastos) #Se obtiene cual es el gasto máximo entre todos los meses.
ahorromax=max(ahorro) #Se obtiene cual es el ahorro máximo entre todos los meses.
for i in range(12): #Se recorren los 12 meses buscando cual es el de gasto y ahorro máximo, así como para calcular el total de gastos e ingresos.
    if gastos[i]==gastomax: #Comparamos el gasto de cada mes con el máximo.
        print(f"El mes con más gasto ha sido {meses[i]}.") #Cuando coincida tendremos el mes de mayor gasto.
    if ahorro[i]==ahorromax: #Comparamos el ahorro de cada mes con el máximo.
        print(f"El mes con más ahorro ha sido: {meses[i]}.") #Cuando coincida tendremos el mes de mayor ahorro.
    totalgasto+=gastos[i] #Vamos calculando el total del gasto sumando el realizado en todos los meses.
    totalingreso+=ingresos[i] #Vamos calculando el total de ingresos sumando el realizado en todos los meses.
mediagasto=(totalgasto/12) #La media del gasto será el total dividido por los 12 meses del año.
print("La media de los gastos ha sido: {:.2f}".format(mediagasto)) #Se muestra por pantalla la media del gasto con dos decimales.
print(f"El gasto total ha sido: {totalgasto}.") # Se muestra por pantalla el gasto total.
print(f"El ingreso total ha sido: {totalingreso}.") # Se muestra por pantalla el ingreso total.


plt.plot(meses,ingresos) #Se crrea le gráfico de los ingresos de cada mes frente al mes en el que se obtuvo.
plt.show() # Se muestra por pantalla el gráfico.


fichero.close() #se cierra el archivo antes de acabar la ejecución del programa.
