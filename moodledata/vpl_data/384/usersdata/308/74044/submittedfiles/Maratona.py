# -*- coding: utf-8 -*-
n = int(input('Numero de postos: '))
m = float(input('Distancia maxima: '))

i = 1
resultado = 0
limite = -1

while i<=n:
    z = float(input('Posicao: '))
    if z>limite:
        resultado = 1
    i += 1
    limite += z
print(resultado)