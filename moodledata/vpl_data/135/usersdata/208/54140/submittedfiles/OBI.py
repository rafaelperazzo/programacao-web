# -*- coding: utf-8 -*-
a=int(input('quantidade dos competidores:'))
b=int(input('quantidade dos competidores:'))
cont=0
for i in range (1,a+1,1):
    c=int(input('quantidade dos pontos da prova 1:'))
    d=int(input('quantidade dos pontos da prova 2:'))
    if (c+d)>b:
        cont=cont+1
print(cont)