import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../housing.csv')

##mostrar las primeras 5 filas
print(df.head())

##mostrar las ultimas 5 filas
print(df.tail())

##mostrar filas especificas
print(df.iloc[7])

##mostrar la columna ocean-proximity
print(df['ocean_proximity'])

media = df['total_rooms'].mean()
print('La media de total room es:', + media)

##mediana

mediana = df['median_house_value'].median()
print("""La mediana de la columna "valor mediano de la casa" """ , + mediana)


##la suma de puopular
salario = df['population'].sum()
print('El salario total es de:', + salario)

##filtrar

filtrito = df[df['ocean_proximity'] == 'ISLAND']
print(filtrito)

#vamos a hacer un grafico de dispersion

plt.scatter(df['ocean_proximity'][:10], df ['median_house_value'][:10])

##nombrado

plt.xlabel('Proximidad')
plt.ylabel('Precio')
plt.title('TABLITA')
plt.show()
