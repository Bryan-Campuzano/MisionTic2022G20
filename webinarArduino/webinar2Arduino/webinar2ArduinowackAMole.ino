  //  aquí declaramos las variables globales, aquellas que se usan en todo el codigo
  //  proyecto de wack a mole
  
  int numeroAleatorio;
  
  //  para el desarrollo de este proyecto usaremos los operadores lógicos "and", "or" y "Not" estos operadores
  //  realizan operaciones sobre dos proposiciones booleanas, y retorna un valor booleano de respuesta, para mas info buscar "tabla de verdad and, or y not"
  //  para saber como operan las entradas y salidas de estas operaciones

  //  también usaremos la funcion "random" esta genera números aleatorios dentro de dos limites definidos por el programador
  
  //  configuración de tiempo en milisegundos

void setup() {
  //  codigo de única ejecución, aquellas declaraciones de elementos y demás codigo de única ejecución
  Serial.begin(9600);           // la initialization de los puertos seriales y su configuración se verán en el webinar numero 3
  randomSeed(analogRead(A5));   //semilla 100% aleatoria, pues las otras variables inicializadas generan números aleatorios con patron
  Serial.println("*** Inicio de los Números Aleatorios");
  
  }
void loop() {
  //  codigo cíclico, aquí se escribe el codigo que necesito que se repita varias veces
  numeroAleatorio = random(0,10);     // initialization del numero aleatorio
  Serial.print("Número Random = ");  // mensaje a imprimir en consola
  Serial.println(numeroAleatorio);    // imprime el numero aleatorio generado
  delay(1000);                        // retraso de mil ms entre cada iteración del loop
  }
  //  aquí se codifican todas las funciones
