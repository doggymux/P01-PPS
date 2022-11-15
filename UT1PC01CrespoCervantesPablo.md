# UT1-PC01CrespoCervantesPablo

## Caracteristicas principales Lenguajes de programación

Vamos a ver las diferencias entre 3 lenguajes de programación a traves de los ejercicios realizados en clase.

Ejercicio 1.3
===

En este ejercicio si nos pedia lo siguiente


Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3

Python
---

En python se ha dado la siguente solución a este ejercicio

for i in range (0,10):
    if ( i % 3 ) == 0:
        print(f"{i}")  

como podemos ver en python podemos escribir codigo de forma facil indexando de esta forma podemos establecer que se encuentra dentro del for o del if en nuestro ejercicio.

Despues de una sentencia como puede ser for o if debemos de terminar con : para dar paso a lo que contendra el bucle o el condicional.

Ruby
---

En Ruby la sintaxis de nuestro ejercicio cambiaria.

En ruby cuando queremos aplicar un bucle for dentro de un rango se expresa de la siguiente forma

for i in(0..10)

como podemos ver en este caso la palabra range se sustituye por .. dentro de los parentesis ademas de desaparecer los : finales

en el caso de ruby para imprimir una variable en pantalla se haria de la siguiente forma.

puts "Hola #{name}"

como podemos ver para imprimir en pantalla en vez de print usamos puts y escribimos la variable entre {} con un # delante.

PHP
---
Una de las primeras diferencias que podemos ver en PHP es que para controlar que se encuentra dentro de los bucles o condicionales debemos hacer uso de { } para delimitar que se encuentra dentro de cada cosa.

Ademas para cerrar el contenido de estos debemos de poner ; antes del final.

Los bucles for en PHP varian debido a que no tenemos ninguna palabra reservada que signifique range, es por eso que los bucles debemos de generarlos de la siguiente forma.

for ([ExpresionInicial]; [ExpresiónCondicional]; [ExpresiónIncremental]) {
    sentencias; }

es decir:

for ($i = 0; $i <= 10; $i++){
    sentencias;
}

de esta forma marcamos que $i vale 0 como en el rango que establecimos en el ejercicio y que una vez que compruebe que el valor de i se encuentra entre 0 y 10 sume 1 a este.


JavaScript
---

En JavaScript podemos encontrar las siguientes diferencias en el codigo.

En el bucle for volvemos a encontrarnos con uan sintaxis parecida a la de PHP.

for ([ExpresionInicial]; [ExpresiónCondicional]; [ExpresiónIncremental]) {
    sentencias }

Es decir:

for ($i; $i < 5; $i++){
    sentencias
}
Como podemos observar tendremos que establecer la la expresión con la que empieza nuestro bucle, la condición con la que este terminara y como vamos a incrementar nuestra expresión.

Al igual que en PHP se utilizan llaves para agrupar las diferentes expresiones que utilizaremos dentro de nuestro bucle.

En el caso de los if estos varian debido a que la expresión que estamos usando para la condición debe ir completamente dentro de los parentesis de esta. Ademas estableceremos llaves para marcar donde empieza y acaba las acciones que se realizaran si la condicion es verdadera.

if (condición) {
   sentencia1
}

Ejercicio 2.2
===

En este Ejercicio se nos pedia lo siguiente:

Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

Para realizar este ejercicio en python se ha creado el siguiente codigo:

num1=int(input())
num2=int(input())


def fun(num1,num2):
    if num1 > num2:
       print(f'el numero {num1} es mayor que {num2}' )
    elif(num2==num1):
        print(f'Los numeros son iguales')
    else:
        print(f'El numero {num2} es mayor que el {num1}')
fun(num1,num2)

En python podemos definir funciones usando la palabra reservada def, de esta forma podemos escribir codigo que luego llamaremos escribiendo el nombre de la función y los parametros que esta necesite.

Como podemos ver en el ejercicio las variables podemos generarlas de la siguiente forma:

"nombrevariable"="contenido"

