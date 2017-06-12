# -*- coding: utf-8 -*-
import math

def média(b):
    soma=0
    for k in range(0,len(b),1):
        soma=soma+i[k]
        média=soma/len(b)
    return(média)

def desvio(d):
    soma=0
    for k in range(0,len(d),1):
        soma=soma+i[k]
    média=soma/len(b)
    sdq=0
    for t in range(0,len(b),1)?
    dq=(a[t]-média)**2
    sdq=sdq+dq
    var=sdq/(len(b)-1)
    desvio=var**0.5
    return(desvio)

n=int(input('Digite a Quantidade de Números da Lista:'))
l1=[]
for i in range(1,n+1,1):
    v=float(input('Digite os Valores a Ser Incluidos na Lista:'))
    l1.append(v)
print('%2.f' %l1[0])
print('%2.f' %[len(l1)-1])
print('%2.f' %média(l1))
print('%2.f' %desvio(l1))
