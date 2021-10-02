""" # # # def sumatoria_teorica ():
# # #     # solicitar numero de lados de la poligonal y que tipo de angulo observo

# # #     n_lados = float(input('Digite numero de lados de la poligonal:'))
# # #     tipo_angulo = float(input('si son internos(-2), si son externos (+2):'))

# # #     sumatoria_teorica = (n_lados + (tipo_angulo)) * 180 
# # #     return sumatoria_teorica
   


# def acimuthPartida(acimuth, angulo_obs):
    
#     acimuth_final = (acimuth + angulo_obs)

#     if acimuth_final > 360:
#         acimuth_final = (acimuth_final)-360

#     return acimuth_final

# def contraAcimuth(acimuth):

#     if acimuth  > 180:
#        contra_az = (acimuth)-180
#     else:
#         contra_az = (acimuth)+180

#     return contra_az

# acimut = float(input('digite acimut:'))
# angulo_dec_corr = float(input('digite angulo obs corregido:'))


# acimuth_1 = acimuthPartida(acimut, angulo_dec_corr)
# contra_acimuth = contraAcimuth(acimuth_1)

    
    
# print("Acimuth: ", acimuth_1)
# print("Contra acimuth: ", contra_acimuth)




# def calculo_az (acimut_part, angle_obs):

#     acimut_final = (acimut_part + angle_obs )
    

#     if acimut_final > 360:
#         acimut_final = (acimut_final)-360

#     print('acimut final:',acimut_final)

#     if acimut_final  > 180:
#         contra_az = (acimut_final)-180
#     else:
#         contra_az = (acimut_final)+180

#     return contra_az


# acimut_part = float(input('digite acimut:'))
# angle_obs = float(input('digite angulo obs corregido:'))


# acimut_final = calculo_az(acimut_part, angle_obs)
# print("Acimuth final: ", acimut_final)

# acimuth = float(input('digite acimut:'))
# angulo_obs = float(input('digite angulo obs corregido:'))

# def calcular_az(acimuth, angulo_obs):
    
#     if acimuth  >= 180:
#         acimuth = (acimuth - 180) + angulo_obs
#     else:
#         acimuth = (acimuth + 180) + angulo_obs

#     if acimuth  >= 360:
#         acimuth -= 360
#     else:
#         acimuth += 0 

#     return acimuth


# acimuth_ = calcular_az(acimuth, angulo_obs)

# print()
# print('el acimut de la linea es:',acimuth_)


# acimuth = float(input('digite acimut:'))
# angulo_obs = float(input('digite angulo obs corregido:'))

# def calcular_az(acimuth, angulo_obs):
    
#     if acimuth  >= 180:
#         acimuth = (acimuth - 180) + angulo_obs
#     else:
#         acimuth = (acimuth + 180) + angulo_obs

#     if acimuth  >= 360:
#         acimuth -= 360
#     else:
#         acimuth += 0 

#     return acimuth


# acimuth_ = calcular_az(acimuth, angulo_obs)

# if acimuth_ >= 180:
#     acimuth_ = (acimuth_ - 180)
# else:
#     acimuth_ = (acimuth_ + 180)

def sumar_lista(lista):
    suma un conjunto de valores en una lista
   
    suma = 0

    for numero in lista:
        suma += numero

    return suma

#Prueba para lista acimut:

def contraAcimuth(acimuth):
    
    if acimuth  > 180:
       contra_az = (acimuth)-180
    else:
        contra_az = (acimuth)+180

    return contra_az

Contracimut = [181.0912904, 253.7577719, 327.0564756, 49.16490156, 101.4247164, 120.4703645]

Acimut =[]

for c_az in Contracimut:
    Acimut.append(contraAcimuth(c_az))

print()
print('Los Acimut son: ' ,Acimut)

# Prueba de proyecciones:


from itertools import zip_longest
import math

Distancias = [79.816, 69.568, 80.591, 67.308, 62.461]
Acimut = [1.091290449, 73.75777193, 147.0564756, 229.1649016, 281.4247164, 300.4703645]


sum_Dist = sumar_lista(Distancias)
print()
print('sumatoria de distancia: ',sum_Dist)

proy_N = [(x * (math.cos(math.radians(y)))) for x, y in zip_longest(Distancias, Acimut,  fillvalue=0)]

proy_E = [(x * (math.sin(math.radians(y)))) for x, y in zip_longest(Distancias, Acimut,  fillvalue=0)]

suma_proyN = sumar_lista(proy_N)
suma_proyE = sumar_lista(proy_E)

print()
print('Las proyecciones Norte son: ' ,proy_N)
print()
print('Las proyecciones Este son: ' ,proy_E)
print()
print('La suma de las Proyecciones N es : ' ,suma_proyN)
print()
print('La suma de las Proyecciones E es : ' ,suma_proyE)


# Prueba de correciones de proyecciones

corr_proyN =[]

for dist in Distancias:
    corr_proyN.append((- suma_proyN) / sum_Dist * dist)

suma_corr_proyN = sumar_lista(corr_proyN)

print()
print(corr_proyN)
print()
print(suma_corr_proyN)

corr_proyE =[]

for dista in Distancias:
    corr_proyE.append((- suma_proyE) / sum_Dist * dista)

suma_corr_proyE = sumar_lista(corr_proyE)

print()
print(corr_proyE)
print()
print(suma_corr_proyE)


#Proyecciones ya corregidas:

proy_Ncorr = [(x + y) for x, y in zip_longest(proy_N, corr_proyN,  fillvalue=0)]

proy_Ecorr = [(x + y) for x, y in zip_longest(proy_E, corr_proyE,  fillvalue=0)]

suma_proyNcorr = sumar_lista(proy_Ncorr)
suma_proyEcorr = sumar_lista(proy_Ecorr)

print()
print('Las proyecciones corr Norte son: ' ,proy_Ncorr)
print()
print('La suma de las Proyecciones corr N es : ' ,suma_proyNcorr)
print()
print('Las proyecciones corr Este son: ' ,proy_Ecorr)
print()
print('La suma de las Proyecciones corr E es : ' ,suma_proyEcorr)


#coordenadas finales

coordenada_N_ini = 100107.980

coor_N1 = (coordenada_N_ini + proy_Ncorr[0])

print()
print("coordenada n1: %.3f" %coor_N1) """
import pandas as pd
from tkinter import filedialog
import xlsxwriter
from xlsxwriter import workbook
from xlsxwriter import worksheet



