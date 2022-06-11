""" iniciamos con la unidad 5, la cual consta de manejo de archivos externos a python, como en este caso
    archivos tipo CSV, Las siglas CSV vienen del inglés "Comma Separated Values" y significan valores separados
    por comas. Dicho esto, un archivo CSV es cualquier archivo de texto en el cual los caracteres están separados 
    por comas, haciendo una especie de tabla en filas y columnas. Las columnas quedan definidas por cada punto y coma (;)
    mientras que cada fila se define mediante una línea adicional en el texto. 

    también usaremos documentos de tipo JSON, json es un archivo que contiene una serie de datos estructurados en formato de 
    texto y se usa para transferir información entre sistemas. Es importante decir que, a pesar de su origen estar en el lenguaje 
    JavaScript, JSON no es un lenguaje de programación
    
    NOTA: usaremos rutas de acceso a carpetas especificas para la organización del proyecto, es probable que si descargas los archivos, al no tener la
    misma ruta, arroje un error, ten encuentra esto para tu proyecto
"""
import pandas as pd # importamos pandas

diccionario = {
        'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
}

df1 = pd.DataFrame(diccionario) # creamos un dataframe con los datos del diccionario

print(df1)
#df1.to_csv('DiccionarioCsv.csv', sep='|', header=None) aquí creamos un documento de tipo .csv, 
#   la separación de elementos se hace con un '|' y sin un header (nombre de tabla) especifico, 
#   el archivo se creara en la carpeta principal del proyecto (G20 en este caso)
#df2 = pd.read_csv('Libro1.csv') con este comando podemos leer los datos de del documento 'libro.csv',
#   si no se le indica la ruta, lo buscara en la carpeta principal del proyecto

 
# aquí creamos un documento de tipo .csv, la separación de elementos se hace con un ',' porque pandas suele crear los dataframe, separados con comas
# y sin un header (nombre de tabla) especifico, el archivo se creara en la carpeta indicada
df1.to_csv('C:/Users/HP/Downloads/G20/Python/Python por temas/UNIDAD 5/DiccionarioCsv.csv', sep=',', header=None) 
# aquí le indicamos una ruta en especifico, para poder leer el archivo ubicado en cualquier otra carpeta que no sea la principal del proyecto
# le indicamos el separador con el que esta dispuesto el csv para que se cree correctamente el dataframe y se organicen bien los datos
df2 = pd.read_csv('C:/Users/HP/Downloads/G20/Python/Python por temas/UNIDAD 5/Libro1.csv',sep=';')
print(df2)
# aquí tenemos que tener en cuenta que el separador con el que se creo el documento, si no, aunque si que va a leer el documento,
# no va a entender las separaciones de los datos
df3 = pd.read_csv('C:/Users/HP/Downloads/G20/Python/Python por temas/UNIDAD 5/DiccionarioCsv.csv', sep=',') 
print(df3)

#   appEnd