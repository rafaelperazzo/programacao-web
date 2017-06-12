# -*- coding: utf-8 -*-
import math

def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return media
def desvpadrao(a,media):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+((a[i]-media)**2)
    desvpadrao=((soma/(n-1)))**0.5
    return desvpadrao
n=int(input('Digite o tamanho da lista: '))
a=[]
for i in range(1,n+1,1):
    valor=float(input('valor: '))
    a.append(valor)
print('%.2f' %a[0])
print('%.2f' %(a[n-1]))
print('%.2f' %media(a))
print('%.2f' %desvpadrao(a,media(a)))

    
    