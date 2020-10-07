import random


def ingresa_Filas_columnas(): #Pide los datos de la matriz al usuario e inicia el proceso para la matriz.
    filas = int(input ("N° Filas: "))
    columnas = int(input("N° Columnas: "))
    matriz = genera_Matriz(filas,columnas)
   # matriz = valores_Aleatorios_Matriz(matriz,filas, columnas)
    matriz = valores_Usuario_Matriz(matriz,filas,columnas)
    matriz = pivote_Matriz(matriz, columnas, filas)
    imprime_matriz(matriz)


def genera_Matriz(filas, columnas): #Creacion de la matriz.
    matriz = []
    for i in  range(filas):
        matriz.append([0]*columnas)
    return matriz

def valores_Aleatorios_Matriz(matriz, filas, columnas): #Coloca valores aleatorios en la matriz.
    for f in range(filas):
        for c in range(columnas):
            if f != c:
                matriz[f][c]=1
            else:
                matriz[f][c]=f+1
    return matriz

def valores_Usuario_Matriz(matriz, filas, columnas): #El usuario ingresa  los datos.
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c]= int(input('Ingresa el valor en la posicion [{}] [{}]' .format(f+1, c+1)))
    return matriz

def imprime_matriz(matriz): #Imprime la matriz
     for f in matriz:
            print(f) 

def pivote_Matriz(matriz, columnas, filas): #Si en la posicion 0,0 es diferente de 1, entonces buscaremos un pivote.
    if matriz[0][0] != 1:
        for f in range(filas):
            for c in range(columnas):
                if matriz[f][0] == 1 and f>0 :
                    print("la fila {} contiene el pivote" .format(f+1))
                    matriz= cambio_Filas(matriz, f,columnas)
                    break
    return matriz


def cambio_Filas(matriz, fila,columnas): #Cambiamos la fila que contiene el pivote a la primera y viceversa.
    print("\n Pivote encontrado F{} <==> F1" .format(fila+1)) 
    for fila in range(fila+1):
        for c in range(columnas):
            temporal=matriz[0][c]       
            matriz[0][c]=matriz[fila][c]
            matriz[fila][c]=temporal
    return matriz


ingresa_Filas_columnas() #Inicializa el programa

