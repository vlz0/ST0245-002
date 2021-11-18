import requests
import cv2
import urllib.request
import os

import re
import numpy as np
from PIL import Image

import time
import sys

def compresion(fotos):
    linkfoto = "https://github.com/mauriciotoro/ST0245-Eafit/blob/master/proyecto/datasets/imagenes/color/enfermo/0.jpg"
    fotos = urllib.request.urlopen(linkfoto)
    imagen = cv2.imread(r'') #ESPECIFICAR LA RUTA DE LOS ARCHIVOS ENTRE LAS ''

    tamaño = 0.777
    alto = int (imagen.shape[0]*tamaño)
    ancho = int (imagen.shape[1]*tamaño)
    dimension = (ancho,alto)

    imagenRedimesionada = cv2.resize(imagen , dimension, interpolation=cv2.INTER_AREA)

    print("     Las dimensiones de nuestra nueva foto es: " +  str(imagenRedimesionada.shape))
    cv2.imwrite(r'', imagenRedimesionada) #ESPECIFICAR LA RUTA DE LOS ARCHIVOS ENTRE LAS ''
    cv2.destroyAllWindows()

def ganadoSano():
    enlace = requests.get('https://github.com/mauriciotoro/ST0245-Eafit/tree/master/proyecto/datasets/imagenes/color/sano')
    convertir = enlace.json

    for i in convertir:
        destino = os.ruta.join('./enfermos', i["nombre"])
        urllib.request.urlretrieve(i["download_url"], destino)

def ganadoEnfermo():
    enlace = requests.get('https://github.com/mauriciotoro/ST0245-Eafit/tree/master/proyecto/datasets/imagenes/color/enfermo')
    convertir = enlace.json

    for i in convertir:
        destino = os.ruta.join('./enfermos', i["nombre"])
        urllib.request.urlretrieve(i["download_url"], destino)

ruta = "./"
fotos = os.listdir(ruta)

searchWindowSize = 0
previewWindowSize = 0

def longest_common_substring(s1, s2):
    maxLongest = 0
    offset = 0
    for i in range(0, len(s1)):
        longest = 0
        if ((i == len(s1) - len(s2) - 2)):
            break
        for j in range(0, len(s2)):
            if (i+j < len(s1)):
                if s1[i+j] == s2[j]:
                    longest = longest + 1
                    if (maxLongest < longest):
                        maxLongest = longest
                        offset = i
                else:
                    break
            else:
                break
    return maxLongest, offset

def encode_lz77(text, searchWindowSize, previewWindowSize):
    encodedNumbers = []
    encodedSizes = []
    encodedLetters = []
    i = 0
    while i < len(text):
        if i < previewWindowSize:
            encodedNumbers.append(0)
            encodedSizes.append(0)
            encodedLetters.append(text[i])
            i = i + 1
        else:
            previewString = text[i:i+previewWindowSize]
            searchWindowOffset = 0
            if (i < searchWindowSize):
                searchWindowOffset = i
            else:
                searchWindowOffset = searchWindowSize
            searchString = text[i - searchWindowOffset:i]
            result = longest_common_substring(searchString + previewString, previewString)
            nextLetter = ''
            if (result[0] == len(previewString)):
                if (i + result[0] == len(text)):
                    nextLetter = ''
                else:
                    nextLetter = text[i+previewWindowSize]
            else:
                nextLetter = previewString[result[0]]
            if (result[0] == 0):
                encodedNumbers.append(0)
                encodedSizes.append(0)
                encodedLetters.append(nextLetter)
            else:
                encodedNumbers.append(searchWindowOffset - result[1])
                encodedSizes.append(result[0])
                encodedLetters.append(nextLetter)
            i = i + result[0] + 1
    return encodedNumbers, encodedSizes, encodedLetters

def decode_lz77(encodedNumbers, encodedSizes, encodedLetters):
    i = 0
    decodedString = []
    while i < len(encodedNumbers):
        if (encodedNumbers[i] == 0):
            decodedString.append(encodedLetters[i])
        else:
            currentSize = len(decodedString)
            for j in range(0, encodedSizes[i]):
                decodedString.append(decodedString[currentSize-encodedNumbers[i]+j])
            decodedString.append(encodedLetters[i])
        i = i+1
    return decodedString

file = r'' #ESPECIFICAR LA RUTA DE LOS ARCHIVOS ENTRE LAS ''
my_string = np.asarray(Image.open(file),np.uint8)
sudhi = my_string
shape = my_string.shape
stringToEncode = str(my_string.tolist())

[encodedNumbers, encodedSizes, encodedLetters] = encode_lz77(stringToEncode, searchWindowSize, previewWindowSize)
a =[encodedNumbers, encodedSizes, encodedLetters]
output = open("compressed.txt","w+")
output.write(str(a))

decodedString = decode_lz77(encodedNumbers, encodedSizes, encodedLetters)
uncompressed_string ="".join(decodedString)

temp = re.findall(r'\d+', uncompressed_string)
res = list(map(int, temp))
res = np.array(res)
res = res.astype(np.uint8)
res = np.reshape(res, shape)
data = Image.fromarray(res)
data.save('uncompressed.png')
if sudhi.all() == res.all():
    print("¡ÉXITO!")

def __main__():
    antes = time.time()
    print("EN TOTAL, USANDO AMBAS CODIFICACIONES NOS DA DE RESULTADOS::")
    compresion(fotos)
    despues = time.time()

    tiempoEjecucion = despues-antes
    memoria = sys.getsizeof(tiempoEjecucion)

    print("     " + str(round(tiempoEjecucion, 2)) + " segundos de Ejecución")
    print("     " + str(memoria) + " KB de consumo de memoria")

__main__()