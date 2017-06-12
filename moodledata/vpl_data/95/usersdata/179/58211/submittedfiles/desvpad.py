# -*- coding: utf-8 -*-
import math

def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return(media)
def desviopadrao(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    somatodv=0
    for j in range(0,len(a),1):
        dq=(a[j]-media)**2
        somatodv=somatodv+dq
    var=somatodv/(len(a)-1)
    desviopadrao=var**1/2
    return(desviopadrao)
n=int(input('digite o valor de n :'))
z=[]
for i in range(1,n+1,1):
    valorz=float(input('digite o valor de elementos da lista :'))
    z.append(valorz)
print('%.2f'%z[0])
print('%.2f'%z[len(z)-1])
print('%.2f'%media(z))
print('%.2f'%desviopadrao(z))

    
    
    
    

