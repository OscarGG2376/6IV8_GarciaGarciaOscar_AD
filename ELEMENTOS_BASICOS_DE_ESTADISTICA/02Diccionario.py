import pandas as pd
##Escribir una funcion que reciba un diccionario con las nptas de los estuudiantes del curso y devuelve un minimo,maximo,media
def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadistica = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()],  index =['Min', 'Max', 'Media','Desviacion'])
    return estadistica

def aprobados(notas):
    notas = pd.Series(notas)
    return notas [notas >= 5].sort

notas = {'Juan': 9, 'Omar': 8, 'Owen': 9, 'Poncho': 3}

print(estadistica_notas(notas))