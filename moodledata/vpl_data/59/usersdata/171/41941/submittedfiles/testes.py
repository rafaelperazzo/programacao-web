# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=float(input('digite a:'))
a=int(a)
b=float(input('digite b:'))
cont=0
i=a
while i<=b:
    if math.cos(i)-math.exp(i)<0:
        cont=cont+1
    i=i+0.01
if contador==0:
    print('sim')
else:
    print('nao')