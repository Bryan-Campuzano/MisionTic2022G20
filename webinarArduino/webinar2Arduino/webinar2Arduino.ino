  //  aquí declaramos las variables globales, aquellas que se usan en todo el codigo
  //  proyecto de luces direccionales
 
  int LED_A =9;
  int LED_B =10;
  int LED_C =11;
  int LED_D =12;
  
  //  configuración de tiempo en milisegundos
  
  int ledTiempo = 100; //tiempo de retardo despues de encendido
  int apagadoTiempo = 400; //tiempo en que todos los led se apagan

  //  pinMode (LED_A,OUTPUT); configuración salida de pin
  //  pinMode (2, INPUT); configuración entrada de pin 
  //  pinMode (Pin_BOTON_2, INPUT_PULLUP); configuración para resistencias pull up internas, en vez de poner una resistencia de salida en config pull up, se hace de manera interna

  //  lectura de pines
  //  digitalWrite (LED_A, HIGH);// HIGH=1 LOW=0
  //  analogWrite (LED_B, 128);  // solo en Pin PWM (0-255)

  //  escritura de punes 
  //  estado_X = digitalRead (2); // HIGH=1 LOW=0 
  //  estado_Y = analogRead (Al); //solo Pin analógico (0-1023)

void setup() {
  //  codigo de única ejecución, aquellas declaraciones de elementos y demás codigo de única ejecución

  pinMode (LED_A,OUTPUT);
  pinMode (LED_B,OUTPUT);
  pinMode (LED_C,OUTPUT);
  pinMode (LED_D,OUTPUT);

}

void loop() {
  //  codigo cíclico, aquí se escribe el codigo que necesito que se repita varias veces
  
  estado_boton = digitalRead(boton2); //  esto es un pin de lectura, detecta señal del de un pin de entrada y la lee, aparte de esto la almacena en una variable
  if(estado_boton == 1){              //  esto es un condicional, el codigo dentro de este solo se desencadena si la condicion dentro de los parentesis es verdadera
  digitalWrite (LED_A,HIGH);          //  para esto se usan los caracteres de comparacion "==" que retornan un booleano como resultado, los otros operadores utiles de conocer son
  delay (ledTiempo);                  //  "!=" diferente de, "<" menor que, ">" mayor que, "<="mayor o igual que, ">=" menor o igual que
  digitalWrite (LED_B,HIGH);
  delay (ledTiempo);
  digitalWrite (LED_C,HIGH);
  delay (ledTiempo);
  digitalWrite (LED_D,HIGH);
  delay (ledTiempo);
  }
  //  Apagado de todos los LEDS
  
  digitalWrite (LED_A,LOW);
  digitalWrite (LED_B,LOW);
  digitalWrite (LED_C,LOW);
  digitalWrite (LED_D,LOW);
  delay (apagadoTiempo);                  
}
  //  aquí se codifican todas las funciones
