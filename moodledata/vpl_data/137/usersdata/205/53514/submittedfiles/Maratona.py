# -*- coding: utf-8 -*-
n=int(input('digite o valor dos postos:'))
m=int(input('digite a distância máxima:'))
a=m
cont=0
for i in range (1, n+1, 1):
    d=int(input('digite a posição dos postos:'))
    a=d-m
    if (a<m):
        cont=cont+1
if (cont!=n):
    print ('n')
else:
    print ('s')