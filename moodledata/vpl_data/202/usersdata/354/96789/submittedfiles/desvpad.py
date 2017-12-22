# -*- coding: utf-8 -*-
import math

#comece abaixo

lista=[]
n=int(input('digite o valor de n: '))
soma=0
xi=0
for i in range(0,n,1):
    num=int(input('digite o valor: '))
    lista.append(num)
    soma=soma+num
media=(soma)/n
def somatorio(media):
    somato(xi-media)**2
    return(somato)
    
def desvio_padrao(n,somato):
    dp=((1/(n-1))*(somato))**0.5
    return(dp)


print('%.2f' %lista[0])

print('%.2f' %lista[len(lista)-1])

print('%.2f' %(media))

print('%.2f' %(desvio_padrao))
