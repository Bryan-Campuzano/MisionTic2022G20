/**
 * CICLO 2: PROGRAMACIÓN BÁSICA EN JAVA
 * como venimos de una primera experiencia de programación usando el lenguaje de programación PYTHON, el aprender Java
 * no va a ser tan difícil como una primera experiencia, pues ya tenemos una experiencia asi sea minima en el proceso de programación 
 * no obstante, Java es un lenguaje sustancialmente diferente a python, tanto en forma como en fondo, lo cual, veremos a lo largo de este ciclo.
 * para empezar, la creación de proyectos:
 *      aunque  en java también se pueden crear archivos independientes y empezar a hacer codigo, lo mas común en este lenguaje es crear lo que
 *      se conoce como "carpeta de proyecto" o "Java project" una serie de carpetas y recursos que java crea para encapsular de manera organizada 
 *      todos los elementos que se necesitan para el desarrollo de un programa completo e independiente, lo que permite la compartimentalizar mejor 
 *      el flujo de trabajo y el multi-proyecto. el proyecto se compone de carpetas 3 default llamadas '.vscode' 'lib' y 'src' cada una destinada para
 *      una función especifica, aunque siempre se pueden generar 
 *      carpetas o sub-carpetas nuevas:
 * 
 *          carpeta '.vscode': aquí se guardan archivos de configuración tipo 'json' que se encargar de configuraciones y preferencias locales que van 
 *          desde manejo de clases hasta preferencias de terminología en el codigo
 *         
 *          carpeta 'lib': en esta carpeta se incluyen las librerías de uso local del programa, permite configurar de manera local los recursos específicos 
 *          usados en cada proyecto por separado aligerando el peso general de cada proyecto y previniendo incompatibilidades
 *          
 *          carpeta 'src': en esta carpeta se cre   a el documento default '.Java' y se inicia el proceso de creación de codigo, en esta carpeta se tienen 
 *          los archivos de java que usaremos para modelar las clases o partes principales en las que fraccionaremos el programa principal 
 * 
 * los comentarios son parte fundamental del codigo. es un tipo de texto que no se ejecuta al momento de copilar y ejecutar el codigo, sirve para una mejor comprensión del codigo
 * el 'para qué' y el 'por qué' de las cosas. en general se usa para que cuando un programador externo o para recordar el funcionamiento del programa después, por si se
 * requiere añadir actualizaciones o correcciones: 
 *      existen varias formas de comentar en java, este comentario largo esta hecho en una convención llamada 'comentario de documentación' pero existen mas tipos 
 *      de comentarios:
 * 
 *          comentario de documentación: es del tipo "/**" para abrir el comentario y "* /" (sin el espacio intermedio) para cerrar, este tipo de comentario sirve para 
 *          la generación de 'documentación' esto es un archivo de texto externo que copila y documenta todos los comentarios de este tipo para poder analizar el funcionamiento
 *          del codigo, los comentarios del desarrollador y su explicación de como funciona cada fragmento del codigo sin necesidad de recorrerlo en su totalidad. 
 *          la documentación es de las partes mas importantes del desarrollo porque solventa dudas, y permite la solución de errores y la implementación de actualizaciones  
 *      
 *          comentario de bloque: es del tipo "/*" para abrir el comentario y "* /" (sin el espacio intermedio) para cerrar, este tipo de comentario sirve para hacer anotaciones
 *          dentro del codigo o en los métodos pero que no hacen parte de la documentación, ya que esta es un documento mas formal del funcionamiento y los comentarios sueltos sirven 
 *          mas como pautas internas de la empresa o notas puntuales personales, o comentarios de acceso exclusivo del programador
 *      
 *          comentario de linea: es del tipo "//" y no se cierra, sirve para comentar una linea, para especificaciones concretas dentro del codigo, comentarios muy específicos de funcionamiento
 *          entre lineas. se le conoce como comentario de linea porque unicamente comprende el texto sobre la misma linea en el que se declara 
 */

/**
 *  esto es un comentario de documentación
 */

/*
 *  esto es un comentario de bloque
 */

//  esto es un comentario de linea

