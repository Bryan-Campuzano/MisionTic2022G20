""" continuaremos con mas funcionalidades de pandas, viendo diferentes maneras de acceder a los datos de los archivos CSV
    
    NOTA: el archivo CSV que trabajamos es un archivo cualquiera usado a modo de ejemplo, puedes usar el archivo CSV de tu preferencia y ver 
    como influyen estos métodos y propiedades sobre un archivo personal
"""
import pandas as pd # importamos pandas como es normal

df1 = pd.read_csv('C:\\Users\\HP\\Downloads\\G20\\Python\\Python por temas\\UNIDAD 5\\surveys.csv') # creamos un dataframe con la informacion del documento CSV
print("--------------------------------separador1----------------------------------------------")    # estos separadores nos sirven para poder ver de mejor manera la informacion en la consola
print(df1.head(15)) # imprime las primeras 15 filas del CSV
print("--------------------------------separador2----------------------------------------------")
print(df1.tail(15)) # imprime las ultimas 15 filas del CSV
print("--------------------------------separador3----------------------------------------------")
print(df1.shape)    # retorna las dimensiones del dataframe (filas x columnas)
print("--------------------------------separador4----------------------------------------------")
print(df1.columns)  # retorna una lista con los indices de las columnas
print("--------------------------------separador5----------------------------------------------")
print(pd.unique(df1['species_id'])) # imprime una lista de los datos únicos de la columna indicada (por ejemplo si tengo una lista con manzanas y peras, me retornara [manzana, pera] sin importar la cantidad de cada una)
print("--------------------------------separador6----------------------------------------------")
print(df1['species_id'].value_counts()) # cuenta los datos únicos de la columna indicada (ejemplo, si tenemos una lista de peras y manzanas, nos dice la cantidad de peras y la cantidad de manzanas, al final nos dice de que columna son los datos y el tipo de dato, que al ser cantidades es 'int64')
print("--------------------------------separador7----------------------------------------------")
print(df1['weight'].describe()) # descripción, muestra un resumen de datos de estadística descriptiva de la columna asignada (el promedio, valor mínimo, valor máximo, entre otros valores útiles)
print("--------------------------------separador8----------------------------------------------")
print(df1['weight'].mean()) # Me arroja un promedio de los valores de una columna asignada, en este caso del peso
print("--------------------------------separador9----------------------------------------------")
#   Creamos un grupo con la informacion de la columna 'sex' la cual puedo recorrer igual al dataFrame
#   en este caso separamos el dataFrame en 3 diferentes, una frame de solo machos, otro de solo hembras, y otro con los que no tienen
#   este dato almacenado 
#   (esta linea en consola no va a imprimir nada)
datosGrupoSexo = df1.groupby('sex') 
print("--------------------------------separador10---------------------------------------------")
print(datosGrupoSexo.describe())# obtenemos información del grupo, nos brindara promedios, mínimos y máximos, de cada dato numérico separado por sexo en este caso,
                                # las columnas con elementos no numéricos, serán obviadas
