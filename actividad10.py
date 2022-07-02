import tkinter as tk
import pandas as pd
import json
import csv
import os
import numpy as np
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

"""
Esta aplicación se encarga de la gestión (añadir, modificar, mostrar, eliminar información) de la base de datos en
formato .csv 'iris.csv', donde se guarda la información dimensional del sépalo y del pétalo y su correspondencia
con la especie de iris (setosa, versicolor, virginica), así como de usar un algoritmo de 'machine learning' 
para predecir la especie que le corresponde a las dimensiones introducidas de sépalo y pétalo medidas para
una flor que no se encuentren en esta base de datos.

La aplicación funciona en modo ventana (GUI) y muestra en cuatro columnas sus cinco funcionalidades.

En la primera columna (empezando por la izquierda) se nos permite introducir un nuevo dato en la BBDD. Para ello
debemos introducir la longitud y ancho del pétalo y el sépalo qu ehayamos medido y la especie a la que pertenece
en cada una de las casillas correspondientes y pulsar en el botón 'Entrar'.

En la siguiente columna se nos da la opción de modificar un dato en la BBDD, proporcionando además de la información
anterior el número de linea en el que se encuentra dentro de la BBDD.

Una columna más a la derecha se encuentran las opciones de eliminar un dato o de mostrarlo introduciendo el
número de linea que ocupa en la BBDD.

Por último, en la columna de más a la derecha, a partir de unos datos de longitud y ancho del pétalo y el sépalo
nos predice a qué especie pertenece utlizando los datos de la BBDD y el algoritmo de 'machine learning' de la
librería sklearn.

El progrmaa ha sido escrito utilizando el framework para aplciacion GUI tkinter.

Cuenta con las siguientes funciones:

nuevo_dato()
modificar_dato()
eliminar_dato()
mostrar_dato()
predecir_especie() 
"""

MEDIA_ROOT = os.path.expanduser("~/Desktop/iris.csv")


ventana= tk.Tk()

def nuevo_dato():
    """ Función que se encarga de introducir un nuevo dato en la BBDD.
    Args: vacios

    Toma los datos de la ventana GUI correspondiente a la columna izquierda y los introduce
    en la BBDD.

    Realiza la comprobación de que la especi introducida es Iris-virginica, Iris-versicolor o 
    Iris-setosa. Si la especie no es ninguna de esas tres no permipip tira seguir adelante y lanzará
    un mensaje de error.
    """

    try:
        e5.configure({"background": "white"})
        e10.configure({"background": "white"})
        e11.configure({"background": "white"})
        e12.configure({"background": "white"})
        e13.configure({"background": "white"})
        tk.Label(ventana, text= "                                                 ", bg="grey" ).grid(row=8, column=0)
        if e5.get()!="Iris-setosa" and e5.get()!="Iris-virginica" and e5.get()!="Iris-versicolor":
            e5.configure({"background": "red"})
            tk.Label(ventana, text= "Especie desconocida", bg="red" ).grid(row=8, column=0)
            return
        e5.configure({"background": "white"})
        with open(MEDIA_ROOT, 'a', newline='') as csvfile:
            fieldnames = ["sepal_length", "sepal_width","petal_length",
            "petal_width", "species"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"sepal_length": e3.get(),
            "sepal_width": e4.get(),
            "petal_length": e1.get(),
            "petal_width": e2.get(),
            "species": e5.get()})
            e1.delete(0, tk.END)
            e2.delete(0, tk.END)
            e3.delete(0, tk.END)
            e4.delete(0, tk.END)
            e5.delete(0, tk.END)
        tk.Label(ventana, text= "Dato introducido", bg="green" ).grid(row=8, column=0)

    except:
        tk.Label(ventana, text= "Error al introducir dato.", bg="red" ).grid(row=8, column=0)


def modificar_dato():
    """
    Función nuevo_dato()
    """
    
    e5.configure({"background": "white"})
    e10.configure({"background": "white"})
    e11.configure({"background": "white"})
    e12.configure({"background": "white"})
    e13.configure({"background": "white"})
    tk.Label(ventana, text= "                                                     ", bg="grey" ).grid(row=8, column=0)
    try:
        df = pd.read_csv(MEDIA_ROOT)
        filas=len(df.index)
        if filas<int(e11.get()):
            e11.configure({"background": "red"})
            tk.Label(ventana, text= "Error al modificar dato", bg="red" ).grid(row=8, column=0)
            return
        if e10.get()!="Iris-setosa" and e10.get()!="Iris-virginica" and e10.get()!="Iris-versicolor":
            e10.configure({"background": "red"})
            tk.Label(ventana, text= "Especie desconocida", bg="red" ).grid(row=8, column=0)
            return
        nuevos_valores = [e8.get(), e9.get(), e6.get(), e7.get(), e10.get()]
        df.loc[int(e11.get())] = nuevos_valores
        df.to_csv(MEDIA_ROOT, index=False)
        e6.delete(0, tk.END)
        e7.delete(0, tk.END)
        e8.delete(0, tk.END)
        e9.delete(0, tk.END)
        e10.delete(0, tk.END)
        e11.delete(0, tk.END)
        tk.Label(ventana, text= "Dato modificado", bg="green" ).grid(row=8, column=0)
    except:
        tk.Label(ventana, text= "Error al modificar dato", bg="red" ).grid(row=8, column=0)




