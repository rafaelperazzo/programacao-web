# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x=float(input('Total de eleitores:'))
y=float(input('Votos brancos:'))
z=float(input('Votos nulos:'))
a=(y/x)
print('Votos brancos:' '%.3f' %a)
b=(z/x)
print('Votos nulos;' '%.3f' %b)
vv=x-(y+z)
c=(vv/x)
print('Votos válidos:' '%.3f' %c)