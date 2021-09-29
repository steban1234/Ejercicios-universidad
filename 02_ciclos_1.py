# Programa que solicite los datos de una poligonal e imprima el numero de deltas

# x_referencia = float(input('Digite la coordenada Este del punto de referencia: '))
# y_referencia = float(input('Digite la coordenada Norte del punto de referencia: '))
# x_armada = float(input('Digite la coordenada Este del punto de referencia: '))
# x_armada = float(input('Digite la coordenada Norte del punto de referencia: '))

deltas = []
angulos = []
distancias = []
total_deltas = 0
delta_final = ''

delta = input('Digite el nombre del primer delta: ')
deltas.append(delta)

while delta != delta_final:
    delta_final = input('Digite el nombre del delta: ')
    deltas.append(delta_final)

print('El valor de total_deltas original es: ', deltas)
total_deltas = len(deltas) - 1

print('El numero de deltas de la poligonal es de', total_deltas)