# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x=float(input('Total de eleitores:'))
y=float(input('Votos brancos:'))
z=float(input('Votos nulos:'))
a=(y/x)
print('Votos brancos:' '%.2f' %a)
b=(z/x)
print('Votos nulos;' '%.2f' %b)
vv=x-(y+z)
c=(vv/x)
print('Votos válidos:' '%.2f' %c)