si el contenido que vamos a usar como es el caso es el que nos introduce un usuario a la hora de ejecutar el archivo podemos usar la función input() la cual produce que el usuario tenga que introducir la cedena.

Usando int() antes del input estamos forzando a que la cadena de entrada deba de ser de tipo int.

Por ultimo podemos ver en este ejercicio como al usar la indexación establecemos que se encuentra dentro de cada condicional, vemos como if, elif y else se encuentra al mismo nivel mientras que las sentencias que se ejecutan segun la condición cumplida se encuentran mas indexadas.

Ruby
---

En ruby cuando estamos generando variables con información que le solicitamos a un usuario varia debido a que se usa otro tipo de sintaxis.

En este caso si queremos generar la variable num1 del ejercicio seria de la siguiente forma:

num1 = gets.chomp.to_i

Usando la linea que hemos enseñado estamos pidiendo al usuario que inserte una cadena para cargarla en la variable num1 pero añadiendo al final .to_i hacemos la misma función que int().

En el caso del if, elsif la unica diferencia se encuentra en el modo de establecer el elif ya que en ruby se establece con la palabra reservada elsif

PHP
---

En PHP al tratarse de un lenguaje web podemos cargar variables con información que nos de el usuario a traves de formularios los cuales recogemos tras realizar un submit.

<form action="foo.php" method="post">
    num1:  <input type="number" name="mun1" /><br />
    num2: <input type="number" name="mun2" /><br />
    <input type="submit" name="submit" value="Submit me!" />
</form>

como vemos en el ejemplo anterior se puede enviar la información de las variables que necesitamos a traves de los input, podemos controlar que sean numeros gracias al atributo type.

A la hora de crear los if si que veremos grandes diferencias debido a que como vimos anteriormente los condicionales deberan de llevar las sentencias que se ejecutan en caso de cumplirse entre {} y las condiciones de estas entre (), ademas la forma de establecer un elif en php se llama con elseif. 

if ($a > $b) {
    echo "a es mayor que b";
} elseif ($a == $b) {
    echo "a es igual que b";
} else {
    echo "a es menor que b";
}

JavaScript
---

Para almacenar datos en una variable en JavaScript deberemos de usar como vimos en el ejemplo de PHP un formulario pero ademas deberemos de hacer unas pequeñas modificaciones las cuales veremos ahora.

En los input deberemos de añadir un atributo llamado ID por ejemplo ID="num1" con el nombre que identifica la información que queremos capturar desde JavaScript.

Crearemos una funcion en un archivo .Js en el cual establecemos que y donde se almacena la información.

function returnText(){
    let input = document.getElementById("mun1").value;
    alert(input)
}

Por ultimo para llamar a esta función deberemos de establecer que el botón de submit del formulario llame a la función añadiendo un atributo como este onclick="returnText()"

Las sentencias If, elif se establecen igual que en PHP salvo que en Js elif se llama con else if

Ejercicio 2-13
===

Para este Ejercicio en Python hemos tenido que comprobar cuantas mayusculas tiene una cadena dada por un usuario.


cadenaorigen = input("introduce una cadena para contar las mayusculas: ")

def contarmayusculas(cadenaorigen):
    cadena = cadenaorigen.lower()
    contador = 0
    num = len(cadenaorigen)
    for l in range(0, len(cadenaorigen)):
        print(l)
        if cadena[l:l+1] != cadenaorigen[l:l+1]:
            num = contador + 1
            contador = num
    print(contador)
contarmayusculas(cadenaorigen)

Para realizar el ejercicio hemos usado la funcion lower para crear una cadena con la que comparar la información dada por el usuario, con esto estableceremos todas las letras de la cadena en minusculas.

Una vez establecido las dos variables usando un substring iremos recorriendo la palabra comprobando que las letras sean diferentes en la misma posición, en python para conseguir hacer un substring se realiza de la siguiente forma.

"cadena"["posicióninicio":"posiciónfinal"]

Ruby
---

