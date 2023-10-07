def segundosAMinutos(duracion):
    minutos = 0
    segundos = 0
    
    tiempo = ""
    
    while duracion > 0:
        if duracion >= 60:
            minutos += 1
            duracion -= 60
        else:
            segundos += duracion
            duracion = 0
        
    tiempo = str(minutos) + ":" + str(segundos)
        
    return tiempo


def segundosAHoras(duracion):
    horas = 0
    minutos = 0
    segundos = 0
    
    tiempo = ""
    
    while duracion > 0:
        if duracion >= 3600:
            horas += 1
            duracion -= 3600
        elif duracion >= 60:
            minutos += 1
            duracion -= 60
        else:
            segundos += duracion
            duracion = 0
            
    tiempo = str(horas) + ":" + str(minutos) + ":" + str(segundos)
    
    return tiempo



arch = open("spotify.txt", "r", encoding = "utf-8")
linea = arch.readline().strip()


cantCanciones = 0 #Contador de canciones en el archivo

duracionCancionMasCorta = 10000 #Contador de segundos de la canción menos reproducida
cancionMasCorta = "" #Nombre de la canción menos reproducida
duracionCancionMasLarga = -1 #Contador de segundos de la canción mas reproducida
cancionMasLarga = "" #Nombre de la canción mas reproducida

reproduccionesCancionMasReproducida70s = -1 #Contador de reproducciones de la cancion mas reproducida en los 70's
albumMasReproducido = "" #Nombre del album que tiene la cancion mas reproducida en los 70's




anioMasAntiguo = 10000
fechaCompletaCancionMasAntigua = "" #Fecha de la canción mas antigua
cancionMasAntigua = "" #Nombre de la canción mas antigua
anioMasReciente = -1
fechaCompletaCancionMasReciente = "" #Fecha de la canción mas reciente
cancionMasReciente = "" #Nombre de la canción mas reciente

tiempoTotalReproducido = 0 #Tiempo total que se reprodujieron las canciones



while linea != "":
    partes = linea.split(",")
    nombreCancion = partes[0]
    artista = partes[1]
    album = partes[2]
    lanzamiento = partes[3].split("/")
    lanzamientoo = partes[3]
    dia = int(lanzamiento[0])
    mes = int(lanzamiento[1])
    anio = int(lanzamiento[2])
    duracion = int(partes[4])
    reproducciones = int(partes[5])
    
    
    if linea != "":#El algoritmo para realizar el item 1
        cantCanciones +=1
    
    #El algoritmo para realizar el item 2
    if duracion < duracionCancionMasCorta:
        duracionCancionMasCorta = duracion
        cancionMasCorta = nombreCancion
    elif duracion > duracionCancionMasLarga:
        duracionCancionMasLarga = duracion
        cancionMasLarga = nombreCancion
        
    
    #El algoritmo para realizar el item 3
    if anio >= 1970 and anio <= 1979:
        if reproducciones > reproduccionesCancionMasReproducida70s:
            reproduccionesCancionMasReproducida70s = reproducciones
            albumMasReproducido = album
    
    
    
    #El algoritmo para realizar el item 4
    if anio < anioMasAntiguo:
        anioMasAntiguo = anio
        fechaCompletaCancionMasAntigua = lanzamientoo
        cancionMasAntigua = nombreCancion
    elif anio > anioMasReciente:
        anioMasReciente = anio
        fechaCompletaCancionMasReciente = lanzamientoo
        cancionMasReciente = nombreCancion
        
    
    #El algoritmo para realizar el item 5
    tiempoTotalReproducido += duracion
    
    
    linea = arch.readline().strip()
    
    
    
print("----------------------------------------")
print("Menu Servicios Spotify\n")
print("1. Cantidad de canciones.")
print("2. Canción menor y mayor duración.")
print("3. Álbum de la canción más reproducida en los 70’s.")
print("4. Canción menor y mayor antigüedad.")
print("5. Horas totales reproducidas.")
print("6. Salir.")
print("----------------------------------------")
    
opcion = int(input("Ingrese una opción: "))
    
while opcion < 0 or opcion > 6:
    opcion = int(input("Ingrese una opción correcta!: "))
        
    
while opcion >= 1 or opcion < 6:
    if opcion == 1:
        print("La cantidad de canciones es:", str(cantCanciones))
            
        print("----------------------------------------")
        print("Menu Servicios Spotify\n")
        print("1. Cantidad de canciones.")
        print("2. Canción menor y mayor duración.")
        print("3. Álbum de la canción más reproducida en los 70’s.")
        print("4. Canción menor y mayor antigüedad.")
        print("5. Horas totales reproducidas.")
        print("6. Salir.")
        print("----------------------------------------")
        opcion = int(input("Ingrese una opción: "))
            
    elif opcion == 2:
        print("La canción con menor duración es:", cancionMasCorta, "con", segundosAMinutos(duracionCancionMasCorta) , "minutos.")
        print("La canción con mayor duración es:", cancionMasLarga, "con", segundosAMinutos(duracionCancionMasLarga) , "minutos.")
            
        print("----------------------------------------")
        print("Menu Servicios Spotify\n")
        print("1. Cantidad de canciones.")
        print("2. Canción menor y mayor duración.")
        print("3. Álbum de la canción más reproducida en los 70’s.")
        print("4. Canción menor y mayor antigüedad.")
        print("5. Horas totales reproducidas.")
        print("6. Salir.")
        print("----------------------------------------")
        
        opcion = int(input("Ingrese una opción: "))
            
    elif opcion == 3:
        print("El álbum con la canción mas reproducida en los 70's es:", albumMasReproducido, "con", str(reproduccionesCancionMasReproducida70s), "reproducciones.")
            
        print("----------------------------------------")
        print("Menu Servicios Spotify\n")
        print("1. Cantidad de canciones.")
        print("2. Canción menor y mayor duración.")
        print("3. Álbum de la canción más reproducida en los 70’s.")
        print("4. Canción menor y mayor antigüedad.")
        print("5. Horas totales reproducidas.")
        print("6. Salir.")
        print("----------------------------------------")
        opcion = int(input("Ingrese una opción: "))
            
    elif opcion == 4:
        print("La canción más antigua es", cancionMasAntigua, "y su fecha de lanzamiento es", fechaCompletaCancionMasAntigua)
        print("La canción más reciente es", cancionMasReciente, "y su fecha de lanzamiento es", fechaCompletaCancionMasReciente)
            
        print("----------------------------------------")
        print("Menu Servicios Spotify\n")
        print("1. Cantidad de canciones.")
        print("2. Canción menor y mayor duración.")
        print("3. Álbum de la canción más reproducida en los 70’s.")
        print("4. Canción menor y mayor antigüedad.")
        print("5. Horas totales reproducidas.")
        print("6. Salir.")
        print("----------------------------------------")
        opcion = int(input("Ingrese una opción: "))
            
    elif opcion == 5:
        print("Las horas totales reproducidas son", str(segundosAHoras(tiempoTotalReproducido)))
            
        print("----------------------------------------")
        print("Menu Servicios Spotify\n")
        print("1. Cantidad de canciones.")
        print("2. Canción menor y mayor duración.")
        print("3. Álbum de la canción más reproducida en los 70’s.")
        print("4. Canción menor y mayor antigüedad.")
        print("5. Horas totales reproducidas.")
        print("6. Salir.")
        print("----------------------------------------")
        opcion = int(input("Ingrese una opción: "))
            
    elif opcion == 6:
        print("Hasta luego :D.")
        break
            
            
            
            
            
            
            
            
            
            
            
            
    
    