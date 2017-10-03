# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n= int(input('Número total de eleitores do município: '))
vb= int(input('Número de votos brancos: '))
vn= int(input('Número de votos nulos: '))
vv= int(input('Número de votos válidos: '))

pvb= (100 * vb)/n
pvn= (100 * vn)/n
pvv= (100 * vv)/n

print('Percentual de votos brancos=%.f' % pvb)
print('Percentual de votos nulos=%.f' % pvn)
print('Percentual de votos válidos=%.f' % pvv)

