# -*- coding: utf-8 -*-
n = int(input('Numero de postos: '))
m = float(input('Distancia maxima: '))

i = 1
resultado = 0
limite = 0
z = 0

while i<=n:
    limite += z
    z = float(input('Posicao: '))
    print('entrou')
    if not(z>limite):
        print('entrou1')
            resultado = 1
    i += 1
print(resultado)