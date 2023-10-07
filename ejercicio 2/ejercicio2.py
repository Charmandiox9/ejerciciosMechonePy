def calcularIMC(peso, altura):
    imc = 0.0
    
    imc  = peso /  (centiAMetros(altura)**2)
    
    return round(imc, 2)


def centiAMetros(cms):
    metros = 0.0
    
    metros = cms / 100
    
    return metros



arch = open("datos.txt", "r", encoding = "utf-8")
linea = arch.readline().strip()

#Variables item 1
cantPersonasAfiliadas = 0 #Contador para personas afiliadas
cantPersonasNoAfiliadas = 0 #Contador para personas no afiliadas

#Variables item 2
sumaEdadesAfiliadas = 0 #Sumador de edades de todas las personas afiliadas
cantPersonasAfiliadas = 0 #Contador para personas afiliadas

#Variables item 3
nombrePersonaMenorIMC = "" #Se guardara el nombre de la persona con menor IMC
menorIMC = 10000.0 #Se guardara el IMC menor
nombrePersonaMayorIMC = "" #Se guardara el nombre de la persona con mayor IMC
mayorIMC = -1.0 #Se guardara el IMC mayor

#Variables item 4
cantPersonasMayoresA178m = 0 #Se guardara la cantidad de personas que tengan altura mayor a 1.78m y que no esten afiliadas



while linea != "":
    partes = linea.split(",")
    nombre = partes[0]
    edad = int(partes[1])
    altura = int(partes[2])
    peso = int(partes[3])
    afiliacion = partes[4]
    
    
    #Algoritmo item 1
    if afiliacion == "afiliado":
        cantPersonasAfiliadas += 1
    elif afiliacion == "no afiliado":
        cantPersonasNoAfiliadas += 1
        
        
    #Algoritmo item 2
    if afiliacion == "afiliado":
        sumaEdadesAfiliadas += edad
    
    
    #Algoritmo item 3
    if edad > 40 and edad < 70:
        if calcularIMC(peso, altura) < menorIMC:
            menorIMC = calcularIMC(peso, altura)
            nombrePersonaMenorIMC = nombre
        elif calcularIMC(peso, altura) > mayorIMC:
            mayorIMC = calcularIMC(peso, altura)
            nombrePersonaMayorIMC = nombre
    
    #Algoritmo para item 4
    if afiliacion == "no afiliado":
        if centiAMetros(altura) >= 1.78:
            cantPersonasMayoresA178m += 1
            
        
    #Pasamos a la siguiente linea
    linea = arch.readline().strip()
    
    
print("--------------------------")
print("Menu de Servicios\n")
print("1. Cantidad de personas afiliadas/no afiliadas.")
print("2. Promedio edades de personas afiliadas.")
print("3. Nombre personas mayor y menor IMC (mayores de 40 y menores de 70).")
print("4. Cantidad de personas mayores a 1.78m.")
print("5. Salir.")
print("--------------------------")
    
opcion = int(input("Ingrese una opción: "))
    
while opcion < 1 or opcion > 5:
    opcion = int(input("Ingrese una opción correcta!!: "))
        
        
while opcion >= 1 or opcion < 5:
    if opcion == 1:
        print("La cantidad de personas afiliadas es: ", str(cantPersonasAfiliadas), "personas")
        print("La cantidad de personas no afiliadas es: ", str(cantPersonasNoAfiliadas), "personas")
            
        print("--------------------------")
        print("Menu de Servicios\n")
        print("1. Cantidad de personas afiliadas/no afiliadas.")
        print("2. Promedio edades de personas afiliadas.")
        print("3. Nombre personas mayor y menor IMC (mayores de 40 y menores de 70).")
        print("4. Cantidad de personas mayores a 1.78m.")
        print("5. Salir.")
        print("--------------------------")
            
        opcion = int(input("Ingrese una opción: "))
            
    elif opcion == 2:
        print("El promedio de edades de las personas afiliadas es: ", str(round((sumaEdadesAfiliadas/cantPersonasAfiliadas), 2)))
            
        print("--------------------------")
        print("Menu de Servicios\n")
        print("1. Cantidad de personas afiliadas/no afiliadas.")
        print("2. Promedio edades de personas afiliadas.")
        print("3. Nombre personas mayor y menor IMC (mayores de 40 y menores de 70).")
        print("4. Cantidad de personas mayores a 1.78m.")
        print("5. Salir.")
        print("--------------------------")
            
        opcion = int(input("Ingrese una opción: "))
            
    elif opcion == 3:
        print("El nombre de la persona con mayor IMC es: ", nombrePersonaMayorIMC, ",con un IMC de ", str(mayorIMC))
        print("El nombre de la persona con menor IMC es: ", nombrePersonaMenorIMC, ",con un IMC de ", str(menorIMC))
            
        print("--------------------------")
        print("Menu de Servicios\n")
        print("1. Cantidad de personas afiliadas/no afiliadas.")
        print("2. Promedio edades de personas afiliadas.")
        print("3. Nombre personas mayor y menor IMC (mayores de 40 y menores de 70).")
        print("4. Cantidad de personas mayores a 1.78m.")
        print("5. Salir.")
        print("--------------------------")
            
        opcion = int(input("Ingrese una opción: "))
            
    elif opcion == 4:
        print("La cantidad de personas con estatura mayor a 1.78m es: ", str(cantPersonasMayoresA178m), "personas")
            
            
        print("--------------------------")
        print("Menu de Servicios\n")
        print("1. Cantidad de personas afiliadas/no afiliadas.")
        print("2. Promedio edades de personas afiliadas.")
        print("3. Nombre personas mayor y menor IMC (mayores de 40 y menores de 70).")
        print("4. Cantidad de personas mayores a 1.78m.")
        print("5. Salir.")
        print("--------------------------")
            
        opcion = int(input("Ingrese una opción: "))
            
    elif opcion == 5:
        print("Hasta luego :D.")
        break
    
    
    
    
    
    
    
    