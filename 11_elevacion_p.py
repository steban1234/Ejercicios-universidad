'''Elevacion del punto (p)''' 

# Marlon Steban Romero Perez _20202131029


#Solicitar los datos de campo al usuario:

ca = float(input('Digite cota del punto A:'))
cb = float(input('Digite cota del punto B:'))
hia = float(input('Digite altura instrumental del punto A:'))
hib = float(input('Digite altura instrumental del punto B:'))
dab = float(input('Digite distancia del punto A al punto B:'))
angha = float(input('Digite angulo horizontal en gggmmss medido de A a I:'))
anghb = float(input('Digite angulo horizontal en gggmmss medido de B a I:'))
angva = float(input('Digite angulo vertical en gggmmss medido de A a P:'))
angvb = float(input('Digite angulo vertical en gggmmss medido de B a p:'))

import math #libreria de matematicas


# Pasaremos gggmmss a decimal y luego a radian todos los angulos digitados:

"""Para el angulo horizontal A"""
angulo = int(angha)  # Convierto el valor ingresado a un entero

angulo = angulo / 10000 # Pongo el punto decimal para separar los grados

grados = int(angulo)
aux = (angulo - grados) * 100 # Guardo en una variable los minutos como entero y los segundos como la parte decimal

minutos = int(aux)
segundos = (aux - minutos) * 100

angulo_decimal = grados + minutos/60 + segundos/3600

angulo_radianes1 = math.radians(angulo_decimal)

""""""""""""""""""

"""Para el angulo horizontal b"""
angulo = int(anghb)  # Convierto el valor ingresado a un entero

angulo = angulo / 10000 # Pongo el punto decimal para separar los grados

grados = int(angulo)
aux = (angulo - grados) * 100 # Guardo en una variable los minutos como entero y los segundos como la parte decimal

minutos = int(aux)
segundos = (aux - minutos) * 100

angulo_decimal = grados + minutos/60 + segundos/3600

angulo_radianes2 = math.radians(angulo_decimal)

""""""""""""""""""

"""Para el angulo vertical a"""
angulo = int(angva)  # Convierto el valor ingresado a un entero

angulo = angulo / 10000 # Pongo el punto decimal para separar los grados

grados = int(angulo)
aux = (angulo - grados) * 100 # Guardo en una variable los minutos como entero y los segundos como la parte decimal

minutos = int(aux)
segundos = (aux - minutos) * 100

angulo_decimal = grados + minutos/60 + segundos/3600

angulo_radianes3 = math.radians(angulo_decimal)

""""""""""""""""""

"""Para el angulo vertical b"""
angulo = int(angvb)  # Convierto el valor ingresado a un entero

angulo = angulo / 10000 # Pongo el punto decimal para separar los grados

grados = int(angulo)
aux = (angulo - grados) * 100 # Guardo en una variable los minutos como entero y los segundos como la parte decimal

minutos = int(aux)
segundos = (aux - minutos) * 100

angulo_decimal = grados + minutos/60 + segundos/3600

angulo_radianes4 = math.radians(angulo_decimal)

""""""""""""""""""
# hallar distancias horizontales de "A a I" "B a I'"

disthAI = ((dab*(math.sin(angulo_radianes2)))) / (math.sin(angulo_radianes1+angulo_radianes2)) 

disthBI = ((dab*(math.sin(angulo_radianes1)))) / (math.sin(angulo_radianes1+angulo_radianes2)) 


# hallar longitud de I a p. a partir del triangulo AIP:

longIPA = disthAI*(math.tan(angulo_radianes3))

# hallar longitud de I a p. a partir del triangulo BIP:

longIPB = disthBI*(math.tan(angulo_radianes4))

# hallamos elevacion para el punto P:

elevP = ((longIPA + ca + hia + longIPB + cb + hib)) / (2)



print()
print( '='*80)
print('la elavacion para el punto P es:' ,elevP)
print( '='*80)
print()


