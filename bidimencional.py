mapa = [[3,3,3,3,3], [3,4,4,4,3], [3,4,0,4,3,], [3,4,4,3,3],[3,4,3,4,3],[3,4,4,4,3], [3,3,3,3,3]] 
posicion_columna = 2
posicion_fila = 2
while True:
    for fila in mapa:
        print(fila)

    movimiento = input("seleccione movimiento:")

    if movimiento == "d":
        if mapa[posicion_fila][posicion_columna] == 0 and mapa[posicion_fila][posicion_columna + 1] == 4:
            mapa[posicion_fila][posicion_columna] = 4
            mapa[posicion_fila][posicion_columna + 1] = 0
            posicion_columna += 1

    if movimiento == "a":
        if mapa[posicion_fila][posicion_columna] == 0 and mapa[posicion_fila][posicion_columna - 1] == 4:
            mapa[posicion_fila][posicion_columna] = 4
            mapa[posicion_fila][posicion_columna - 1] = 0
            posicion_columna -= 1

    if movimiento == "s":
        if mapa[posicion_fila][posicion_columna] == 0 and mapa[posicion_fila + 1][posicion_columna] == 4:
            mapa[posicion_fila][posicion_columna] = 4
            mapa[posicion_fila + 1][posicion_columna] = 0
            posicion_fila += 1

    if movimiento == "w":
        if mapa[posicion_fila][posicion_columna] == 0 and mapa[posicion_fila - 1][posicion_columna] == 4:
            mapa[posicion_fila][posicion_columna] = 4
            mapa[posicion_fila - 1][posicion_columna] = 0
            posicion_fila -= 1
