# -*- coding: utf-8 -*-
a=int(input('q competidores:'))
b=int(input('q competidores:'))
cont=0
for i in range (1,a+1,1):
    c=int(input('prova 1:'))
    d=int(input('prova 2:'))
    if (c+d)>=b:
        cont=cont+1
print(cont)        