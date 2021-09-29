"""
Programa que calcula el acimut de una linea recta a partir de coordenadas cartesianas de sus vertices.
"""

import math # Importo la libreria de matematicas

# Solicita los datos al usuario
x1 = float(input('Digite la coordenada Este del punto 1: '))
y1 = float(input('Digite la coordenada Norte del punto 1: '))
x2 = float(input('Digite la coordenada Este del punto 2: '))
y2 = float(input('Digite la coordenada Norte del punto 2: '))

# Calcular las deltas de coordenadas
dx = x2 - x1
dy = y2 - y1

# Calcular el rumbo y determinar el valor del acimut

if dy != 0:

    # Calcula el rumbo
    rumbo = math.atan(dx/dy)
    rumbo = math.degrees(rumbo)

    # Determinar el valor del acimut

    if dx > 0 and dy > 0:   #Para el primer cuadrante
      acimut = rumbo

    elif dx > 0 and  dy < 0: #Para el 2so cuadrante
      acimut = 180 + rumbo

    elif dx < 0 and dy <0: #Para el 3er cuadrante
      acimut = 180 + rumbo

    elif  dx  > 0 and dy > 0: #Para el 4to cuadrante
      acimut = 360 + rumbo

    elif dx == 0 and dy > 0: #para Y+
      acimut = 0

    elif dx == 0 and dy < 0: #Para el eje Y-
      acimut = 180
else:
    # Cuando Y = 0

    if dx > 0:
      acimut = 90
    elif dx < 0:
      acimut = 270
    else:
      acimut = 'No se puede calcular el acimut de un punto'

print()
print('='*80)
print('El acimut de la linea es:',acimut)
print('='*80)






                        
                
     