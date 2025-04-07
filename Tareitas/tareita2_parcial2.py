"""calcularemos la distancia entre todos los pares de puntos y determminaremos cuales estan mas cercanos Un a los otros utilizando las distancias f
euclidianas, manhattan y chebyshev
"""
import numpy as np
import pandas as pd
from scipy.spatial import distance

puntoS = {
    'punto1': (2, 3),
    'punto2': (5, 4),
    'punto3': (1, 1),
    'punto4': (6, 7),
    'punto5': (3, 5),
    'punto6': (8, 2),
    'punto7': (4, 6),
    'punto8': (2, 1),
}

df_puntoS= pd.DataFrame.from_dict(puntoS).T
df_puntoS.columns = ['x', 'y']
print('\nCordenadas de los puntos')
print(df_puntoS)

def calcular_distancias(df_puntoS):
    distancia = pd.DataFrame(index=df_puntoS.index, columns=df_puntoS.index)
    #Calcula las distancias
    for i in df_puntoS.index:
        for k in df_puntoS.index:
            if i!=k:
                distancia.loc[i,k] = distance.euclidean(df_puntoS.loc[i],df_puntoS.loc[k])
            else:
                distancia.loc[i,k] = 0
    return distancia


distancias = calcular_distancias(df_puntoS)

valor_maximo = distancias.values.max()
(punto1, punto2) = distancias.stack().idxmax()
print('\n\nTabla de distancias')
print(distancias)         

print('\nDistancia maxima',valor_maximo)  # Distancia Euclidiana
print('Entre el punto', punto1,'y el punto', punto2) # Distancia Euclidiana

#Otra manera
max_value = distancias.max().max()
col_max=distancias.max().idxmax()
id_max=distancias[col_max].idxmax()

print(f'valor maximo {max_value}')
print(f'columna {col_max}')
print(f'indice {id_max}')  # Distancia Euclidiana


#Distancia Manhattan
def calcular_manhattan(df_puntoS):
    distancia = pd.DataFrame(index=df_puntoS.index, columns=df_puntoS.index)
    for i in df_puntoS.index:
        for k in df_puntoS.index:
            if i!=k:
                distancia.loc[i,k] = distance.cityblock(df_puntoS.loc[i],df_puntoS.loc[k])
            else:
                distancia.loc[i,k] = 0
    return distancia

dist_manhattan = calcular_manhattan(df_puntoS)

valor_maximo_manhattan = dist_manhattan.values.max()
(punto1_m, punto2_m) = dist_manhattan.stack().idxmax()
print('\n\nTabla de distancias Manhattan')
print(dist_manhattan)         
print('\nDistancia maxima',valor_maximo_manhattan)
print('Entre el punto', punto1_m,'y el punto', punto2_m)

max_value_manhattan = dist_manhattan.max().max()
col_max_manhattan = dist_manhattan.max().idxmax()

id_max_manhattan = dist_manhattan[col_max_manhattan].idxmax()
print(f'valor maximo {max_value_manhattan}')
print(f'columna {col_max_manhattan}')
print(f'indice {id_max_manhattan}')

#Distancia Chebyshev
def calcular_chebyshev(df_puntoS):
    distancia = pd.DataFrame(index=df_puntoS.index, columns=df_puntoS.index)
    for i in df_puntoS.index:
        for k in df_puntoS.index:
            if i!=k:
                distancia.loc[i,k] = distance.chebyshev(df_puntoS.loc[i],df_puntoS.loc[k])
            else:
                distancia.loc[i,k] = 0
    return distancia

dist_chebyshev = calcular_chebyshev(df_puntoS)

valor_maximo_chebyshev = dist_chebyshev.values.max()
(punto1_c, punto2_c) = dist_chebyshev.stack().idxmax()
print('\n\nTabla de distancias Chebyshev')
print(dist_chebyshev)         
print('\nDistancia maxima',valor_maximo_chebyshev)
print('Entre el punto', punto1_c,'y el punto', punto2_c)

max_value_chebyshev = dist_chebyshev.max().max()
col_max_chebyshev = dist_chebyshev.max().idxmax()
id_max_chebyshev = dist_chebyshev[col_max_chebyshev].idxmax()
print(f'\nValor maximo {max_value_chebyshev}')
print(f'Columna {col_max_chebyshev}')
print(f'indice {id_max_chebyshev}')
