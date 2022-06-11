# r, leer: r abre un archivo para lectura y si ek archivo no existe sale un error
#    es el valor por defecto
# w, escribir: abre el archivo para escribir desde el inicio del archivo
#    si el archivo no existe lo crea
# a, agregar: abre el archivo para agregar información
#    si el archivo no existe lo crea
archivo1 = open('prueba.txt', 'rt') #rt es el valor por defecto 
print(archivo1.read(5))
print(archivo1.readline())
print(archivo1.readlines())
archivo1.close()

archivo2 = open('prueba2.txt','w')
archivo2.write('Estoy utilizando "w", para escribir en un archivo\n')
archivo2.write('Hola mundo')
archivo2.close()

lista = ['Medellin', 'Popayán', 'Cali', 'Nariño']
archivo2 = open('prueba2.txt','w', encoding='utf-8')  
for i in lista:
    archivo2.write(i)
    archivo2.write('\n')
archivo2.close()

lista2 = ['Barranquilla', 'Bucaramanga', 'Tunja']
archivo2 = open('prueba2.txt','a', encoding='utf-8')
for i in lista2:
    archivo2.write(i)
    archivo2.write('\n')
archivo2.close()


