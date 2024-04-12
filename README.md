# sokobanslug
El metal slug mueve cajitas

## 0. Objetivo

Programar el juego Sokoban en una versión retro para consola.

## 1. Reglas del juego

El juego sokoban consiste en acomodar cajas en puntos determinados por las metas.

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja en cualquier sentido.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar totas las cajas sobre las metas.

## 2. Elementos del juego

### 2.0 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando numeros para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

mapa = [
            [3,3,3,3,3],
            [3,4,4,4,3],
            [3,4,0,4,3],
            [3,4,4,4,3],
            [3,3,3,3,3]
        ]

### 2.1 Lista de elementos

- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Pesonaje meta
- 6 - Caja meta

## 3. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover.

- a -> Izquierda
- s -> Derecha
- w -> Arriba
- s -> Abajo

## 4. Función a implementar

| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | Por hacer | - | | - |
| 1. | Repetir el juego hasta terminar el nivel. | LISTO | - | | - |
| 2. | Imprimir mapa.| LISTO | - |
| 3. | Leer el movimiento. | LISTO | - |
| 4. | Evaluar el movimiento del usuario. | LISTO | - |

## Derecha

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | Hecho | [0,4] | [4,0] | - |
| 6. | Personaje, meta  |  Hecho | [0,2] | [4,6] |- |
| 7. | Personaje, caja, pasillo | Hecho | [0,1,4] | [4,0,1] | - |
| 8. | Personaje, caja,  meta |Hecho | [0,1,2] | [4,0,5] | - |
| 9. | Personaje, caja_meta, pasillo | Hecho | [] | [] | - |
| 10. |Personaje, caja_meta, meta | Hecho | [] | [] | - |
| 11. | Personaje_meta, pasillo | Hecho | [] | [] | - |
| 12. | Personaje_meta, meta | Hecho | [] | [] | - |
| 13. | Personaje_meta, caja, pasillo | Hecho | [] | [] | - |
| 14. | Personaje_meta, caja, meta | Hecho | [] | [] | - |
| 15. | Personaje_meta, caja_meta, pasillo | Hecho | [] | [] | - |
| 16. | Personaje_meta, caja_meta, meta | Hecho | [] | [] | - |

## Izquierda

| No. | Función | Kanban | 
| --- | --- | --- | 
| 17. | Personaje y espacio | Hecho | 
| 18. | Personaje y meta | Hecho | 
| 19. | Personaje, caja y espacio | Hecho | 
| 20. | Personaje, caja y meta | Hecho | 
| 21. | Personaje, caja_meta y espacio | Hecho | 
| 22. | Personaje, caja_meta y meta | Hecho | 
| 23. | Personaje_meta y espacio | Hecho | 
| 24. | Personaje_meta y meta | Hecho | 
| 25. | Personaje_meta, caja y espacio | Hecho | 
| 26. | Personaje_meta, caja y meta | Hecho | 
| 27. | Personaje_meta, caja_meta y espacio | Hecho | 
| 28. | Personaje_meta, caja_meta y meta | Hecho | 

## Arriba

| No. | Función | Kanban | 
| --- | --- | --- | 
| 29. | Personaje y espacio | Hecho | 
| 30. | Personaje y meta | Hecho | 
| 31. | Personaje, caja y espacio | Hecho | 
| 32. | Personaje, caja y meta | Hecho | 
| 33. | Personaje, caja_meta y espacio | Hecho | 
| 34. | Personaje, caja_meta y meta | Hecho | 
| 35. | Personaje_meta y espacio | Hecho | 
| 36. | Personaje_meta y meta | Hecho | 
| 37. | Personaje_meta, caja y espacio | Hecho | 
| 38. | Personaje_meta, caja y meta | Hecho | 
| 39. | Personaje_meta, caja_meta y espacio | Hecho | 
| 40. | Personaje_meta, caja_meta y meta | Hecho | 

## Abajo

| No. | Función | Kanban | 
| --- | --- | --- | 
| 41. | Personaje y espacio | Hecho | 
| 42. | Personaje y meta | Hecho | 
| 43. | Personaje, caja y espacio | Hecho | 
| 44. | Personaje, caja y meta | Hecho | 
| 45. | Personaje, caja_meta y espacio | Hecho | 
| 46. | Personaje, caja_meta y meta | Hecho | 
| 47. | Personaje_meta y espacio | Hecho | 
| 48. | Personaje_meta y meta | Hecho | 
| 49. | Personaje_meta, caja y espacio | Hecho | 
| 50. | Personaje_meta, caja y meta | Hecho | 
| 51. | Personaje_meta, caja_meta y espacio | Hecho | 
| 52. | Personaje_meta, caja_meta y meta | Hecho | 

## Determina si se completo el nivel o no

| No. | Función | Kanban | 
| --- | --- | --- | 
| 53. | Evaluar si el nivel esta terminado.  |  Hecho | 
| 54. | Si el nivel esta terminado cargar el siguiente nivel.  | Por hacer | 

## Función extra

| No. | Función | Kanban | 
| --- | --- | --- | 
| 55. | Función adicional o powerup (convierte las cajas en piedra ). | Hecho | 
