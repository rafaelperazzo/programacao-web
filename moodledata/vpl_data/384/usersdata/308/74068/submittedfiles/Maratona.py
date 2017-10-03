# -*- coding: utf-8 -*-
n = int(input('Numero de postos: '))
m = float(input('Distancia maxima: '))

i = 1
resultado = 0
limite = 0
z = 0

while i<=n:
    z = float(input('Posicao: '))
    if (z>limite):
        print('entrou1 %d' %limite)
        resultado = 1
    i += 1
    limite += z
print(resultado)