""" Módulo: TKinter
    Widgets: son elementos que componen la interfaz gráfica como por ejemplo:
    botones, cajas de texto, botón radial, etiquetas, etc
"""

import tkinter as tk    # importamos la librería necesaria para el desarrollo de entornos gráficos, usamos 'tk' por convención

ventana1 = tk.Tk()      # el método 'Tk' crea una ventana principal
ventana1.title('Hola mundo')    # modificamos el titulo de la ventana
ventana1.mainloop()     # se encarga de mantener la ventana abierta 

# al ejecutar este archivo, deveníamos poder ver una ventana flotante con el titulo de 'Hola mundo' en la pestaña 

#   appEnd