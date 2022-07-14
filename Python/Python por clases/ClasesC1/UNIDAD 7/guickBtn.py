""" Creamos una pequeña Aplicacion que cuenta cuantas de las casillas creadas han sido seleccionadas para estudiar el comportamiento de las checkBox en tk
"""
#------------------------IMPORTACIONES---------------------------
import tkinter as tk    # importamos la librería de tkinter
#------------------------ZONA DE CÓDIGO------------------------
class Aplicacion:
    def __init__(self):                                                                                                     # método constructor de la Aplicacion
        self.ventana1 = tk.Tk()                                                                                             # creamos la ventana principal
        self.selec1 = tk.IntVar()                                                                                           # variable que almacena el estado de la primera checkBox
        self.chkBtn1 = tk.Checkbutton(self.ventana1, text='Pensamiento lógico', variable=self.selec1)                       # creamos el primer checkBox, en la ventana principal, con le texto de 'Pensamiento lógico' y almacena su estado en la anterior variable
        self.chkBtn1.grid(row=0, column=0)                                                                                  # ubicamos el elemento en la grilla
        self.selec2 = tk.IntVar()                                                                                           # variable que almacena el estado de la segunda checkBox
        self.chkBtn2 = tk.Checkbutton(self.ventana1, text='Trabajo en equipo', variable=self.selec2)                        # creamos la segunda checkBox
        self.chkBtn2.grid(row=1, column=0)                                                                                  # ubicamos el elemento en la grilla
        self.selec3 = tk.IntVar()                                                                                           # variable que almacena el estado de la tercera checkBox
        self.chkBtn3 = tk.Checkbutton(self.ventana1, text='Disciplina', variable=self.selec3)                               # creamos la tercera checkBox
        self.chkBtn3.grid(row=2, column=0)                                                                                  # ubicamos el elemento en la grilla                
        self.selec4 = tk.IntVar()                                                                                           # variable que almacena el estado de la cuarta checkBox
        self.chkBtn4 = tk.Checkbutton(self.ventana1, text='Aceptar', variable=self.selec4, command=self.cambiarEstado)      # creamos una checkBox especial que habilitara o no el botón de contar, afectando el estado del botón dependiendo del estado propio
        self.chkBtn4.grid(row=3, column=0)                                                                                  # ubicamos el elemento en la grilla
        self.btnContar = tk.Button(self.ventana1, text='Contar', state = 'disabled', command= self.contarSeleccion)         # creamos el botón 'contar' que efectuara el método 'contar Seleccion' al ser presionado. solo se habilitara el botón cuando el estado del checkBox 'Aceptar' sea marcado inicia deshabilitado por defecto
        self.btnContar.grid(row=4, column=0)                                                                                # ubicamos el elemento en la grilla
        self.lblMostrar = tk.Label(self.ventana1, text='')                                                                  # etiqueta donde se muestra el resultado en pantalla
        self.lblMostrar.grid(row=5, column=0)                                                                               # ubicamos el elemento en la grilla
        self.ventana1.mainloop()                                                                                            # loop principal del entorno gráfico
    def contarSeleccion(self):                                                                                              # modelamos el método contador, actualiza la cuenta dependiendo del estado de las casillas, y suma +1 cuando esta seleccionada alguna de las casillas
        Conta = 0
        if self.selec1.get() == 1:
            Conta+=1
        if self.selec2.get() == 1:
            Conta+=1
        if self.selec3.get() == 1:
            Conta+=1
        self.lblMostrar['text'] = Conta                                                                                     # actualizamos la etiqueta con la cantidad de casillas seleccionadas actualmente
    def cambiarEstado(self):                                                                                                # modelamos el metodo que cambia el estado del botón 'Contar' dependiendo del estado de la casilla 'Aceptar'
        if self.selec4.get() == 1:                                                                                          # dependiendo del estado de la variable asociada a la casilla (1 para marcada, 0 para desmarcada) le asigna un estado de habilitado o deshabilitado
            self.btnContar['state']= 'normal'
        if self.selec4.get() == 0:
            self.btnContar['state']= 'disabled'
         
        
#------------------------INICIALIZACIONES---------------------------            
x = Aplicacion()

#   appEnd