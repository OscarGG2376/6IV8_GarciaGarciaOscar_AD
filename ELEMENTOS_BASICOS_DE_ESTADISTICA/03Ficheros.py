import pandas as pd

def resumen_cotizacion(ficheros):
    df = pd.read_csv(ficheros, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean(), df.std()], index= ['Min', 'Max', 'Media','Desviacion'])

print(resumen_cotizacion('../cotizacion.csv'))