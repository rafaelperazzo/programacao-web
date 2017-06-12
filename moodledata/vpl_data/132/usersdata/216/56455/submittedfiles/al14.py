# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de pessoas:'))
x=[]
soma=0

for i in range(0,n,1):
    a=int(input('Digite a idade:'))
    x.append(a)

for i in range(1,len(x),1):
    soma=soma+x[i]
    
media=soma/len(x)

print('%.2f'%media)