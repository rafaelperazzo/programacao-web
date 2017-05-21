# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x=int(input('Total de eleitores:'))
y=int(input('Votos brancos:'))
z=int(input('Votos nulos:'))
a=(y/x)*100
print('Votos brancos:' %a)
b=(z/x)*100
print('Votos nulos;' %b)
vv=x-(y+z)
c=(vv/x)*100
print('Votos válidos:' %c)