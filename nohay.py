personaje = "👽"
cajas = "🐄"
metas = "🛸"
paredes = "⬜"
espacio_piso = "  "
personaje_meta = "✌️"
caja_meta = "💀"

historial = []

posicion_personaje = []
posiciones_cajas = []

print("OCUPA LAS TECLAS A/S/D/W PARA MOVERTE")
print("Para ocupar la habilidad especial deberas posicionar la mitad de las cajas")

mapa = [
    [
        paredes, paredes, paredes, paredes, paredes, paredes, paredes, paredes,
        paredes, paredes, paredes, paredes
    ],
    [
        paredes, espacio_piso, espacio_piso, espacio_piso, metas, espacio_piso,
        espacio_piso, paredes, espacio_piso, personaje, espacio_piso,
        paredes
    ],
    [
        paredes, cajas, espacio_piso, espacio_piso, paredes, cajas, espacio_piso,
        espacio_piso, cajas, espacio_piso, espacio_piso, paredes
    ],
    [
        paredes, metas, espacio_piso, espacio_piso, espacio_piso, espacio_piso,
        espacio_piso, espacio_piso, paredes, paredes, paredes, paredes
    ],
    [
        paredes, espacio_piso, espacio_piso, espacio_piso, paredes,
        espacio_piso, espacio_piso, espacio_piso, espacio_piso, espacio_piso,
        metas, paredes
    ],
    [
        paredes, paredes, paredes, paredes, paredes, paredes, paredes, paredes,
        paredes, paredes, paredes, paredes
    ],
]

final =[
    paredes, paredes, paredes, paredes, paredes, paredes, paredes, paredes,
    paredes, paredes, paredes, paredes
],


def contar_numero(lista, numero):
  return lista.count(numero)


def imprimir_mapa():
  for fila in mapa:
    print(''.join(fila))


def contar_cajas():
  return sum(fila.count(cajas) for fila in mapa)


def verificar_ganador():
  return all(cajas not in fila for fila in mapa)


def guardar_estado():
  historial.append({
      "mapa": [fila.copy() for fila in mapa],
      "posicion_personaje": posicion_personaje.copy(),
      "posiciones_cajas": [pos.copy() for pos in posiciones_cajas]
  })


def cargar_estado():
  estado = historial.pop()
  global mapa, posicion_personaje, posiciones_cajas
  mapa = [fila.copy() for fila in estado["mapa"]]
  posicion_personaje = estado["posicion_personaje"].copy()
  posiciones_cajas = [pos.copy() for pos in estado["posiciones_cajas"]]

def encontrar_cajas():
  posiciones_cajas = []
  for i, fila in enumerate(mapa):
    for j, celda in enumerate(fila):
      if celda == cajas or celda == caja_meta:
        posiciones_cajas.append([i, j])
  return posiciones_cajas

def encontrar_personaje():
  for i, fila in enumerate(mapa):
    for j, celda in enumerate(fila):
      if celda == personaje or celda == personaje_meta:
        return [i, j]

