""" continuamos con la unidad 5, en este caso haremos la introducción a mas elementos y propiedades de los documentos
    tipo CSV
"""
import pandas as pd # importamos pandas

diccionario = {
        'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
}
df1 = pd.DataFrame(diccionario)
# como vimos las rutas se pueden establecer con doble backslash o con slash simple
df1.to_csv('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\ejemploCsv.csv')
pd.options.display.max_rows = 10    # imprime un máximo de 10 lineas en consola
df2 = pd.read_csv('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\casos_covid.csv', header=None)
print(df2)
#   explicación de parámetros:
#       (sep='|'): indica el separador de lectura, o escritura dependiendo del método de pandas respectivo
#       (names= ['index']): indica los nombres de las columnas
#       (index_col=['Nombre', 'Apellido']): se diferencia de los nombres de columna y sus indices es que los indices permiten acceder a los datos
#       mientras que los nombres son indicativos visuales de las columnas
#       (skiprows=1): esto salta la cantidad de filas indicada desde la primera en adelante, en este caso salta la primera fila
df3 = pd.read_csv('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\ejemploCsv.csv', sep=',', names= ['index', 'Nombre', 'Apellido','Edad','Ventas1', 'Ventas2'], na_values=["?"], index_col=['Nombre', 'Apellido'], skiprows=1)
print(df3)

""" ahora vamos a ver la manipulación (lectura, escritura y modificación) de  archivos  de texto
    a la hora de manipular archivos de texto, tenemos parámetros llamados 'modos de apertura'
    estos son un carácter que se le pasa a los distintos métodos de manipulación de archivos (ejemplo 'r' o 'w')
    que indican la acción a realizar sobre el documento, los mas comunes son:
        r, leer: r abre un archivo para lectura y si el archivo no existe sale un error es el valor por defecto
        w, escribir: abre el archivo para escribir desde el inicio del archivo si el archivo no existe lo crea
        a, agregar: abre el archivo para agregar información si el archivo no existe lo crea
    aquí también la ruta de acceso a los documentos es especifica para este proyecto, tenlo en cuenta si solo quieres descargar este documento de python
"""
archivo1 = open('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\prueba.txt', 'rt') # rt viene de 'r' leer y 't' de texto, osea que indica 'lectura sobre archivo de texto' su sinónimo es 'r' pues 'r' por defecto presupone que se leerá un archivo de texto 
print(archivo1.read(5))     # el método read, lee la informacion dentro del documento, si le introducimos un entero a este método, nos retorna los primeros 'n' caracteres del documento, siendo n el numero introducido

#   NOTA:el método read deja un registro de hasta donde leyó el archivo de texto, por esto si se le indica leer todo el documento y posteriormente se le solicita una nueva lectura, retornara un renglón vació,
#   pues ya completó la lectura del archivo, esto permite el procesamiento de los datos 

print(archivo1.readline())  # este método lee un renglón completo del documento de texto, si se le indica un entero n, retornará la cantidad de caracteres indicada de la linea actual, si se repite el método, leerá desde donde lo dejó anteriormente  
print(archivo1.readlines()) # este método retorna todas los renglones del documento, organizado dentro de una lista
archivo1.close()            # cierra el archivo, impidiendo posteriores ediciones o manipulaciones

archivo2 = open('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\prueba2.txt','w')   # el parámetro 'w' indica que escribiremos en el documento
#   NOTA: no podremos leer la informacion del archivo hasta que terminemos la edición y lo cerremos
archivo2.write('Estoy utilizando "w", para escribir en un archivo\n')   # 'write' escribirá el contenido de la cadena en el documento, sin importar cuantas veces realicemos este proceso, lo agregara todo en la misma linea del documento a menos que le indiquemos un salto de linea con '\n'  
archivo2.write('Hola mundo')
archivo2.close()


lista = ['Medellin', 'Popayán', 'Cali', 'Nariño']
archivo2 = open('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\prueba2.txt','w', encoding='utf-8') # 'encoding' permite cambiar el codificador por defecto del archivo de texto, en este caso lo hacemos para que el archivo reconozca tildes y 'ñ' pues estos caracteres no existen en ingles (codec por defecto)
#   aquí agregaremos elementos de una lista a un archivo de texto, cada elemento se agregara a una linea independiente
for i in lista:
    archivo2.write(i)
    archivo2.write('\n')
archivo2.close()

#   NOTA: cada vez que realizamos un 'write' sobre un archivo, borrará el contenido existente en este y realizara la escritura nueva, si queremos conservar los datos 
#   existentes en este documento, tenemos que usar el argumento 'a' para agregar nuevo contenido 
lista2 = ['Barranquilla', 'Bucaramanga', 'Tunja']
archivo2 = open('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\prueba2.txt','a', encoding='utf-8')
for i in lista2:
    archivo2.write(i)
    archivo2.write('\n')
archivo2.close()

#   verificamos los cambios realizados
archivo2 = open('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\prueba2.txt','rt', encoding='utf-8')
print(archivo2.read())
archivo2.close()

""" en esta parte, empezaremos con la manipulación y creación de archivos JSON (Java Script Objet Notation) y su uso 
"""
import json
df1 = pd.read_json('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\data.json')  # usamos el método 'read_json' para poder leer los datos dentro de un documento tipo json y agregamos su informacion a una serie
print(df1.to_string())  # usamos el método 'to_string' para convertir los datos del archivo json en una cadena, la cual puedo imprimir

diccionario ={
    "nombre":"Juan",
    "edad": 25,
    "profesion": "contador",
    "hijos": ['Ana', 'Julián'],
    "mascotas": None,
    "divorciado": False    
}
archivo3 = json.dumps(diccionario, indent=4, ensure_ascii=False)    # el método 'dumps' crea un string en formato json a partir de un objeto 
print(archivo3)                                                     # 'indent' agrega los niveles de identacion introducidos por el usuario 
print(type(archivo3))                                               # ensure:ascii=False quita la limitación del documento a caracteres tipo ascii y permite la representación de caracteres adicionales, como lo pueden ser las tildes o las 'ñ'

#   appEnd