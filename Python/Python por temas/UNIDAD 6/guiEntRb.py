# mini calculadora
import tkinter as tk
from tkinter import messagebox as mb
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title('Mini Calc')
        self.lblNum1 = tk.Label(self.ventana1, text= "Ingrese el número 1")
        self.lblNum1.grid(row=0, column= 0)
        self.lblNum2 = tk.Label(self.ventana1, text= "Ingrese el número 2")
        self.lblNum2.grid(row=0, column=2)   
        self.num1 = tk.StringVar()     
        self.entNum1 = tk.Entry(self.ventana1, textvariable=self.num1)
        self.entNum1.grid(row=1, column=0)
        self.num2 = tk.StringVar()
        self.entNum2 = tk.Entry(self.ventana1, textvariable=self.num2)
        self.entNum2.grid(row=1, column=2)
        self.opcion= tk.IntVar()
        self.rbSuma = tk.Radiobutton(self.ventana1, text = '+', variable=self.opcion, value = 1)
        self.rbSuma.grid(row=2, column=1)
        self.rbResta = tk.Radiobutton(self.ventana1, text = '-', variable=self.opcion, value = 2)
        self.rbResta.grid(row=3, column=1)
        self.rbMul = tk.Radiobutton(self.ventana1, text = '*', variable=self.opcion, value = 3)
        self.rbMul.grid(row=4, column=1)
        self.rbDiv = tk.Radiobutton(self.ventana1, text = '/', variable=self.opcion, value = 4)
        self.rbDiv.grid(row=5, column=1)
        self.btnOperacion = tk.Button(self.ventana1, text='=',command=self.operaciones)
        self.btnOperacion.grid(row=6, column=0)
        self.lblResultado = tk.Label(self.ventana1, text='--', foreground='red')
        self.lblResultado.grid(row=6, column=2)
        
        self.ventana1.mainloop()
    def operaciones(self):
        try:
            if self.opcion.get() ==1:
                op = float(self.num1.get())+float(self.num2.get())
                self.lblResultado['text']= op
            if self.opcion.get() ==2:
                op = float(self.num1.get())-float(self.num2.get())
                self.lblResultado['text']= op
            if self.opcion.get() ==3:
                op = float(self.num1.get())*float(self.num2.get())
                self.lblResultado['text']= op
            if self.opcion.get() ==4:
                    op = float(self.num1.get())/float(self.num2.get())
                    self.lblResultado['text']= op
        except ZeroDivisionError:
            mb.showinfo("Informacion",'División por cero, no válida')
            #self.lblResultado['text']='División por cero, no válida'
            
        except ValueError:
            mb.showerror('Error','Por favor solo ingrese números')
            #self.lblResultado['text']='Por favor solo ingrese números'
        except:
            self.lblResultado['text']='Algo salió mal'

x = Aplicacion()
    