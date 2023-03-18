/*
 * Importaciones 
 */
import java.util.Scanner;
/**
 * Ejercicio 1:     Implemente un algoritmo que dado un
                    nombre en una variable de tipo cadena,
                    imprima un saludo en consola.
 */
public class Ejercicio1 {
    
/**
 * Documentación del método Principal
 * @param args parámetros de entrada del método
 * @throws Exception arroja error
 */    
    public static void main(String[] args) throws Exception {
        
        var sc = new Scanner(System.in);                        // variable de almacenamiento de la entrada de texto recogido de la terminal                        
        System.out.println("Por favor ingrese su Nombre");   // mensaje de inicio que da inicio añ algoritmo   
        var nombre = sc.nextLine();                            // captura unicamente el texto introducido por el usuario
        System.out.println("!hola " + nombre + "¡");           // mensaje de respuesta que incluye el texto del usuario
    }
}
