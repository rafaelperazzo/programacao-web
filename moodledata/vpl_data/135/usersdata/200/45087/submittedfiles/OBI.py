# -*- coding: utf-8 -*-
N=float(input('digite o valor de N:'))
N=int(N)
P=float(input('digite o valor de P:'))
cont=0
soma=0
while cont<N:
    x=int(input('digite o valor da nota 1:'))
    y=int(input('digite o valor da nota 2:'))
    if (x+y)>=P:
      soma=soma+1
    cont=cont+1
print(soma)