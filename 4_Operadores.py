# 30 de agosto de 2022
# Juanita Alzate Arango
#Operadores: 
""" Objetivo: Utilizar los distintos operadores, tratar de resolver distintos ejercicios 
mentalmente y posteriormente comprobar los resultados usando el lenguaje y la ejecución 
del código """

""" Operador de asignación: =
Operadores aritméticos: +, -, *,/,//, %, **
Los dos asteriscos funcionan como ^
El % funciona como residuo
El // funciona como la parte entera de la división


Operadores lógicos: or, and, not
Operadores de comparación: <,>,<=,>=, !=

Operadores de conjuntos: | representa la unión 
                         & interseccióname
                         - diferencia """
#EJERCICIOS

#Operadores de asignación

a=1 
b=3
c=5

#Operadores aritméticos
#Realice las siguientes operaciones mentalmente y verifique los resultados en el script

print(3+9)
print(3.0+9)
print(9**.5)
print(2**32)
print(19//2)
print(19%3)
print("hola"+"mundo")
print("hola"*3)
print(["A"] + [1,2,3])
print([]+[])
print((1,2,3)+(1,)) #Tuplas debo poner la coma en el segundo termino

#Operadores lógicos
#Realice las siguientes operaciones 


print(0 and "hola") #Devuelve el falso 
print("" or "hola") #El primero es falso entonces con el or evalua el segundo
print("hola" or "verdadero") #Devuelve Hola
print(1 or 3) #Los dos son verdaderos y estoy usando un or
print(1 and 3) #3
print(True and True)
print(False and True)
print(1 and 1)
print(False or True)
print(True or True)
print(not False)
print(not True) 

print("\n")
#Operadores de comparación 
""" print ("4" > True) """ #Es una operación no permitida

print([] > [1,2,3]) # Una lista es falsa cuando está vacia
print("a" >= "b") #Compara el orden de asignación del alfabeto y evalua
print("Juanita" > "Alzate")
print(1 > 2)  #(Tienen que devolver booleanos, independientemente del tipo de variable)
print(1 < 3   )
print(1 == 1)  # (=) El igual es otro operador
print(2 != 1  )
print(3 >= 3) 
print (5 <= 2)
print(4 > True)
print(True > False)


print("\n")
#Operadores de pertenencia
print("a" in "abshfg")
print("ohla" in "holamundo") #Python verifica el orden por lo tanto es Falso
print("hola" in "holamundo") #Python verifica el orden por lo tanto es Verdadero
print("Hola" not in "holamundo") #Verdadero
print(1 in ["1", "2", "3"]) #Falso un entero no está dentro de una lista de strings
print(1 in [1,2,3]) #Verdadero 



