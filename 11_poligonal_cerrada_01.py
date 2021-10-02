# Este programa calcula y ajusta una poligonal por los metodos de brujula y transito
import math
from tkinter.constants import S, X, Y
import pandas as pd
import xlsxwriter
import numpy as np
from tkinter import filedialog
from itertools import zip_longest


def angle_to_dec(angulo):
    angulo = angulo / 10000
    grados = int(angulo)
    auxiliar = (angulo - grados) * 100
    minutos = int(auxiliar)
    segundos = (auxiliar - minutos) * 100

    angle_dec = grados + minutos / 60 + segundos / 3600
    return angle_dec
 

def dec_to_angle(angulo_dec):
    grados = int(angulo_dec)
    auxiliar = (angulo_dec - grados) *60
    minutos = int(auxiliar)
    segundos = (auxiliar - minutos) * 60

    angulo = grados + minutos / 60 + segundos / 3600
    return angulo


def azimuth_by_coordinate(x1, y1, x2, y2,):
    dx = x2 - x1
    dy = y2 - y1

    if dy != 0:
        rumbo = math.degrees(math.atan(dx/dy))

        if   dx > 0 and dy > 0:
            azimuth = rumbo
        elif dx > 0 and dy <0:
            azimuth = 180 + rumbo
        elif dx < 0 and dy < 0:
            azimuth = 180 + rumbo
        elif dx < 0 and dy > 0: 
            azimuth = 360 + rumbo
        elif dx == 0 and dy > 0:
            azimuth = 0
        elif dx == 0 and dy < 0:
            azimuth = 180
    else:
        if dx > 0:
             azimuth = 90
        elif dx < 0:
            azimuth = 270
        else:
            print("Error: No se puede calcular el acimut de un punto")
            azimuth = -1

    return azimuth


def sumatoria_teorica (n_lados, tipo_angulo):

    sumatoria_teorica = (n_lados + (tipo_angulo)) * 180 
    return sumatoria_teorica



def sumar_lista(lista):
    """suma un conjunto de valores en una lista
    """
    suma = 0

    for numero in lista:
        suma += numero

    return suma

def acimuthPartida(acimuth, angulo_obs):
    
    acimuth_final = (acimuth + angulo_obs)

    if acimuth_final > 360:
        acimuth_final = (acimuth_final)-360

    return acimuth_final

def contraAcimuth(acimuth):

    if acimuth  > 180:
       contra_az = (acimuth)-180
    else:
        contra_az = (acimuth)+180

    return contra_az

def calcular_caz(acimuth, angulo_obs, lista_caz):
    iterador = 0
    while(iterador < angulo_obs.__len__()):

        if acimuth  >= 180:
            acimuth = (acimuth - 180) + angulo_obs[iterador]
        else:
            acimuth = (acimuth + 180) + angulo_obs[iterador]

        if acimuth  >= 360:
            acimuth -= 360
        else:
            acimuth += 0 

        iterador += 1

        lista_caz.append(acimuth)

    return lista_caz

def calc_proyecciones_E(lista_distancias, lista_acimu):
    proy_E = [(x * (math.sin(math.radians(y)))) for x, y in zip_longest(lista_distancias, lista_acimu,fillvalue=0)]

    return proy_E

def suma_proyE(lista_distancias, lista_acimut):
    proy_E = [(x * (math.sin(math.radians(y)))) for x, y in zip_longest(lista_distancias, lista_acimut,  fillvalue=0)]
    suma_proyE = sumar_lista(proy_E)

    return suma_proyE

def calc_proyecciones_N(lista_distancias, lista_acimu):
    proy_N = [x * (math.cos(math.radians(y))) for x, y in zip_longest(lista_distancias, lista_acimu,fillvalue=0)]
    
    return proy_N 

def suma_proyN(lista_distancias, lista_acimut):
    proy_N = [x * (math.cos(math.radians(y))) for x, y in zip_longest(lista_distancias, lista_acimut,  fillvalue=0)]
    suma_proyN = sumar_lista(proy_N)
    print("Valor de la variable suma_proyN: ", suma_proyN)


    return suma_proyN

def cal_coordenadas(lista_ProyCorreg, lista_resultado, coordenada):
    iterador = 0
    calc = 0
    while(iterador < lista_ProyCorreg.__len__()):
        
        if iterador == 0:
            calc = (coordenada + lista_ProyCorreg[iterador])
        else:

            calc = (calc + lista_ProyCorreg[iterador])

        lista_resultado.append(calc)

        iterador += 1

    return lista_resultado