print("--------------------------------separador11---------------------------------------------")
print(datosGrupoSexo.max())     # esto nos retornara, separado por genero, el valor máximo encontrado en cada una de las columnas asociadas, en este caso (la mayor altura femenina y masculina, el mayor peso etc)
print("--------------------------------separador12---------------------------------------------")
#   NOTA: el siguiente método puede ser algo engorroso de entender, asi que aquí la explicación lo mas detallada posible
#   primero agrupamos la informacion separándola por especies. después usamos la columna 'record id' que es una columna consecutiva
#   osea que nos brinda meramente la posición de cada fila, para realizar el filtro. si asociamos las filas a 'individuos' el tenerlos listados y ordenados
#   ayuda a estos procesos de filtrado, pues es como tener un listado de objetos, cada uno con sus características, las cuales son accesibles. después usamos el método 'count' para saber cuantos individuos de cada especie hay en el dataframe.
#   por ultimo le pasamos el parámetro 'NL' siendo NL el indicativo de una especie concreta en este dataframe, lo que estamos solicitando aquí
#   es la cantidad de individuos de esta especie.
#   en resumen, estamos tomando un listado de individuos organizado, los separamos por especie, contamos los individuos por especie y solicitamos el valor de la cuenta para una especie en especifico
print(df1.groupby('species_id')['record_id'].count()['NL'])
""" aquí introducimos nuevas funcionalidades relacionadas con las posiciones de filas y columnas
"""
print("--------------------------------separador A---------------------------------------------")
print(df1.columns)  # retorna una lista con los indices de las columnas
print("--------------------------------separador B---------------------------------------------")
print(df1['month']) # columna de meses solicitada mediante parámetro, también retorna un resumen de la informacion de la columna
print("--------------------------------separador C---------------------------------------------")
print(df1.month)    # columna solicitada mediante método, gracias a las propiedades de los DataFrame
print("--------------------------------separador D---------------------------------------------")
df2 = df1.month     # aquí podemos ver que cada una de las columnas del dataFrame es una serie 
print(type(df1), type(df2)) 
print("--------------------------------separador E---------------------------------------------")
df3 = df1[['species_id','plot_id']] 
print(df3)          # subconjunto de varias columnas, o un frame de solo dos columnas, sacado del documento original
print("--------------------------------separador F---------------------------------------------")
print(df1[10:21])   # imprime de la linea 10 hasta la 21 del dataFrame
print("--------------------------------separador G---------------------------------------------")
print(df1.iloc[0:4,1:3])    # aquí solicitamos las filas del cero al cuatro y del 1 al 3, entiendo en cuenta que 
                            # el rango es cerrado al inicio y abierto al final, osea que imprime las filas del 
                            # cero al 3 y del 1 al 2 por como funcionan los rangos de pandas
print("--------------------------------separador H---------------------------------------------")
print(df1.iloc[[0,4,7],:])  # solicita todos los valores de las filas 0,4 y 7 
print("--------------------------------separador I---------------------------------------------")
print(df1.iloc[4,2])# si al iloc le paso solo un numero, me retorna todos los valores de la fila dada, en este caso
                    # la segunda coordenada me indica que dato lo estoy solicitando al elemento    
print("--------------------------------separador J---------------------------------------------")
print(df1[df1.year==1977]) # filtro de filas según un criterio, retorna todos los elementos que coincidan
print("--------------------------------separador K---------------------------------------------")
print(df1[(df1.year >= 1985) & (df1.year <=1995)])  # las operaciones booleanas también pueden ser simbolizadas con: 
                                                    # and: &, or: |, not:~ 
""" veremos el método de pivote 'pivot_table' que permite crear nuevas formas de organizar la informacion 
    dependiendo de las necesidades del filtro que apliquemos, permitiendo generar frames con nuevas filas y columnas en 
    base a documentos o frames dados
"""
df4 = pd.DataFrame(
    {
        'Nombre': ['Laura','Laura','Laura','Laura','Juan','Juan','Juan','Juan'],
        'Fecha':['03/05/2022','04/05/2022','05/05/2022','05/05/2022','03/05/2022','04/05/2022','05/05/2022','05/05/2022'],
        'Cantidad': [8,2,5,6,8,7,1,2]
    }
)
#   en este caso, el método de pivote toma el dataframe dado, usa la lista de nombres como indices (si se repiten los valores crea una sola fila
#   con el nombre común), es decir, filas y las fechas como columnas (si coinciden algún dato también resume en una sola columna
#   con el valor común, si coincide en ambos, fila y columna, en el valor, de ser numérico, retorna el promedio por defecto)
#   ademas con el parámetro 'aggfunc' permite agregar una lista de funciones, tomara las funciones de la lista y las aplicara a los valores
#   del frame una por una, generando un frame extra por cada función con los valores obtenidos, tiene funciones predeterminadas las cuales
#   podemos usar y aplicar en nuestros datos como 'sum' y 'count'
pt = pd.pivot_table(df4, index='Nombre', columns = 'Fecha', aggfunc=['sum', 'count'])
print(pt)
#   appEnd