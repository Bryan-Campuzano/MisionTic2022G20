""" realizar un programa que que lea el código numérico de un producto como llave de un 
    diccionario y en dicha llave va a almacenar nombre, precio y cantidad 
    del producto en una lista
    
    el programa debe permitir cargar datos al diccionario, debe mostrar 
    un listado completo del diccionario y debe permitir consultar un producto 
    por su llave
    
    CRUD Create, Read, Update, Delete
"""
""" esta funcion crea un producto con ciertas características recibiendo un codigo como entrada

    Parámetros: codigo (int): numérico que identifica el producto 
                descripcion (str): alfanumérico que indica la descripcion del producto 
                precio (int): precio del producto
                cantidad (int): cantidad de unidades del producto
    retorna:    productos (Dict): diccionario con el listados de productos de la forma: [descripcion, precio, cantidad]
"""
def crear(productos):                                               
    codigo = int(input('Digite el código del producto\n'))                  # solicita los datos del producto para crearlo, estos datos son el codigo del producto 
    descripcion = input('Digite el nombre del producto\n')                  # su descripcion, en este caso, este valor funciona como nombre
    precio = int(input('Digite el precio unitario del producto\n'))         # el precio unitario del producto
    cantidad = int(input('Digite la cantidad existente del producto\n'))    # la cantidad de unidades del producto
    productos[codigo] = [descripcion, precio, cantidad]                     # crea una lista en la posición "codigo" del diccionario llamado "productos" con los valores introducido por el usuario
    return productos                                                        # actualiza el diccionario pasado como parametro

""" esta funcion imprime en pantalla el diccionario 'productos' ademas de una serie de elementos para una mejor comprensión visual del contenido

    Parámetros: codigo (int): numérico que identifica el producto 
                descripcion (str): alfanumérico que indica la descripcion del producto 
                precio (int): precio del producto
                cantidad (int): cantidad de unidades del producto
    retorna:    listado de productos (str): retorna una cadena de la forma: 'LISTADO DE PRODUCTOS'
                indice (str): retorna una cadena de la forma: 'Codigo        Nombre      precio      cantidad'
                productos (str): retorna una cadena de la forma 'descripcion, precio, cantidad' de todos los productos guardados en el diccionario
"""   
def mostrar(productos):
    print('LISTADO DE PRODUCTOS')
    print('Código\t\tNombre\t\tPrecio\t\tCantidad')
    for i in productos:
        #print(productos[i][0]+'\t\t'+ str(productos[i][1])+'\t\t'+ str(productos[i][2]))   # esta opcion lo único que cambia es la identacion, imprimiendo dos sangrias horizontales entre cada elemento
        print(i,productos[i][0], productos[i][1], productos[i][2], sep="\t\t")              # el elemento "\t" hace parte del la lista de elementos de python llamada "secuencias de escape" 
                                                                                            # caracteres que modelan un comportamiento a la hora de imprimir un elemento en consola
                                                                                            # en este caso, el elemento "\t" representa una sangria horizontal, es un espaciado similar a cuando presionas la tecla "TAB"
""" esta funcion busca un producto concreto dentro del diccionario y lo retorna en forma de cadena de caracteres, si el codigo no existe retorna el mensaje 'Digite el código que desea consultar'                          

    Parámetros: productos(Dict): diccionario con el listado de productos 
                cod (int): codigo de producto indicado por el usuario
    retorna:    producto (str): retorna la informacion del producto cuyo codigo coincide con la busqueda, mensaje de error de lo contrario
"""
def consultar(productos):
    cod = int(input('Digite el código que desea consultar\n'))
    if cod in productos:
        print('Nombre\t\tPrecio\t\tCantidad')
        print(productos[cod][0], productos[cod][1], productos[cod][2], sep="\t\t")          # el comando "sep" establece la separación entre elementos del print
    else:
        print('El código del producto no existe')

""" esta funcion actualiza la informacion un producto concreto dentro del diccionario y retorna un mensaje en forma de cadena de caracteres, si el codigo no existe retorna el mensaje 'El código del producto no existe'                          

    Parámetros: productos(Dict): diccionario con el listado de productos 
                cod1 (int): codigo de producto indicado por el usuario
    retorna:    mensaje (str): retorna un mensaje de 'Producto actualizado', mensaje de error de lo contrario
"""        
def actualizar(productos):
    cod1 = int(input('Digite el código del producto que desea actualizar\n'))
    if cod1 in productos:
        precio = int(input('Digite el precio unitario del producto\n'))
        cantidad = int(input('Digite la cantidad existente del producto\n'))
        productos[cod1][1] = precio
        productos[cod1][2] = cantidad
        print('Producto actualizado')
    else:   
        print('El código del producto no existe') 
       
""" esta funcion borra la informacion un producto concreto dentro del diccionario y retorna un mensaje en forma de cadena de caracteres, si el codigo no existe retorna el mensaje 'El código del producto no existe'                          

    Parámetros: productos(Dict): diccionario con el listado de productos 
                cod2 (int): codigo de producto indicado por el usuario
    retorna:    mensaje (str): retorna un mensaje de 'Producto eliminado', mensaje de error de lo contrario
"""
def borrar(productos):
    cod2 = int(input('Digite el código del producto que desea borrar\n'))
    if cod2 in productos:
        productos.pop(cod2)
        print('Producto eliminado')
    else:
        print('El código del producto no existe') 
        

continuar = 's'                 # valor inicial que desencadena el menu
productos = {                   # lista preliminar de productos
    1:['manzana', 2500, 80],
    2:['pera', 3000, 90],
    3:['banana', 500, 1500]
}

""" funcion que modela un menu de selección multiple con 5 opciones definidas en el CRUD
"""
while continuar == 's' or continuar == 'S':                             # esta condición modela la opcion de continuar, contempla ambos casos del carácter "s" ya sea en mayúscula o minúscula
    print('MENU')                                                       # los siguientes print modelan el menu que va a recibir el usuario en la consola
    print('1. Crear producto')
    print('2. Mostrar productos')
    print('3. Consultar producto ')
    print('4. Actualizar el producto')
    print('5. Borrar producto')
    opcion = int(input('Digite una opción del menú [1,2,3,4,5]:\n'))    # se le pide al usuario la opcion a realizar
    if opcion == 1:                                                     # dependiendo del valor introducido, realiza un proceso modelado con anterioridad
        crear(productos)
        print(f'El producto ha sido creado con éxito')
        # print(productos)
    elif opcion == 2:
        mostrar(productos)
    elif opcion == 3:
        consultar(productos)
    elif opcion == 4:
        actualizar(productos)
    elif opcion == 5:
        borrar(productos)
    else:
        print('Digite una opción válida (1, 2 o 3)')
    continuar = input('Digite "s" para continuar o cualquier letra para salir\n')   # te retorna al menu principal por si se requiere realizar otra accion 

#   appEnd