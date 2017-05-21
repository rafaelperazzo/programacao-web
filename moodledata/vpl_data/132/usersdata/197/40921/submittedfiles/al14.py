# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de pessoas:'))
cont=0
for i in range (1,n+1,1):
    x=int(input('Digite a idade:'))
    cont=cont+x
media=cont/n
print('%.2f'%media)
