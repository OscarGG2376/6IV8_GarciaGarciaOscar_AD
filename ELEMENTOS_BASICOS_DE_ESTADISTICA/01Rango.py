import pandas as pd

##vamos a hacer un progrma que pregunte al usuario por las ventas en un año antes y despues

inicio = int(input('introduce el año de ventas inicial: '))
fin = int(input('introduce el año final de ventas: '))

ventas = {}
for i in range(inicio,fin + 1):
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) + ':'))
ventas = pd.Series(ventas)




print('Ventas \n ', ventas)
print('Ventas con descuento\n',ventas*0.9)