# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x=int(input('Total de eleitores:'))
y=int(input('Votos brancos:'))
z=int(input('Votos nulos:'))
a=(y/x)
print('Votos brancos:' '%.3d' %a)
b=(z/x)
print('Votos nulos;' '%.3d' %b)
vv=x-(y+z)
c=(vv/x)
print('Votos válidos:' '%.3d' %c)