/**
 *  las clases en java, asi como en python representan aspectos fundamentales del programa, si por ejemplo, si en el programa se requiere modelar un cliente, con informacion personal, o 
 *  funciones especificas, se crean una clase especial para ello, esto obedece al paradigma de programación ya que se usan estas clases para modelar valores y métodos propios de cada objeto
 *  lo que permite la separación y la posterior asociación con otros objetos del programa
 *      em java los nombres de las clases se establecen con un orden de términos especifico, a esta acción la llamamos "declarar":
 * 
 *          visibilidad: puede ser publica o privada. en este caso que sea publica nos dice que todo lo que contiene esta clase, valores, constantes, métodos y atributos son visibles y accesibles desde
 *          otras clases o partes del proyecto, el privado oculta la visibilidad del elemento en cuestión de otras clases o partes del programa. por ejemplo, un método o atributo puede ser privado y
 *          unicamente accesible dentro de la clase a la que pertenece
 * 
 *          tipo: existen varios tipos de datos, métodos y objetos que contienen determinados métodos y valores predeterminados, estos son llamados "clases discretas" o "clases primitivas". clases propias 
 *          de java y que modelan el comportamiento del elemento o "instancia" que se genera. la clase "class" modela un tipo de objeto con atributos, métodos y demás elementos que específicos
 *          podemos entender los tipos y las instancias como un molde de galleta y una galleta respectivamente, el tipo define los limites y el como funciona, asi como un molde de galletas. y la instancia es
 *          una galleta en especifico, con forma, sabor textura y en general, atributos únicos a ella. 
 *          
 *          nombre: el nombre tiene una sintaxis especifica para las clases y es que tiene que tener la primera letra en mayúscula, si el nombre es compuesto por varias palabras, cada nueva palabra también 
 *          inicia en mayúscula, y no se pueden tener espacios, ejemplo: "ClientePrivado" la 'p' en privado va en mayúscula
 * 
 *          corchetes: los corchetes, asi como la identacion en python, sirve para ayudar a la legibilidad del codigo, su organización y jerarquía, en este caso se escriben un par de corchetes después de la declaración
 *          de la clase y todo el codigo escrito dentro de este par de corchetes, pertenece a la clase. ademas de pasar a una jerarquía inferior, el funcionamiento de los métodos es similar, esto se hace porque java no
 *          los espacios como caracteres que se pueden copilar, por lo que la identacion aunque puede servir para la legibilidad del codigo, no es necesario para la lógica
 */
public class App {
    public static void main(String[] args) throws Exception {
        //  lo siguiente se conoce como sentencia, las sentencias son ordenes que se le indican al sistema y modelan el codigo en su nivel mas bajo, en java cada sentencia se finaliza con un punto y coma ";"
        //  declaraciones de variables, constantes, ordenes y demás se tienen un punto y coma dandi fin a la instrucción
        //  para poder solicitar métodos o atributos de una clase en especial se escribe el nombre de la clase seguida por un punto y el nombre del método, en este caso
        //  tenemos la clase System, sub-clase out, método println
        
        System.out.println("Hello, World!");    // esta instrucción imprime el mensaje "Hello World!" en consola
        
        //  las variables son un tipo de almacén de datos, en el cual podemos asignar un tipo de dato especifico con el cual podemos operar
        //  su contenido puede cambiar mediante operaciones o resultados de métodos, por esto su contenido es "variable"
        //  para declarar una variable: tipoVariable nombreVariable = valorVariable;

        int x = 0;  //cuando una variable no es usada se marca como una falla, hay varios tipos de de errores en java, en este caso es una falla que no impide la ejecución del codigo pero resaltan para tener un codigo mas limpio

        //  existen varios tipos de variables, como enteros (int) decimales (double, float o long) o alfa-numéricos (string o char) cuando se define el tipo de variable en un elemento
        //  al momento de variar el valor unicamente se puede almacenar un valor del mismo tipo, excepto en el caso del tipo 'var' en la cual puede almacenarse un numero y después una letra
    
        var variable = 5.5;     //  ene ste caso java infiere el tipo de variable
        String nombre = "Juan";

        System.out.println(nombre.getClass().getSimpleName());
        
        //  System.out.println(x.getClass().getSimpleName());   este métodos no es factible pues las clases primitivas no tienen métodos tan complejos,por lo que esto arroja un error que impide la ejecución 
        //  estos errores son conocido como errores lógicos, errores de mala implementación, uso o sencillamente sintaxis que no tiene sentido en este lenguaje

        
    }
}
