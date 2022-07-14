# checkButton
import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.selec1 = tk.IntVar()
        self.chkBtn1 = tk.Checkbutton(self.ventana1, text='Pensamiento lógico', variable=self.selec1)
        self.chkBtn1.grid(row=0, column=0)
        self.selec2 = tk.IntVar()
        self.chkBtn2 = tk.Checkbutton(self.ventana1, text='Trabajo en equipo', variable=self.selec2)
        self.chkBtn2.grid(row=1, column=0)
        self.selec3 = tk.IntVar()
        self.chkBtn3 = tk.Checkbutton(self.ventana1, text='Disciplina', variable=self.selec3)
        self.chkBtn3.grid(row=2, column=0)
        self.selec4 = tk.IntVar()
        self.chkBtn4 = tk.Checkbutton(self.ventana1, text='Aceptar', variable=self.selec4, command=self.cambiarestado)
        self.chkBtn4.grid(row=3, column=0)
        self.btnContar = tk.Button(self.ventana1, text='Contar', state = 'disabled', command= self.contarSeleccion)
        self.btnContar.grid(row=4, column=0)
        self.lblMostar = tk.Label(self.ventana1, text='')
        self.lblMostar.grid(row=5, column=0)
        self.ventana1.mainloop()
    def contarSeleccion(self):
        conta = 0
        if self.selec1.get() == 1:
            conta+=1
        if self.selec2.get() == 1:
            conta+=1
        if self.selec3.get() == 1:
            conta+=1
        self.lblMostar['text'] = conta
    def cambiarestado(self):
        if self.selec4.get() == 1:
            self.btnContar['state']= 'normal'
        if self.selec4.get() == 0:
            self.btnContar['state']= 'disabled'
         
        
        
        
x = Aplicacion()
