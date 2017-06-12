# -*- coding: utf-8 -*-

def media(n):
    soma=0
    for i in range(1,n+1,1):
        n=int(input('Digite a idade:'))
        soma=soma+1
        return(soma)
n=int(input('Digite a quantidade de pessoas:'))
c=(media(n))/4
if c>=0:
    print('%.2f'%c)
    
    