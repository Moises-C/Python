from random import randint 
import tkinter as tk


class Matrix():
    #Constructor de la clase
    def __init__(self, filas, columnas): 
        self.filas=filas
        self.columnas=columnas
        self.__matriz = []
        self.__ventana = tk.Tk()
        self.__matriz = []
        self.__valor = []

    def valoresUsuarioMatriz(self): #Coloca valores aleatorios en la matriz.

        for f in range(self.filas):

            self.__valor.append([0]*self.columnas)
            self.__matriz.append([0]*self.columnas)

            for c in range(self.columnas):

                self.__valor[f][c] =tk.IntVar() #Crea espacios para guardar los valores de los entrys
                entrada = tk.Entry(self.__ventana, width = 10, textvariable = self.__valor[f][c])
                entrada.grid(padx=2, pady=2,row = f, column = c)  
            
        boton = tk.Button(self.__ventana, text = "listo", command = self.guardaValoresMatrizAux)
        boton.grid(row = f+2, column = c+2)
        self.__ventana.mainloop()
        return self.__matriz

    def guardaValoresMatrizAux(self):

        for f in range(self.filas):
            for c in range(self.columnas):

                self.__matriz[f][c]= self.__valor[f][c].get() #Obtenemos valores de los entry para guardarlos en orden dentro de la matriz 
        return self.__matriz
    '''
    def valoresUsuarioMatriz(self): #El usuario ingresa  los datos.
        for f in range(self.filas):
           for c in range(self.columnas):
                self.__matriz[f][c]= int(input('Ingresa el valor en la posicion [{}] [{}]' .format(f+1, c+1)))
        return self.__matriz
    '''
    
matriz = Matrix(3,3)
matrizR = matriz.valoresUsuarioMatriz()
matrizR = matriz.guardaValoresMatrizAux()
for i in matrizR:
    print(i)
