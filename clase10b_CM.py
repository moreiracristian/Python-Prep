import sys

if len(sys.argv) == 2:
    import datetime
    import os
    marca_de_tiempo = datetime.datetime.now()
    marca_de_tiempo = int(datetime.datetime.timestamp(marca_de_tiempo))

    lluvia = sys.argv[1]
    temperatura = input('Ingrese la temperatura actual en grados centígrados')
    humedad = input('Ingrese el porcentaje de humedad actual')
    linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

    logs_lluvia = open('clase09_ej2.csv', 'a')
    logs_lluvia.write(linea+'\n')
    logs_lluvia.close()
else:
    print('ERROR: No se permite más de 3 argumentos.')
    print('Ejemplo: .py <temperatura> <humedad> <True o False>')