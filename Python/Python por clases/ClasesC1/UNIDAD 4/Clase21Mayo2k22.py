""" instalamos y vemos el tema de pandas

    instalación:
    digitados en consola el comando
        conda install pandas
    esperamos a que complete la instalación, si sale un mensaje del tipo
        The following packages will be UPDATED:

        conda 4.10.3-py39haa95532_0 --> 4.13.0-py39haa95532_0

        Proceed ([y]/n)?  
    digitados 'y' para conceder el permiso para la actualización de paquetes
    
    finalizada la instalación podemos proceder con el siguiente codigo
"""

""" Las series son estructuras similares a los arrays de una dimensión. Son homogéneas, es decir,
    sus elementos tienen que ser del mismo tipo, y su tamaño es inmutable, es decir, 
    no se puede cambiar, aunque si su contenido.
    Dispone de un índice que asocia un nombre a cada elemento del la serie, 
    a través de la cuál se accede al elemento.
"""
import pandas as pd #   asi como en numpy, importamos las propiedades de la librería pandas en un elemento llamado 'pd'

#   creamos un diccionario base
inventario = {
    'Impresoras': ['Hp', 'Epson', 'Canon'],
    'Cantidad':[8,10,5]     
}

InvPandas = pd.DataFrame(inventario)    # el comando dataframe crea una tabla con la informacion proporcionada por la series
print(inventario)                       # podemos entender a las series como vectores, y en cada variable de este, es el indice de un valor a guardar
print('------------------------------') # un dataframe es la organización de vectores de similares dimensiones
print(InvPandas)

ciudades = ['Cali', 'Barranquilla', 'Cartagena']    # una serie de una dimension organiza un vector de valores de indexacion 
SerPanda = pd.Series(ciudades)
print(ciudades)
print(SerPanda)

ventas = {
    'enero': 2000000.0,
    'febrero': 3500000.0,
    'marzo': 4000000.0
}

#print(ventas.keys())
ventasPan = pd.Series(data = ventas, index = list(ventas.keys())) # aquí le agregamos un indice personalizado a la serie, pues en vez de organizar con enteros positivos cada elemento del diccionario, lo asignamos con llaves personalizadas 
ventasPan.name = "Ventas primer trimestre"  # personalizamos el nombre de la serie 
print(ventasPan)
print(ventasPan['enero'])   # podemos solicitar los valores guardados por su indice o por su posición en el vector
print(ventasPan[0])
print(ventasPan.values)     # retorna los valores de cada llave asociada al vector
print(ventasPan.keys)       # retorna las llaves y sus valores, incluyendo el nombre de la serie

#   appEnd