En ruby para reemplazar las letras mayusculas de una cadena por las minusculas debemos hacerlo de la siguiente forma.

"string".downcase

Una vez tenemos las variables que vamos a comparar deberemos de realizar el substring a las dos cadenas de forma simultanea para ir comparando. En ruby no existe un substring como tal por lo que debemos de trabajar a traves de rangos, el metodo es parecido a python pero varia en el segundo dato que damos en los [].

"cadena"["posicioninicio","longitud"]

Como vemos esta vez especificamos la posición desde la que queremos realizar la extracción de la cadena y la longitud de esta en vez de la posición hasta la que tiene que extraer, es por ello que basandonos en el ejercicio y usando las mismas variables la sentencia quedaria asi.

cadena[l,1]

PHP
---

En PHP para reemplazar las letras mayusculas de una cadena por las minusculas debemos hacerlo de la siguiente forma.

strtolower("cadena");

Como hemos estado viendo al ser una funcion de PHP debera de terminar obligatoriamente en ;

Una vez tenemos en PHP las variables controladas deberemos de comparar las cadenas extrayendo la letra con substring y comparando una con otra. para ello podemos usar la funcion substr() que viene incorporada, la sintaxis es la siguiente:

substr(string $string, int $start, int $length = ?): string

Usando como ejemplo las variables que tenemos actualmente en el ejercicio quedaria de la siguiente forma, utilizando la sintaxis de PHP para llamar a variables.

substr($cadena, l, 1);

al igual que sucede en ruby el segundo valor nos da la longitud de la cadena devuelta por lo que debera de ser 1.

JavaScript
---

En JavaScript para reemplazar las letras mayusculas de una cadena por las minusculas debemos hacerlo de la siguiente forma.

"cadena".toLowerCase()

Deberemos de calcular la longitud de la cadena para poder realizar el bucle, en JavaScript se calcula de la siguiente manera la cual ya podemos cargar en una variable.

var num = cadena.lenght
JavaScript trabaja los substring al igual que python como vemos en la sintaxis siguiente:

substring(indexStart, indexEnd)

Podemos utilizar las variables del ejercicio para substraer la información y comparar ambas cadenas, un ejemplo de substring seria este:

cadena.substring(l, l+1);

Para comparar cadenas en JavaScript podemos utilizar el metodo localeCompare() usando la opcion de case sensitive para detectar cuando comparamos una mayuscula con una minuscula esto nos permitira comprobar las cadenas a traves del bucle.

cadena.localecompare(cadenaorigen, { sensitivity: 'case' })

En este caso nos esta dando positivo cuando ambas letras fueran minusculas por lo que a la hora de generar el if deberemos de añadir 1 al contador cuando la condición sea falsa.

## Comparación entre python y C

Para realizar las comparaciones entre Python y C vamos a elegir los mismos ejercicios que vimos anteriormente.

Ejercicio 1.3
===

En python se ha dado la siguente solución a este ejercicio

for i in range (0,10):
    if ( i % 3 ) == 0:
        print(f"{i}")  

Es por eso que veremos las diferencias de como se hubiera generado este codigo de haberse escrito en C

El primer cambio lo veriamos antes del codigo esto es debido a que al escribir en C deberemos de establecer un main() seguido de corchetes para empezar el codigo

main()
    {
        "codigo"
    }

Para crear el bucle for primero deberemos de definir la variable que utilizaremos en este a diferencia de python que nos permite definirla en el mismo bucle, finalizamos con ;. 

int i;

Tras esto generamos el bucle for, este es parecido a Python ya que deberemos de darle el valor de inicio a la variable, hasta que valor va a estar dentro del bucle y el incremento.

for (i = 1; i <= 10; i++)

{

//Instrucciones a ejecutar "x" número de veces ;

}

Cuando escribamos el if en C deberemos de poner la condicion entre parentesis seguido de {} que contendran las instrucciones que realizara el programa de ser true la condición.

if (Condición) 
{
   "Codigo";
}
 las diferencias como vemos radican en tener que establecer la condición entre parentesis las {} y el uso de ; para finalizar el codigo dentro del if.


