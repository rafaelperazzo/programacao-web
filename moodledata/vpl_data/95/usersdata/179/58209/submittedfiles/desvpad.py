# -*- coding: utf-8 -*-
import math

def media(a):
    soma=0
    for j in range(0,len(a),1):
        soma=soma+a[j]
    media=soma/len(a)
    return(media)
def desvio(a):
    soma=0
    for j in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    sdq=0
    for k in range(0,len(a),1):
        dq=(a[k]-media)**2
        sdq=sdq+dq
    var=sdq/(len(a)-1)
    desvio=var**0.5
    return(desvio)
n=int(input('digite o valor de n :'))
z=[]
for i in range(1,n+1,1):
    valor=float(input('digite o valor de elementos da lista :'))
    z.append(valor)
print('%.2f'%z[0])
print('%.2f'%z[len(z)-1])
print('%.2f'%media(z))
print('%.2f'%desviopadrao(z))

    
    
    
    

