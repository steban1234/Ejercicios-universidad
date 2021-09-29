# Solicitar al usuario numeros enteros hasta que digite un numero par

es_par = False

while es_par == False:
    numero = int(input('Digite un numero entero: '))
    if numero % 2 == 0:
        es_par = True 
        print('El numero {} es par' .format(numero))
    else:
        continue

