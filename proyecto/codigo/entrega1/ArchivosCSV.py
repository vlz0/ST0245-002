import _csv
lista = [] 
nombre_archivo= "Casos_positivos_de_COVID-19_en_Colombia.csv"
with open(nombre_archivo, encoding ="utf8")as archivo: 
    entrada = _csv.reader(archivo, errors='ignore')
    lista = list(entrada) 

for linea in lista: 
    print(linea) 

#en la linea 3 se pone un ejemplo de un archivo csv para su ejecucion#