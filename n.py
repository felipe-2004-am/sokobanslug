personaje = " 0 "
cajas = " 📦 "
metas = " 2 "
paredes = "333"
espacio_piso = "   "
personaje_meta = " 3 "
caja_meta = " 🍕 "

posicion_personaje = [2, 2]
posiciones_cajas = [[2, 3], [2, 1]]  # Añade más posiciones de cajas según sea necesario

print("OCUPA LAS TECLAS A/S/D/W PARA MOVERTE")

mapa = [
    [paredes, paredes, paredes, paredes, paredes],
    [paredes, espacio_piso, espacio_piso, metas, paredes],
    [paredes, cajas, personaje, cajas, paredes],
    [paredes, metas, espacio_piso, espacio_piso, paredes],
    [paredes, paredes, paredes, paredes, paredes],
]

def imprimir_mapa():
  for fila in mapa:
    print(''.join(fila))

def verificar_ganador():
  for fila in mapa:
    if cajas in fila:
      return False
  return True

def mover_personaje(direccion):
  nueva_posicion = posicion_personaje.copy()
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

  if 0 <= nueva_posicion[0] < len(mapa) and 0 <= nueva_posicion[1] < len(mapa[0]):
    if mapa[nueva_posicion[0]][nueva_posicion[1]] != paredes:
      for i, (pos_caja, pos_caja_dos) in enumerate(zip(posiciones_cajas, nuevas_posiciones_cajas)):
        if mapa[nueva_posicion[0]][nueva_posicion[1]] == cajas and pos_caja == nueva_posicion:
          if mapa[pos_caja_dos[0]][pos_caja_dos[1]] != paredes:
            if mapa[pos_caja_dos[0]][pos_caja_dos[1]] == metas:
              mapa[pos_caja_dos[0]][pos_caja_dos[1]] = caja_meta
            else:
              mapa[pos_caja_dos[0]][pos_caja_dos[1]] = cajas
            posiciones_cajas[i] = pos_caja_dos
      if mapa[posicion_personaje[0]][posicion_personaje[1]] == metas:
        mapa[posicion_personaje[0]][posicion_personaje[1]] = metas
      else:
        mapa[posicion_personaje[0]][posicion_personaje[1]] = espacio_piso
      if mapa[nueva_posicion[0]][nueva_posicion[1]] == metas:
        mapa[nueva_posicion[0]][nueva_posicion[1]] = personaje_meta
      else:
        mapa[nueva_posicion[0]][nueva_posicion[1]] = personaje
      posicion_personaje[0], posicion_personaje[1] = nueva_posicion[0], nueva_posicion[1]

continuar_juego = True
while continuar_juego:
  imprimir_mapa()
  if verificar_ganador():
    print("¡siguiente nivel.")
    break

  movimiento = input("presiona a donde te vas a mover: ")
  if movimiento.lower() == 'exit':
    continuar_juego = False
  else:
    mover_personaje(movimiento)
