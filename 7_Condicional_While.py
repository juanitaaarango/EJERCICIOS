"""06-09-2022

---------------CICLO WHILE ------------
Evalua la condición tantas veces hasta la sentencia sea falsa

Tiene similitud con la sentencia if. Sin embargo, 
la condición puede cambiar.

Si la condición es verdadera, se ejecutan todas las sentencias
que contenga el ciclo while.
Si la condición es falsa, no se ejecutan las sentencias contenidas

--------------
if condicion:
    <sentencia>
----------------

----------------
while <condicion>:
    <sentencia1>
    <sentencia2>
    <sentencia3>
    .....
----------------


----------------
while <condicion>:
    <sentencia1>
    <sentencia2>
    <sentencia3>
else:
    <Sentencias del else>
----------------"""


"""
Desarrolle un ciclo while infinito
"""
# condicion = True
# 
# while condicion:
#     print("ciclo ejecutado")

"""Cómo protegernos de un ciclo infinito"""

condicion = True
contador = 0
while condicion:
     print("ciclo ejecutado {}".format(contador))
     contador = contador + 1
     if contador == 100: 
        break

"""
Realice un ciclo while con un numero secreto. Cada vez que se ejecuta
un ciclo, el programa pide adivinar el numero, en caso de no ser acertado
se debe mostrar un mensaje diciendo: "Estás atrapado". Y en caso contrario
terminar el ciclo y avisar que el numero es correcto.
"""
#numero_secreto = 999
#numero_usuario = int(input("Ingrese el número secreto: "))
#condicion = (numero_secreto != numero_usuario)
#
#while condicion:
#    print("No es el número correcto")

"""
Realice un ciclo while que imprima los números del 10 al 100, separados por guion(-)
sin salto de linea
10 - 11 - 12 - 13 - ... 100
"""

"Imprima los números del 28 al 50 utilizando el while"

contador2 = 20
while True:
    print(contador2)
    contador2 = contador2 + 1
    if contador2 > 50:
        break






        