def eliminar_dato():

    e5.configure({"background": "white"})
    e10.configure({"background": "white"})
    e11.configure({"background": "white"})
    e12.configure({"background": "white"})
    e13.configure({"background": "white"})
    tk.Label(ventana, text= "                                                     ", bg="grey" ).grid(row=8, column=0)
    try:
        df = pd.read_csv(MEDIA_ROOT)
        filas=len(df.index)
        if filas<int(e12.get()):
            e12.configure({"background": "red"})
            tk.Label(ventana, text= "Error al eliminar dato", bg="red" ).grid(row=8, column=0)
            return
        df.drop(int(e12.get()), inplace=True)
        df.to_csv(MEDIA_ROOT, index=False)
        e12.delete(0, tk.END)
        tk.Label(ventana, text= "Dato eliminado", bg="green" ).grid(row=8, column=0)
    except:
        tk.Label(ventana, text= "Error al eliminar dato", bg="red" ).grid(row=8, column=0)


def mostrar_dato():

    e5.configure({"background": "white"})
    e10.configure({"background": "white"})
    e11.configure({"background": "white"})
    e12.configure({"background": "white"})
    e13.configure({"background": "white"})
    tk.Label(ventana, text= "                                                     ", bg="grey" ).grid(row=8, column=0)
    try:
        df = pd.read_csv(MEDIA_ROOT)
        filas=len(df.index)
        if filas<int(e13.get()):
            e13.configure({"background": "red"})
            tk.Label(ventana, text= "Error al mostrar dato", bg="red" ).grid(row=8, column=0)
            return
        tk.Label(ventana, text= "Dato mostrado", bg="green" ).grid(row=8, column=0)
        messagebox.showinfo(message=f"Petal Length: {df.loc[int(e13.get()),'petal_length']}\
        \nPetal Width: {df.loc[int(e13.get()),'petal_width']}\
        \nSepal length: {df.loc[int(e13.get()),'sepal_length']}\
        \nSepal width: {df.loc[int(e13.get()),'sepal_width']}\
        \nSpecie: {df.loc[int(e13.get()),'species']}.")

        e13.delete(0, tk.END)

    except:
        tk.Label(ventana, text= "Error al mostrar dato", bg="red" ).grid(row=8, column=0)

def predecir_especie():

    e5.configure({"background": "white"})
    e10.configure({"background": "white"})
    e11.configure({"background": "white"})
    e12.configure({"background": "white"})
    e13.configure({"background": "white"})
    tk.Label(ventana, text= "                                                     ", bg="grey" ).grid(row=8, column=0)
    try:
        df = pd.read_csv(MEDIA_ROOT)
        df.species = df.species.map({"Iris-setosa": 0,
                                    "Iris-versicolor": 1,
                                    "Iris-virginica": 2})
        X = df.drop("species",axis=1)
        y = df["species"]
        clf= DecisionTreeClassifier()
        clf.fit(X,y)
        X_pred=pd.DataFrame()
        X_pred['sepal_length'] = None
        X_pred['sepal_width'] = None
        X_pred['petal_length'] = None
        X_pred['petal_width'] = None
        X_pred.loc[1]=[e16.get(),e17.get(),e14.get(),e15.get()]
        y_pred= clf.predict(X_pred)
        if y_pred==[0]:
            tk.Label(ventana, text= "Predicción realizada", bg="green" ).grid(row=8, column=0)
            messagebox.showinfo(message="La especie predecida es Iris-setosa")
        elif y_pred==[1]:
            tk.Label(ventana, text= " Predicción realizada", bg="green" ).grid(row=8, column=0)
            messagebox.showinfo(message="La especie predecida es Iris-versicolor")
        elif y_pred==[2]:
            tk.Label(ventana, text= "Predicción realizada", bg="green" ).grid(row=8, column=0)
            messagebox.showinfo(message="La especie predecida es Iris-virginica")
        else:
            tk.Label(ventana, text= "Error al ejecutar prediccion", bg="red" ).grid(row=8, column=0)
            messagebox.showinfo(message="No se ha podido realizar la prediccion")



        e14.delete(0, tk.END)
        e15.delete(0, tk.END)
        e16.delete(0, tk.END)
        e17.delete(0, tk.END)

    except:
        tk.Label(ventana, text= "Error al ejecutar prediccion", bg="red" ).grid(row=8, column=0)


