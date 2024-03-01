personaje = " 0 "
cajas = " 1 "
metas = " 2 "
paredes = "333"
espacio_piso = "   "
personaje_meta=5
caja_meta=6

posicion_personaje = [2, 2]

print("OCUPA LAS TECLAS A/S/D/W PARA MOVERTE")

mapa = [
    [paredes, paredes, paredes, paredes, paredes],
    [paredes, espacio_piso, espacio_piso, metas, paredes],
    [paredes, espacio_piso, personaje, cajas, paredes],
    [paredes, espacio_piso, espacio_piso, espacio_piso, paredes],
    [paredes, paredes, paredes, paredes, paredes],
]


def imprimir_mapa():
  for fila in mapa:
    print(fila)


def mover_personaje(direccion):
  nueva_posicion = posicion_personaje.copy()
  if direccion == 'w':
    nueva_posicion[0] -= 1
  elif direccion == 's':
    nueva_posicion[0] += 1
  elif direccion == 'a':
    nueva_posicion[1] -= 1
  elif direccion == 'd':
    nueva_posicion[1] += 1

  if 0 <= nueva_posicion[0] < len(mapa) and 0 <= nueva_posicion[1] < len(
      mapa[0]):
    if mapa[nueva_posicion[0]][nueva_posicion[1]] != paredes:
      mapa[posicion_personaje[0]][posicion_personaje[1]] = espacio_piso
      mapa[nueva_posicion[0]][nueva_posicion[1]] = personaje
      posicion_personaje[0], posicion_personaje[1] = nueva_posicion[
          0], nueva_posicion[1]


#
continuar_juego = True
while continuar_juego:
  imprimir_mapa()
  movimiento = input("presiona a donde te vas a mover: ")
  if movimiento.lower() == 'exit':
    continuar_juego = False
  else:
    mover_personaje(movimiento)
