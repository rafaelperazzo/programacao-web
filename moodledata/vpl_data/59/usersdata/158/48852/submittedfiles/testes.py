# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
e=int(input('total de eleitores:'))
vb=int(input('votos brancos:'))
vn=int(input('votos nulos:'))
vv=int(input('votos válidos:'))
pvb=(vb/e)*100
pvn=(vn/e)*100
pvv=(vv/e)*100
print('o valor de pvb: %d' %pvb)
print('o valor de pvn: %d' %pvn)
print('o valor de pvv: %d' %pvv)
