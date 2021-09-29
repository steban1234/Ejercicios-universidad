# Ejercicio de ciclos

# Ciclo whith ==> mientras

# white CONDICION:
#   Bloque de codigo

# numero = int(input('Por favor digite un entero (0 para terminar): '))

# while numero != 0:
#     print('El numero digitado fue', numero)
#     numero = int(input('Por favor digite un entero (0 para terminar): '))
# else: 
#     print('El programa finalizo por el usuario')

# Palabra = input('Digite cualquier letra: ')

# while Palabra != 'abc' :
#     if Palabra == 'cba' :
#         break
#     print('AAAAAAAAAAAAAA')
#     Palabra = input('Digite cualquier letra: ')
# else:
#     print('fin')

number = 0

# while number <= 255:
#     print('alt + {} = {}' .format(number,chr(number)))
#     number += 1

# for number in range(0, 256, 2):
#     print('alt + {} = {}' .format(number,chr(number)))

# mylist = [1,2,3,4,5,6,7,8,9, 'A','B']
# otralista = []

# for element in mylist:
#     print(element)
#     otralista.append(element)
# print(otralista)

# mydic = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# for key, value in mydic.items():
#     print('La clave {} corresponde al valor {}'.format(key, value))








def number2char(number):
    caracter = chr(number) + ' = ' + str(number)
    return caracter

for numero in range(0,50):
    print(number2char(numero))