tk.Label(ventana, text= "                                                     ", bg="grey" ).grid(row=8, column=0)
tk.Label(ventana, text="Introduzca nueva dato.").grid(row=1, column=0)
tk.Label(ventana, text="Petal Length ").grid(row=2, column=0)
tk.Label(ventana, text= "Petal Width " ).grid(row=3, column=0)
tk.Label(ventana, text="Sepal Length ").grid(row=4, column=0)
tk.Label(ventana, text= "Sepal Width " ).grid(row=5, column=0)
tk.Label(ventana, text= "Species " ).grid(row=6, column=0)


e1= tk.Entry(ventana)
e1.insert(0,"")
e1.grid(row=2, column=1)

e2= tk.Entry(ventana)
e2.insert(0,"")
e2.grid(row=3, column =1)

e3= tk.Entry(ventana)
e3.insert(0,"")
e3.grid(row=4, column =1)

e4= tk.Entry(ventana)
e4.insert(0,"")
e4.grid(row=5, column =1)

e5= tk.Entry(ventana)
e5.insert(0,"")
e5.grid(row=6, column =1)




tk.Button(ventana, text="Entrar", fg="white", bg="blue",
        command=nuevo_dato).grid(row=7,column=0)



tk.Label(ventana, text="Modifique un dato.").grid(row=1, column=3)
tk.Label(ventana, text="Petal Length ").grid(row=2, column=3)
tk.Label(ventana, text= "Petal Width " ).grid(row=3, column=3)
tk.Label(ventana, text="Sepal Length ").grid(row=4, column=3)
tk.Label(ventana, text= "Sepal Width " ).grid(row=5, column=3)
tk.Label(ventana, text= "Species " ).grid(row=6, column=3)
tk.Label(ventana, text= "Dato a modificar " ).grid(row=7, column=3)

e6= tk.Entry(ventana)
e6.insert(0,"")
e6.grid(row=2, column=4)

e7= tk.Entry(ventana)
e7.insert(0,"")
e7.grid(row=3, column =4)

e8= tk.Entry(ventana)
e8.insert(0,"")
e8.grid(row=4, column =4)

e9= tk.Entry(ventana)
e9.insert(0,"")
e9.grid(row=5, column =4)

e10= tk.Entry(ventana)
e10.insert(0,"")
e10.grid(row=6, column =4)

e11= tk.Entry(ventana)
e11.insert(0,"")
e11.grid(row=7, column =4)

tk.Button(ventana, text="Modificar", fg="white", bg="blue",
        command=modificar_dato).grid(row=8,column=4)

tk.Label(ventana, text= "Elimine un dato." ).grid(row=1, column=5)
tk.Label(ventana, text= "Dato a eliminar " ).grid(row=2, column=5)
e12= tk.Entry(ventana)
e12.insert(0,"")
e12.grid(row=2, column =6)

tk.Button(ventana, text="Eliminar", fg="white", bg="blue",
        command=eliminar_dato).grid(row=3,column=5)


tk.Label(ventana, text= "Mostrar un dato" ).grid(row=5, column=5)
tk.Label(ventana, text= "Dato a mostrar" ).grid(row=6, column=5)
e13= tk.Entry(ventana)
e13.insert(0,"")
e13.grid(row=6, column =6)
tk.Button(ventana, text="Mostrar", fg="white", bg="blue",
        command=mostrar_dato).grid(row=7,column=5)



tk.Label(ventana, text="Predecir un dato (especie)").grid(row=1, column=7)
tk.Label(ventana, text="Petal Length ").grid(row=2, column=7)
tk.Label(ventana, text= "Petal Width " ).grid(row=3, column=7)
tk.Label(ventana, text="Sepal Length ").grid(row=4, column=7)
tk.Label(ventana, text= "Sepal Width " ).grid(row=5, column=7)



e14= tk.Entry(ventana)
e14.insert(0,"")
e14.grid(row=2, column=8)

e15= tk.Entry(ventana)
e15.insert(0,"")
e15.grid(row=3, column =8)

e16= tk.Entry(ventana)
e16.insert(0,"")
e16.grid(row=4, column =8)

e17= tk.Entry(ventana)
e17.insert(0,"")
e17.grid(row=5, column =8)


tk.Button(ventana, text="Predecir", fg="white", bg="blue",
        command=predecir_especie).grid(row=6,column=7)








ventana.mainloop()
