# -*- coding: utf-8 -*-
n=int(input('digite o numero de competodores n:'))
m=int(input('digite a media :'))
cont=0
for i in range(0,n,1):
    x=int(input('digite a 1° nota do candidato:'))
    y=int(input('digite a 2° nota do candidato:'))
    if x+y>=m:
        cont=cont+1
print(cont)       
