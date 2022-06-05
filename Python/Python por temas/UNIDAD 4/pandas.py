import pandas as pd #   asi como en numpy, importamos las propiedades de la librería pandas en un elemento llamado 'pd'
inventario = {
    'Impresoras': ['Hp', 'Epson', 'Canon'],
    'Cantidad':[8,10,5]     
}
InvPandas = pd.DataFrame(inventario)
print(inventario)
print('------------------------------')
print(InvPandas)

ciudades = ['Cali', 'Barranquilla', 'Cartagena']
SerPanda = pd.Series(ciudades)
print(ciudades)
print(SerPanda)

ventas = {
    'enero': 2000000.0,
    'febrero': 3500000.0,
    'marzo': 4000000.0
}

#print(ventas.keys())
ventasPan = pd.Series(data = ventas, index = list(ventas.keys()))
ventasPan.name = "Ventas primer trimestre"
print(ventasPan)
print(ventasPan['enero'])
print(ventasPan[0])
print(ventasPan.values)
print(ventasPan.keys)