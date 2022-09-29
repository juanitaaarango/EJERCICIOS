""" 13-09-2022 


---------------------ITERABLES Y MÉTODOS ------------------

Es importante saber que todo elemento en python es un objeto.
Y que cada objeto posee sus propios métodos (funcionalidades). 

Entre los objetos más comunes que se tienen están: strings, listas y diccionarios.
Cada uno de ellos posee métodos propios para ejecutar alguna funcionalidad. Por ejemplo:

cadena.count("A")             #Cuenta el número de veces que se repite el caracter "A" en la cadena
lista.append(1)               #Agrega el entero 1 a la lista
diccionario.get("cristian")   #Obtiene el elemento del diccionario cuya clave es "cristian"


Veamos algunos de los métodos más importantes:

--------strings---------
formateo:      capitalize(), upper(), lower(), title()
               center(spaces), strip()
operaciones:   count(subcadena),
               find(subcadena)
               replace(old, new)
verificacion:  isalnum(), isalpha(), isdigit, isdecimal, 
Indexado:      [indice]
Slicing:       [indice1:indice2:salto]

---------Listas---------
operaciones: append(value), insert(index, value), 
             pop(index), remove(value),
             count(value)
ordenado:    sort(), reverse()
almacenamiento: clear(), copy()
Indexado: [indice]
Slicing:  [indice1:indice2:salto]


-------Tuplas-----
Operaciones: index(value), count(value)
Indexado: [indice]
Slicing:  [indice1:indice2:salto]


-------diccionarios--------
Extraccion: items(), keys(), values(), get(key)
Eliminar: pop(key)
Almacenamiento: clear(), copy()
Indexado: [key]
 """
""" 
-------------------------------------------
 """
# 29-09-22
# Hay diversas formas de extraer datos de un tipo de variable por ejemplo 
cadena="holamundocruel"
# Puedo extraer los caracteres a partir del indexado la cual usa indices para identificar la posición de cada uno
# Estos indices comienzan desde la posición 0 y se pueden extraer también de derecha a izquierda mediante índices negativos
#Extrae el primer elemento 
print(cadena[0])
print(cadena[-14])
#Extrae elementos de la mitad
print(cadena[3]+cadena[2])
lista=[1,"a",2,3,"b"]
#Metodo inplace (METODO QUE NO DEVUELVE lista.append NADA PERO ESTA AFECTANDO LA LISTA)
lista.append("1000") 

print(lista.pop(1))
lista.insert(2,"Juanita")
lista.insert(5,"Alzate")
print(lista)
#Eliminar los que no puedo sumar 
lista.pop(2)
lista.pop(3)
lista.pop(3) 
lista.pop(-1)
print(sum(lista))

""" for indice in [2,3,3]:
    lista.pop(i) """

