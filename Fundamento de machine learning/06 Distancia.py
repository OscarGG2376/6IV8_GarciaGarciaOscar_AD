import numpy as np
import pandas as pd
from scipy.spatial import distance 

tiendas = {

    'tienda1' : (1,1),
    'tienda2' : (1,5),
    'tienda3' : (7,1),
    'tienda4' : (3,3),
    'tienda5' : (4,8),
    }

df_tienda = pd.DataFrame.from_dict(tiendas).T
df_tienda.columns = ['x', 'y']
print('cordenadas de las tiendas')
print(df_tienda)


distancia_eu = pd.DataFrame(index=df_tienda.index, columns=df_tienda.index)
distancia_mh = pd.DataFrame(index=df_tienda.index, columns=df_tienda.index)
distancia_ch = pd.DataFrame(index=df_tienda.index, columns=df_tienda.index)

for i in df_tienda.index:
    for j in df_tienda.index:
        # Distancia Manhattan
        distancia_eu.loc[i,j] = distance.euclidean(df_tienda.loc[i], df_tienda.loc[j])
        # Distancia Euclidiana
        distancia_mh.loc[i,j] = distance.cityblock(df_tienda.loc[i], df_tienda.loc[j])
        # Distancia Chebyshev
        distancia_ch.loc[i,j] = distance.chebyshev(df_tienda.loc[i], df_tienda.loc[j])

#mostrar las distancias
print('distancia euclidiana')
print(distancia_eu)
print('distancia manhattan')
print(distancia_mh)
print('distancia chebyshev')
print(distancia_ch)