Ejercicio 2.2
===

Para empezar a comparar vamos a ver primero de nuevo el codigo del ejercicio en python

num1=int(input())
num2=int(input())


def fun(num1,num2):
    if num1 > num2:
       print(f'el numero {num1} es mayor que {num2}' )
    elif(num2==num1):
        print(f'Los numeros son iguales')
    else:
        print(f'El numero {num2} es mayor que el {num1}')
fun(num1,num2)

En C a la hora de crear funciones debemos de asignar que tipo de resultado nos va a devolver esta y los parametros de entrada.

tipo_del_resultado NOMBRE(tipo_param1 param1, tipo_param2 param2, ... ) 
{
    /* Cuerpo de la función */
}

Todas las funciones de C tienen un return que devuelve un valor este debe de coincidir con el establecido al principio de esta.

Un ejemplo de esto seria el siguiente


int addition(int a, int b) 
{
    return (a + b);
}

Ejercicio 2-13
===

Para empezar a comparar vamos a ver primero de nuevo el codigo del ejercicio en python

def contarmayusculas(cadenaorigen):
    cadena = cadenaorigen.lower()
    contador = 0
    num = len(cadenaorigen)
    for l in range(0, len(cadenaorigen)):
        print(l)
        if cadena[l:l+1] != cadenaorigen[l:l+1]:
            num = contador + 1
            contador = num
    print(contador)
contarmayusculas(cadenaorigen)

Una de las primeras diferencias que encontramos es que en C no tenemos una opción de range para realizar un bucle de forma sencilla es por ello que usando condicionales podemos establecer un bucle while como por ejemplo.

while( n >= 0 && n <= 10 )

Diferencias entre C y python
===

Como hemos estado viendo anteriormente python y C son lenguajes muy diferente.

C es un lenguaje que se utiliza principalmente para crear y desarrollar sistemas operativos, entre los mas famosos escritos en C podemos encontrar Unix.

Por otra parte Python es un tipo de lenguaje que se utiliza especialmente en el desarrollo de aplicaciones web, software y machine learning

A la hora de realizar la lectura del codigo, C necesita pasar por un proceso de compilado para que este codigo sea ejecutable, al utilizar un compilador traducimos un programa en codigo fuente, una vez compilado se le agrega las librerias a traves de un programa llamado linker y se obtiene al fin el ejecutable.

Python por su parte no necesita de un proceso de compilado y el codigo de este es interpretado directamente, estos interpretes son programas que traducen lenguajes de alto nivel y su ejecución se realiza simultaneamente. No se genera un programa objeto con este tipo de lenguaje.

## Analisis de codigo

Vamos a analizar el codigo fuente de los ejercicios, es por eso que comentaremos los elementos que veremos durante los ejercicios.

Palabras reservadas
===

En las palabras reservadas podemos encontrar todas las cadenas que usamos para llamar a funciones internas del lenguaje como serian:

-def
-if
-for
-import
-while
-return
-int

Comandos o instrucciones
===

import --> metodo para importar librerias de python.

Print() --> Función que se utiliza para mostrar por pantalla

lista = [] --> forma de generar una lista en python.

enumerate() --> crea un array bidimensional usando la cadena dada donde podemos establecer la posición de la letra y el valor.

[i:o] --> forma de realizar substring dando valores numericos para establecer las posiciones.

[::-1] --> invertir la cadena.

Identificadores
===

def "funcion" --> forma de definir funciones.

nota = --> forma de crear variables en python


Comparaciones
===

if "variable" "condición" --> forma de generar un condicional, establecemos el nombre de la variable que vamos a utilizar y la condición donde podemos utilizar condicionantes numericos, dentro del condicional if podemos ver elif y else.

Bucles
===

while --> Otro metodo de generar bucles

for "variable" in range() --> Bucle para recorrer un rango numerico. 

"lista".append("variable") --> metodo para anexar la variable que tratamos a un listado.