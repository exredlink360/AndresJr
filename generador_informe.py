#sacar hipervinculo 
#reemplazar los saltos de lineas alt 010
#exportarlo csv limitados por ;

nombre_archivo = "C:/Users/02015/Desktop/Tools/enero.csv"
with open(nombre_archivo, "r") as archivo:
    # Omitir el encabezado
    #next(archivo, None)
    for linea in archivo:
        # Remover salto de línea
        linea = linea.rstrip()
        # Ahora convertimos la línea a arreglo con split
        separador = ";"
        lista = linea.split(";")
        # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
        ticket = lista[0]
        motivo = lista[1]
        tipo = lista[5]
        descripcion= lista[6]
        solucion = lista[7]
        if(tipo == "VMware vSphere"):        
            print(ticket + ": " + motivo)
            #print("https://wetcom.atlassian.net/servicedesk/customer/portal/58/"+ticket)
            #print("Descripción: "+descripcion)
            #print("Solución: "+solucion)           
       