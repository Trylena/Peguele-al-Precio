from principal import *
from configuracion import *
import random
import math
from extras import *
import os

# lee el archivo y carga en la lista lista_producto todas las palabras

def separarConComas(linea):                         #toma una linea y separa con una "," para determinar cada posicion de la lista
    partes=linea.strip().split(',')                 #Funcion Auxiliar
    precios=[int(partes[1]), int(partes[2])]
    return [partes[0]]+precios

def lectura():                                      #lee el txt y ordena los productos por listas, en una lista
    listaDeProductos=[]
    with open("productos.txt", "r") as f:
        lineas=f.readlines()
    for linea in lineas:
        producto= separarConComas(linea)
        listaDeProductos.append(producto)
    return listaDeProductos

lista_productos = lectura()

def buscar_producto(lista_productos):                                               #Le asigna una categoria de producto al azar
    nuevaLista = []
    productoElegido = random.choice(lista_productos)
    tipoProducto=random.randint(1,2)
    if tipoProducto == 1:
        nuevaLista = [productoElegido[0], "(Economico)", productoElegido[1]]
    elif tipoProducto == 2:
        nuevaLista = [productoElegido[0], "(Premium)", productoElegido[2]]
    return nuevaLista

margen=50

def dameProducto(lista_productos, margen):
    producto=buscar_producto(lista_productos)
    cont=0
    for i in lista_productos:
        if producto[2] >= (i[2]-margen) and producto[2]<=(i[2] + margen) or producto[2] >= (i[1]-margen) and producto[2]<=(i[1] + margen) and producto[0]!=i[0]: ##podemos agregar un marge o contamos con uno?...
#cheqeando que el precio del producto que estoy mirando este dentro del margen tanto en la condicion premium como en la economica y a la vez me estoy fijando que no sea el mismo elemento
            cont=cont+1
            print(i)
            if cont>=2:
                return producto

##    producto = ["Silla de oficina", "(premium)", 4391]

#print(dameProducto(lista_productos, 100))


#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    cont = 0
    for producto in lista_productos:
        if (producto[1] - margen) <= precio <= (producto[1] + margen) or (producto[2] - margen) <= precio <= (producto[2] + margen):
            cont =cont + 1
            if cont >= 3:
                return True
    return False

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def procesar(producto_principal, producto_candidato, margen):

    precio_principal = producto_principal[2]  # Precio del producto principal
    precio_candidato = producto_candidato[2]  # Precio del producto candidato

    # Verificar si el producto candidato es diferente al producto principal
    if producto_principal[0] != producto_candidato[0]:
        # Verificar si los precios son iguales o si el precio del candidato está dentro del margen del precio principal
        if precio_principal == precio_candidato or (precio_candidato >= precio_principal - margen and precio_candidato <= precio_principal + margen):
            return producto_candidato[2]  # Sumar el precio del producto candidato a la canasta
    return 0  # Si no es válido, no suma a la canasta


###Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
###De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
###para que sea mostrado en pantalla.
##def dameProductosAleatorios(producto, lista_productos, margen):
##    return productos_seleccionados

def dameProductosAleatorios(producto, lista_productos, margen):
    productos_seleccionados = []

    while len(productos_seleccionados) < 6:
        producto_elegido = random.choice(lista_productos)
        productos_similares = [p for p in lista_productos if
                               (p[1] - margen <= producto_elegido[1] <= p[1] + margen) or
                               (p[2] - margen <= producto_elegido[2] <= p[2] + margen)]

        if len(productos_similares) >= 2:
            categoria = "(Economico)" if producto_elegido[1] < producto_elegido[2] else "(Premium)"
            otra_categoria = "(Premium)" if categoria == "(Economico)" else "(Economico)"

            if len(productos_seleccionados) % 2 == 0:
                categoria_seleccionada = categoria
            else:
                categoria_seleccionada = otra_categoria

            precio_seleccionado = producto_elegido[1] if categoria_seleccionada == "(Economico)" else producto_elegido[2]
            productos_seleccionados.append([producto_elegido[0], categoria_seleccionada, precio_seleccionado])

    return productos_seleccionados




