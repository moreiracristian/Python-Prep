import sys

if len(sys.argv) == 4:
    print('El primer parámetro es:', sys.argv[1])
    print('El segundo parámetro es:', sys.argv[2])
    print('El tercer parámetro es:', sys.argv[3])
else:
    print('ERROR: Solo se permite hasta tres (3) argumentos')
    print('Ejemplo: clase10_ejCM.py 1 2 3')
