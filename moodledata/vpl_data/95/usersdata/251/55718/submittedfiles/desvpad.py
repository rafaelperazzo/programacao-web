# -*- coding: utf-8 -*-
import math

#comece abaixo
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)

def desvPad(lista,media):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media)**2)
    variancia=soma/(len(lista)-1)
    desvio=(variancia**0.5)
    return(desvio)

l=[]
n=int(input('Digite o número de termos da lista: '))
for i in range(0,n,1):
    termo=float(input('Digite o valor de índice '+str(i)+' da lista: '))
    l.append(termo)
 
print('%.2f'%l[0])
print('%.2f'%l[len(l)-1])
print('%.2f'%media(l))
print('%.2f'%desvPad(l,media(l)))