num = int(input("Ingrese un número: "))

i = 1  # Fila actual que es el mismo número que el número de columnas que tiene que tener esa fila
y = 1  # Número que hay que imprimir
j = 1  # número de columnas que hay en la fila
frase = ""

for i in range(1, num + 1):
    y = 1
    for j in range(1, i + 1):  # z recorre de 1 hasta x. Ejemplo en la 4 (x=4 z=1,2,3,4)
        frase += ((" ") + (str(y)))
        y = (y + 2)
    invertida = frase[::-1]
    # print(frase)
    print(invertida)
    frase = ""