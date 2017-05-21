# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x=int(input('Total de eleitores:'))
y=int(input('Votos brancos:'))
z=int(input('Votos nulos:'))
w=int(input('Votos válidos:'))
a=(y/x)*100
print('Votos brancos:' '%.2d' %a)
b=(z/x)*100
print('Votos nulos;' '%.2d' %b)
c=(w/x)*100
print('Votos válidos:' '%.2d' %c)