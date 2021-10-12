import requests
import cv2
import urllib.request
import os

# EL PASO DE LAS FOTOS LO HACEMOS EN .JPG ¡POR EL MOMENTO!, LUEGO IMPLEMENTAREMOS CON .CSV
# TAMBIEN, LAS FOTOS LAS TENEMOS ALMACENADAS DE MANERA LOCAL, PUES DE MANERA VIRTUAL VISUAL NO NOS DEJA ABRIRLAS

def compresion(fotos):
    linkfoto = "https://github.com/mauriciotoro/ST0245-Eafit/blob/master/proyecto/datasets/imagenes/color/enfermo/0.jpg"
    foto = urllib.request.urlopen(linkfoto)
    #imagen = cv2.imread(foto)
    imagen = cv2.imread(r'C:\Users\esove\Desktop\vaca.jpg')

    tamaño = 0.750
    alto = int (imagen.shape[0]*tamaño)
    ancho = int (imagen.shape[1]*tamaño)
    dimension = (ancho,alto)

    imagenRedimesionada = cv2.resize(imagen , dimension, interpolation=cv2.INTER_AREA)

    print(imagenRedimesionada.shape)
    cv2.imshow('output', imagenRedimesionada)
    cv2.imwrite(r'C:\Users\esove\Desktop\vaca_redimensionada.jpg', imagenRedimesionada)

    cv2.waitKey(0)
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

def __main__():
    compresion(fotos)

__main__()