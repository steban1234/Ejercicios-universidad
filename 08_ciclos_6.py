marcas = {'Topcon':'t001', 'Sokia':'s002', 'Trimble':'tr001', 'Leica':'l004', 'South':'st020', 'Nikon':'n001'}

for marca, serial in marcas.items():
    print('La UD cuenta con una estacion {} con serial {} en su laboratorio'.format(marca, serial))
