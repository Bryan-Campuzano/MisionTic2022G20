/*
 * importaciones
 */
import java.util.Scanner;
/**
 * Ejercicio 2:     Implemente un algoritmo que reciba un número por
                    teclado y cuente cuántas cifras (o dígitos) contiene e
                    imprima el mensaje en consola.
 */
public class Ejercicio2 {

    /**
     * Método123 Constructor de la clase
     * @param args parámetros de entrada del método
     * @throws Exception arroja error
     */
    public static void main(String[] args)throws Exception{

        String msg = "La cantidad de Cifras del numero dado es: ";
        var scan = new Scanner(System.in);
        System.out.println("Introduzca un Numero Entero:");
        var numero = scan.nextLine();
        System.out.println(msg + numero.length());
        
    }
}