def traverse():
    # solicitar las coordenadas en pantalla
    x1 = float(input('Digite la coordenada X1: '))
    y1 = float(input('Digite la coordenada y1: '))
    x2 = float(input('Digite la coordenada X2: '))
    y2 = float(input('Digite la coordenada y2: '))


    acimut_linea = azimuth_by_coordinate(x1, y1, x2, y2)

    print()
    print('El acimut de la linea es {} grados decimales'.format(acimut_linea))

    # solicitar numero de lados de la poligonal y que tipo de angulo observo
    n_lados = float(input('Digite numero de lados de la poligonal:'))
    tipo_angulo = float(input('si son angulos internos introduzca -2, si son angulos externos introduzca +2:'))

    sum_teorica = sumatoria_teorica (n_lados, tipo_angulo)

   
    # importando cartera de excel

    #input_path = r"C:\TEC. LEV TOPOGRAFICOS\2DO SEMESTRE\LOGICA PROGRAMACION\poligonal_cerrada.xlsx"
    input_path = filedialog.askopenfile(
        title="Importar archivo",
        filetypes=(("Archivos de excel", "*.xlsx"), ("Todo los archivos", "*.*"))
    )
    traverse_date = pd.read_excel(input_path.name)

    # conviertiendo en lista 
    estaciones = list(traverse_date["STATION"])
    angulos = list(traverse_date["ANGULO"])
    distancias = list(traverse_date["DISTANCIA"])

   

    angulo_dec=[]

    for angulo in angulos:
        angulo_dec.append(angle_to_dec(angulo))

    #sumatoria distancias
    sum_distancias = sumar_lista(distancias)
    
    # Sumatoria real, de los angulos observados en decimal    
    sum_real = sumar_lista(angulo_dec)

    # Error angular
    e_ang = (sum_teorica - sum_real) 

    # correcion angular
    corr_ang = (e_ang / (n_lados + 1))

    # Sumar correcion angular a cada uno de los angulos, en la lista (angulo_dec)
    angulo_dec_corr =[]

    for angulo1 in angulo_dec:
        angulo_dec_corr.append(angulo1 + corr_ang)


    #Calculando acimutes
    Contracimut = []
    Acimut =[]
    calcular_caz(acimut_linea, angulo_dec_corr, Contracimut)
    for c_az in Contracimut:
        Acimut.append(contraAcimuth(c_az))

    #Elegir ajuste: (Brujula o tránsito)
    # metodoCalc = int(input("Método de ajuste: \n1. Brujula\n2.Transito\n"))

    # if(metodoCalc == 1):
    #     print("metodo transito")
    # elif(metodoCalc == 2):
    #     calc_brujula()
    # else:
    #     print("Ingrese una opción válida!")
   

    #Proyecciones
    Proy_NS = calc_proyecciones_N(distancias, Acimut)
    sum_proynorte = sumar_lista(Proy_NS)

    Proy_EW = calc_proyecciones_E(distancias, Acimut)
    sum_proyeste = sumar_lista(Proy_EW)





    #correciones de proyecciones

    corr_proyN =[]

    for dist in distancias:
        corr_proyN.append((- sum_proynorte) / sum_distancias * dist)

    suma_corr_proyN = sumar_lista(corr_proyN)
    

    corr_proyE =[]
    for dist in distancias:
        corr_proyE.append((- sum_proyeste) / sum_distancias * dist)

    suma_corr_proyE = sumar_lista(corr_proyE)

    #Proyecciones ya corregidas:

    Proy_NScorr = [(x + y) for x, y in zip_longest(Proy_NS, corr_proyN,  fillvalue=0)]

    
    Proy_EWcorr = [(x + y) for x, y in zip_longest(Proy_EW, corr_proyE,  fillvalue=0)]

    
    #coordenadas finales

    coordenadas_N = []

    coordenadas_N = cal_coordenadas(Proy_NScorr, coordenadas_N, y1)
    # print("Lista de resultados: ",coordenadas_N)
    # input("stop")
    coordenadas_E = []

    coordenadas_E = cal_coordenadas(Proy_EWcorr, coordenadas_E, x1)



    print()
    print('la sumatoria teorica es',format(sum_teorica))
    print()
    print('la sumatoria real es',format(sum_real))
    print()
    print('el error angular de la poligonal es',format(e_ang))
    print()
    print('la correcion angular de la poligonal es',format(corr_ang))
    print()
    print(estaciones, angulos, distancias, angulo_dec, angulo_dec_corr, Acimut, Proy_NS, Proy_EW, corr_proyN, Proy_NScorr, Proy_EWcorr, coordenadas_N, coordenadas_E)
    print()
    print("la suma de las distancias es: ",sum_distancias)
    print()
    print("la suma de las proyecciones NS es: ",sum_proynorte)
    print()
    print("la suma de las proyecciones EW es: ",sum_proyeste)
    print()
    print("la suma de las correciones proyecciones NS es: ",suma_corr_proyN)
    print()
    print("la suma de las correciones proyecciones EW es: ",suma_corr_proyE)
    



if __name__ == '__main__':
    traverse()
    input("\t\t\n====================================\nPulse cualquier cualquier tecla para salir")


