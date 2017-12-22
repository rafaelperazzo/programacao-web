# -*- coding: utf-8 -*-
import math

#comece abaixo
def soma2(media):
    xi=0
    for xi in range(0,n-1,1):
        soma2=(xi-media)**2
    return(soma2)    

def desvio(n,media):
    desviopad=((1/(n-1))*(soma2(media)))**(0.5)
    return(desviopad)

a=[]
n=int(input('Digite a quantidade de números: '))
soma=0
for quant in range(0,n,1):
    num=int(input('Digite um valor: '))
    a.append(num)
    soma=soma+num

media=((soma)/n)

print('%.2f'% a[0])

print('%.2f'% a[len(a)-1])

print('%.2f'%(media)

print(desvio(n,media))