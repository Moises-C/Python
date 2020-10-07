import tkinter

ventana = tkinter.Tk()
matriz = []
num = tkinter.IntVar()
valor=[]



for i in  range(3):
        matriz.append([0]*3)

for i in range (3):
    valor.append([0]*3)
    for j in range(3):
        valor[i][j] =tkinter.IntVar() #Crea espacios para guardar los valores de los entrys
        entrada= tkinter.Entry(ventana, width = 10, textvariable = valor[i][j])
        entrada.grid(padx=2, pady=2,row = i, column = j)      

def guarda():
    for i in range(3):
        for j in range(3):
            matriz[i][j]= valor[i][j].get() #Obtenemos valores de los entry para guardarlos en orden dentro de la matriz 
    imprimir()
    exit()

def imprimir():
    for i in matriz:
        print(i)

def colocar_boton(fil,col):
    boton = tkinter.Button(ventana, text = "listo", command = guarda)
    boton.grid(row = i+2, column = j+2)



colocar_boton(i,j)
ventana.mainloop()