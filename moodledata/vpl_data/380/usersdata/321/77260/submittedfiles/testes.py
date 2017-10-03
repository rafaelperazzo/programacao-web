# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n= int(input('Número total de eleitores do município: '))
vb= int(input('Número de votos brancos: '))
vn= int(input('Número de votos nulos: '))
vv= int(input('Número de votos válidos: '))

pvb= (100 * vb)/n
pvn= (100 * vn)/n
pvv= (100 * vv)/n

print('Votos brancos=%.f de 1000' % pvb)
print('Votos nulos=%.f de 1000' % pvn)
print('Votos válidos=%.f de 1000' % pvv)

