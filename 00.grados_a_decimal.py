'''
Programa que convierte grados en forma gggmmss (174°09'30" = 1740930) a decimales.
'''
print()
# Solicito el angulo al usuario
angulo = input('Digite un angulo en gggmmss: ')
angulo = int(angulo)  # Convierto el valor ingresado a un entero

angulo = angulo / 10000 # Pongo el punto decimal para separar los grados

grados = int(angulo)
aux = (angulo - grados) * 100 # Guardo en una variable los minutos como entero y los segundos como la parte decimal

minutos = int(aux)
segundos = (aux - minutos) * 100

angulo_decimal = grados + minutos/60 + segundos/3600

print()
print( '='*80)
print('El angulo {} en decimal es:{}'.format(str(grados)+'°'+str(minutos)+"'"+str(segundos)+'"',angulo_decimal))
print( '='*80)
print()


