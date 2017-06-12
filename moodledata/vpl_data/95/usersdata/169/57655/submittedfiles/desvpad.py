# -*- coding: utf-8 -*-
import math

def média(b):
    soma=0
    for j in range(0,len(b),1):
        soma=soma+b[j]
    média=soma/len(b)
    return(média)

def desvio(d):
    soma=0
    for j in range(0,len(d),1):
        soma=soma+b[j]
    média=soma/len(b)
    sdq=0
    for k in range(0,len(b),1):
      dq=(b[k]-média)**2
      sdq=sdq+dq
    var=sdq/(len(b)-1)
    desvio=var**0.5
    return(desvio)

n=int(input('Digite a Quantidade de Números da Lista:'))
l1=[]
for i in range(1,n+1,1):
    v=float(input('Digite os Valores a Ser Incluidos na Lista:'))
    l1.append(v)
print('%.2f' %l1[0])
print('%.2f' %l1[len(l1)-1])
print('%.2f' %média(l1))
print('%.2f' %desvio(l1))
