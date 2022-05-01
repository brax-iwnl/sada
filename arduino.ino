//Definindo pino dos sensores analogico/Digital
//Sensor 1
int s1_analog = A5;
int s1_digital = 7;
//Sensor 2
int s2_analog = A4;
int s2_digital = 6;
//Sensor 3
int s3_analog = A3;
int s3_digital = 5;
//Criando e inciando variaveis de controle dos sensores
int s1_A0 = 0;
int s1_D = 0;
int s2_A0 = 0;
int s2_D = 0;
int s3_A0 = 0;
int s3_D = 0;
void setup() {
  Serial.begin(2000000); //Velocidade da comincacao serial
  //Definindo o estado incial dos sensores - todos sao entradas(INPUT)
  pinMode(s1_analog, INPUT);
  pinMode(s1_digital, INPUT);
  pinMode(s2_analog, INPUT);
  pinMode(s2_digital, INPUT);
  pinMode(s3_analog, INPUT);
  pinMode(s3_digital, INPUT);
}

void loop() {
  //Lendo os sesnores antes de entrar nas condicionais
  s1_A0 = analogRead(s1_analog);
  s1_D = digitalRead(s1_digital);
  s2_A0 = analogRead(s2_analog);
  s2_D = digitalRead(s2_digital);
  s3_A0 = analogRead(s3_analog);
  s3_D = digitalRead(s3_digital);
  //Envia os dados a serem recebidos em python
  Serial.print((String)s1_A0 + "," + (String)s1_D);
  Serial.print("|" +(String)s2_A0 + "," + (String)s2_D);
  Serial.println("|" +(String)s3_A0 + "," + (String)s3_D);
  delay(100);
}
