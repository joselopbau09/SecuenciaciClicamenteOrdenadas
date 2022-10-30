# José Luis López Bautista

El lenguaje de programación: 
- Python3

## Ejecución
Para ejecutar el programa se necesita:
- Python 3

Se descomprime el archivo de tipo ".zip" luego:
1. Dirigirse en la terminal a la carpeta src: 
```
JoseLuisLopez\src$
```
2. Ejecutar el comando 
```
Python3 main.py
```
- Se ingresa el tamaño del ejemplar, para este caso el valor minimos será uno.

## Justificación
Tenemos que lo primero que se realizó fue la creación de la secuencia, para ello creamos la clase GeneradorSecuencia, está 
recibirá la cantidad de elemento que tiene la secuencia, y de forma pseudoaleatoria selecciona la cantidad de elementos pedidos 
en el rango de [1,100], estos se almacenan en una arreglo y antes de alamcenar alguno se verifica que estos no se repitan, una 
vez que se obtienen todos lo elementos hacemos uso del algoritmo de mergesort para mostrar en consola la secuencia ordenada. 
Para la creación de la secuencia cíclicamente ordenada se nos solicita que el índice del menor elemento sea selecciona de forma 
aleatoria, por lo que se elige un número de forma pseudoaleatoria en el rango de cero al último índice del arreglo que almacena 
la secuencia, una vez que se obtiene lo que hacemos es recorrer los elemento mediante un ciclo una posición, como el arreglo 
está ordenado entonces se realiza esto i-veces con i el número que se obtuvo de forma pseudoaleatoria.
Se creó la clase Buscador la cual recibe la secuencia cíclicamente ordenada y también contará las operaciones que realiza el 
algoritmo visto en clase, además tiene como métodos la implementación del algoritmo para esto se siguio el algoritmo y no se 
hizo uso de algo distinto o algo importante de mecionar. Por último lo que se hace es crear la clase main la cual lleva a cabo 
la interacción mediante la terminal y crea los ejemplares de las clases.