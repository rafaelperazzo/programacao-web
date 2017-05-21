# -*- coding: utf-8 -*-
n=int(input('digite numero de pessoas:'))
contador=0
for i in range(1,n+1,1):
    idade=int(input('digite a idade :'))
    contador=contador+idade
media=contador/n
print('%.2f'%media)