def mover_personaje(direccion):
  guardar_estado()
  posicion_personaje = encontrar_personaje()  
  nueva_posicion = posicion_personaje.copy()
  posiciones_cajas = encontrar_cajas()  
  nuevas_posiciones_cajas = [pos.copy() for pos in posiciones_cajas]

  
  if direccion == 'w':
    nueva_posicion[0] -= 1
    for pos in nuevas_posiciones_cajas:
      pos[0] -= 1
  elif direccion == 's':
    nueva_posicion[0] += 1
    for pos in nuevas_posiciones_cajas:
      pos[0] += 1
  elif direccion == 'a':
    nueva_posicion[1] -= 1
    for pos in nuevas_posiciones_cajas:
      pos[1] -= 1
  elif direccion == 'd':
    nueva_posicion[1] += 1
    for pos in nuevas_posiciones_cajas:
      pos[1] += 1
  elif direccion.lower() == 'p':
    if contar_cajas() < (len(posiciones_cajas) / 2):
      for fila in mapa:
        while cajas in fila:
          indice = fila.index(cajas)
          fila[indice] = paredes
      posiciones_cajas.clear()
    else:
      print("Aun no >:v.")


  if 0 <= nueva_posicion[0] < len(mapa) and 0 <= nueva_posicion[1] < len(mapa[0]):
    if mapa[nueva_posicion[0]][nueva_posicion[1]] != paredes:
      for i, (pos_caja, pos_caja_dos) in enumerate(zip(posiciones_cajas, nuevas_posiciones_cajas)):
        if mapa[nueva_posicion[0]][nueva_posicion[1]] == cajas and pos_caja == nueva_posicion:
          if mapa[pos_caja_dos[0]][pos_caja_dos[1]] != paredes and mapa[pos_caja_dos[0]][pos_caja_dos[1]] != cajas and mapa[pos_caja_dos[0]][pos_caja_dos[1]] != caja_meta:
            if mapa[pos_caja_dos[0]][pos_caja_dos[1]] == metas:
              mapa[pos_caja_dos[0]][pos_caja_dos[1]] = caja_meta
            else:
              mapa[pos_caja_dos[0]][pos_caja_dos[1]] = cajas
            posiciones_cajas[i] = pos_caja_dos
          else:
            nueva_posicion = posicion_personaje.copy()
      if mapa[posicion_personaje[0]][posicion_personaje[1]] == personaje_meta:
        mapa[posicion_personaje[0]][posicion_personaje[1]] = metas
      elif mapa[posicion_personaje[0]][posicion_personaje[1]] == caja_meta:
        mapa[posicion_personaje[0]][posicion_personaje[1]] = cajas  
      else:
        mapa[posicion_personaje[0]][posicion_personaje[1]] = espacio_piso
      if mapa[nueva_posicion[0]][nueva_posicion[1]] == metas:
        mapa[nueva_posicion[0]][nueva_posicion[1]] = personaje_meta
      elif mapa[nueva_posicion[0]][nueva_posicion[1]] == caja_meta:
        mapa[nueva_posicion[0]][nueva_posicion[1]] = personaje_meta  
        if direccion == 'w' and (mapa[nueva_posicion[0] - 1][nueva_posicion[1]] == espacio_piso or mapa[nueva_posicion[0] - 1][nueva_posicion[1]] == metas):  
          mapa[nueva_posicion[0] - 1][nueva_posicion[1]] = cajas
        elif direccion == 's' and (mapa[nueva_posicion[0] + 1][nueva_posicion[1]] == espacio_piso or mapa[nueva_posicion[0] + 1][nueva_posicion[1]] == metas):
          mapa[nueva_posicion[0] + 1][nueva_posicion[1]] = cajas
        elif direccion == 'a' and (mapa[nueva_posicion[0]][nueva_posicion[1] - 1] == espacio_piso or mapa[nueva_posicion[0]][nueva_posicion[1] - 1] == metas):
          mapa[nueva_posicion[0]][nueva_posicion[1] - 1] = cajas
        elif direccion == 'd' and (mapa[nueva_posicion[0]][nueva_posicion[1] + 1] == espacio_piso or mapa[nueva_posicion[0]][nueva_posicion[1] + 1] == metas):
          mapa[nueva_posicion[0]][nueva_posicion[1] + 1] = cajas
      else:
        mapa[nueva_posicion[0]][nueva_posicion[1]] = personaje
      posicion_personaje[0], posicion_personaje[1] = nueva_posicion[0], nueva_posicion[1]



continuar_juego = True


while continuar_juego:
  imprimir_mapa()
  print("Número de cajas restantes: ", contar_cajas())
  if verificar_ganador():
    print("¡siguiente nivel.")
    break
  movimiento = input("presiona a donde te vas a mover: ")
  if movimiento.lower() == 'exit':
    continuar_juego = False
  elif movimiento.lower() == 'r':
    cargar_estado()
  else:
    mover_personaje(movimiento)
