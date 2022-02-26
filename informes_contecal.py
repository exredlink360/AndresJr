#exportarlo csv limitados por ;
from pickle import NONE


cantidad = 0
nombre_archivo = "C:/Users/Plantel01/Documents/GitHub/AndresJr/sFiltro22.csv"
with open(nombre_archivo, "r") as archivo:
    # Omitir el encabezado
    next(archivo, None)
    next(archivo, None)
    next(archivo, None)
    next(archivo, None)
    for linea in archivo:
        # Remover salto de línea
        linea = linea.rstrip()
        # Ahora convertimos la línea a arreglo con split
        separador = ";"
        lista = linea.split(";")
        # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
        numero_tramite = lista[1] 
       # tipo = lista[2] 
        #fecha_creado= lista[4]
        #numero_legajo=lista[6]
        
        
        #if(numero_legajo != "305"):        
        #print(numero_tramite + ": " + tipo)
        print(numero_tramite)   