# -*- coding: utf-8 -*-
import math

#comece abaixo
def soma2(a,media):
    for i in range(0,n,1):
        soma2=((a[i])-media)**2
    return(soma2)    

def desvio(n,media):
    desviopad=((1/(n-1))*(soma2(a,media)))**(0.5)
    return(desviopad)

a=[]
n=int(input('Digite a quantidade de números: '))
soma=0
for quant in range(0,n,1):
    num=float(input('Digite um valor: '))
    a.append(num)
    soma=soma+num

media=((soma)/n)
desviopadrao= desvio(n,media)
print('%.2f'% a[0])

print('%.2f'% a[len(a)-1])

print('%.2f'%(media))

print('%.2f'% desviopadrao)