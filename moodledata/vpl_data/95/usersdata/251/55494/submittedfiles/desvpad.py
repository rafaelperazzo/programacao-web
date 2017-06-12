# -*- coding: utf-8 -*-
import math

#comece abaixo
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)
    


l=[]
n=int(input('Digite o número de termos da lista: '))
for i in range(0,n,1):
    termo=float(input('Digite o valor de índice '+str(i)+' da lista: '))
    l.append(termo)
 
 print('%.2f'%l[0])
 print('%.2f'%l[len(lista)-1])
 print('%.2f'%media(l))
 print(l)