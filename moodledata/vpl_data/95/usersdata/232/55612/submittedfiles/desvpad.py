# -*- coding: utf-8 -*-
import math

#comece abaixo
def medialista (a):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+lista[i]
    media=soma/(len(lista))
    return media
    
def DesvPad (media,a):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((a[i]-media)**2)
    DesvPad=soma/(len(lista)-1)
    return DesvPad

n=int(input('Digite o número de elementos da lista: '))
a=[ ]
for i in range(1,n+1,1):
    h=float(input('Digite o elemento '+str(i)+' da lista: '))
    a.append(h)

print('%.2f' %a[0])
print('%.2f' %a[len(a)-1])
print('%.2f' %medialista(a))
print('%.2f' %DesvPad(media(a),a)
