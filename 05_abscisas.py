'''Programa que calcula las abscisas de un alineamiento segun el intervalo que el usuario digite en pantalla. Al usuario se le solicita tambien la longitud del alineamiento'''

longitud_alineamiento = float(input('cual es la longitud del alineamiento en metros?: '))
intervalo_abscisas = float(input('Digite el intervalo de abscisado en metros: '))

print()
print('*'*80)
print('{:^80}' .format('Abscisas para el alineamiento de '+str(longitud_alineamiento)+' metros '))
print('*'*80)
print()
print('k0+000.000')

distancia = intervalo_abscisas

while longitud_alineamiento >= distancia:
    kilometros = int(distancia // 1000) # Division entera
    abscisa = int(distancia % 1000) # Modulo de la division
    print('K'+str(kilometros)+'+'+'{:07.3f}' .format(abscisa))
    distancia = distancia + intervalo_abscisas

kilometro = int(longitud_alineamiento // 1000)
abscisa = int(longitud_alineamiento) % 1000

print('K'+str(kilometro)+'+'+'{:07.3f}' .format(abscisa))
print()
print('*'*80) 

