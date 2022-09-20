cadena = "HolaMundoCruel"
 lista = [1,2, 30, 100, 50, -20]
 tupla = (1,2,3,1,2,3,1,2,3)
 resultados = [1,-1,1,-1,1,-1]
 rango = range(1,100)

for caracter in cadena:
    print(caracter, end="--")

for i in lista:
    print(i, end= "--")

for numero in tupla:
    print(numero, end= "--")

for resultado in resultados:
    print(resultado, end= "--")

for i in rango:
    print(i, end="--")