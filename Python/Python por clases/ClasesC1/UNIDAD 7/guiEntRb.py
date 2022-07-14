""" Construir una Aplicacion que modele una calculadora sencilla, con las cuatro operaciones básicas para analizar el manejo de Numeros enteros
"""
#------------------------IMPORTACIONES---------------------------
import tkinter as tk    # importamos la librería de tkinter
from tkinter import messagebox as mb
#------------------------ZONA DE CÓDIGO------------------------
class Aplicacion:   # clase principal de la Aplicacion
    def __init__(self):                                                                             # constructor del elemento
        self.ventana1 = tk.Tk()                                                                     # ventana principal
        self.ventana1.title('Mini Calc')                                                            # titulo de la ventana principal
        self.lblNum1 = tk.Label(self.ventana1, text= "Ingrese el número 1")                         # etiqueta 1
        self.lblNum1.grid(row=0, column= 0)                                                         # ubicamos la etiqueta 1
        self.lblNum2 = tk.Label(self.ventana1, text= "Ingrese el número 2")                         # etiqueta 2
        self.lblNum2.grid(row=0, column=2)                                                          # ubicamos la etiqueta 2
        self.num1 = tk.StringVar()                                                                  # variable especial de captura de informacion mediante interfaz gráfica
        self.entNum1 = tk.Entry(self.ventana1, textvariable=self.num1)                              # entrada de texto o caja de texto, método de captura de informacion
        self.entNum1.grid(row=1, column=0)                                                          # posicionamos la caja de texto
        self.num2 = tk.StringVar()                                                                  # creamos una variable de almacenamiento para una segunda caja de texto
        self.entNum2 = tk.Entry(self.ventana1, textvariable=self.num2)                              # creamos una segunda caja de texto
        self.entNum2.grid(row=1, column=2)                                                          # posicionamos la caja de texto en la grilla
        self.opcion= tk.IntVar()                                                                    # las variables anteriores fueron cadenas de texto, en este caso creamos una variable de tipo entero
        self.rbSuma = tk.Radiobutton(self.ventana1, text = '+', variable=self.opcion, value = 1)    # creamos un botón en la ventana principal, con el texto '+', almacena su valor en 'opcion' cuando es clickado y le damos el valor de '1' para indicar que es el primer botón, es un botón de selección, osea que se mantendrá seleccionado hasta que se seleccione otra opcion
        self.rbSuma.grid(row=2, column=1)                                                           # lo posicionamos en la grilla
        self.rbResta = tk.Radiobutton(self.ventana1, text = '-', variable=self.opcion, value = 2)   # creamos el botón 2
        self.rbResta.grid(row=3, column=1)                                                          # lo posicionamos en la grilla
        self.rbMul = tk.Radiobutton(self.ventana1, text = '*', variable=self.opcion, value = 3)     # creamos el botón 3
        self.rbMul.grid(row=4, column=1)                                                            # lo posicionamos en la grilla
        self.rbDiv = tk.Radiobutton(self.ventana1, text = '/', variable=self.opcion, value = 4)     # creamos el botón 4
        self.rbDiv.grid(row=5, column=1)                                                            # lo posicionamos en la grilla
        self.btnOperacion = tk.Button(self.ventana1, text='=',command=self.operaciones)             # creamos un botón con el texto '=' posicionado en la ventana principal y que desencadena el método 'operaciones' cuando es pulsado
        self.btnOperacion.grid(row=6, column=0)                                                     # ubicamos el botón Operacion en la grilla
        self.lblResultado = tk.Label(self.ventana1, text='--', foreground='red')                    # etiqueta que muestra el resultado en la interfaz, con un texto temporal y le asignamos rojo al texto
        self.lblResultado.grid(row=6, column=2)                                                     # ubicamos la etiqueta en la grilla
        
        self.ventana1.mainloop()                                                                    # loop principal de la interfaz gráfica
    def operaciones(self):                                                                          # método principal de la lógica interna o "backend" aquí se harán todos los procesos que no implican interacción directa con el usuario en el codigo, se incluye dentro de la clase principal para manejar los valores de variables directamente
        try:                                                                                        # modelamos dentro de un try/except para poder modelar errores cuando los resultados de las operaciones sean inválidos o matemáticamente incoherentes o no definidos
            if self.opcion.get() ==1:                                                               # hacemos un crud simple, en el que dependiendo del valor obtenido al momento de presionar algún botón, efectuaran la Operacion pertinente
                op = float(self.num1.get())+float(self.num2.get())                                  # creamos una variable temporal donde almacenaremos el resultado de la Operacion, como los datos son almacenados dentro de strings, necesitamos convertirlas en variables operables matemáticamente, y como existe la posibilidad de una Operacion con Numeros decimales, usamos la conversion a Numeros de punto flotante 
                self.lblResultado['text']= op                                                       # actualizamos la etiqueta con el resultado obtenido para que se muestre en pantalla 
            if self.opcion.get() ==2:
                op = float(self.num1.get())-float(self.num2.get())
                self.lblResultado['text']= op
            if self.opcion.get() ==3:
                op = float(self.num1.get())*float(self.num2.get())
                self.lblResultado['text']= op
            if self.opcion.get() ==4:
                    op = float(self.num1.get())/float(self.num2.get())
                    self.lblResultado['text']= op
        except ZeroDivisionError:                                                                   # modelamos los casos de error, en este caso, python nos ofrece una clase que contiene el error de 'division por cero' previamente modelado por lo que lo único que tenemos que modelar es el mensaje que queremos que muestre en pantalla
            mb.showinfo("Informacion",'División por cero, no válida')
            #self.lblResultado['text']='División por cero, no válida'
            
        except ValueError:                                                                          # también hay una clase que modela el error de valor, este error salta cuando se introduce un carácter de valor invalido como puede ser una letra u otro elemento no matemáticamente operable
            mb.showerror('Error','Por favor solo ingrese números')
            #self.lblResultado['text']='Por favor solo ingrese números'
        except:
            self.lblResultado['text']='Algo salió mal'                                              # modelamos un posible error no contemplado en primera instancia

#------------------------INICIALIZACIONES---------------------------
x = Aplicacion()

#   appEnd