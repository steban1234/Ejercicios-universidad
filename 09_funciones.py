
def gms2dec(angulo_gms): # El angulo se recibe en gggmmss.sss (1790514.17)
    angulo_gms = angulo_gms / 10000
    grados = int(angulo_gms)
    auxiliar = (angulo_gms - grados) * 100
    minutos = int(auxiliar)
    segundos = (auxiliar - minutos) * 100 

    angulo_decimal = grados + minutos / 60 + segundos / 3600

    return angulo_decimal


def dec2gms(angulo_dec):
    grados = int(angulo_dec)
    auxiliar = (angulo_dec - grados) * 60
    minutos = int(auxiliar)
    segundos = (auxiliar - minutos) * 60

def proyecciones():
    pass





def main():
    print()
    print('{:^100}'.format('Ajuste de poligonal'))
    print()

    angulo = float(input('Digite el angulo observado: '))
    angulo_decimal = gms2dec(angulo)
    
    print('El angulo {} en decimal es {}'.format(str(angulo),str(angulo_decimal)))


if __name__ == '__main__':
    main()