""" 
input_path = filedialog.askopenfile(
        title="Importar archivo",
        filetypes=(("Archivos de excel", "*.xlsx"), ("Todo los archivos", "*.*"))
    )
traverse_date = pd.read_excel(input_path.name) """

""" def crear_archivo(nombre_archivo, tipo_archivo):

    workbook = xlsxwriter.Workbook('./' + nombre_archivo + tipo_archivo)
    worksheet = workbook.add_worksheet("Ajuste poligonal")
    
    workbook.close()

    data = {
            'estaciones': [3455, 3453, 345],
            'angulos':  [3455, 3453, 345],
            'distancias':  [3455, 3453, 345],  
            'angulos_decimales':  [3455, 3453, 345],
            'angulos_decimales_corregidos':  [3455, 3453, 345],
            'acimut':  [3455, 3453, 345],
            'proyecciones_N/S': [3455, 3453, 345],
            'proyecciones_E/W': [3455, 3453, 345],
            'correcciones_de_proyeccion N': [3455, 3453, 345],
            'correcciones_de_proyeccion S': [3455, 3453, 345],
            'proyecciones_N/S_corregida': [3455, 3453, 345],
            'proyecciones_E/W_corregida': [3455, 3453, 345],
            'coordenadas_N': [3455, 3453, 345],
            'coordenadas_E': [3455, 3453, 345],
        }
    
 """


#crear_archivo("adrian", ".xlsx")

""" data = {'Product': ['Desktop Computer','Printer','Tablet','Monitor'],
        'Price': [1200,150,300,450]
        }

df = pd.DataFrame(data, columns = ['Product', 'Price'])

df.to_excel (input_path.name, index = False, header=True) """