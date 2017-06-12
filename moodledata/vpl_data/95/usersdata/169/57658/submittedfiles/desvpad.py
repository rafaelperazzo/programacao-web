# -*- coding: utf-8 -*-
import math

def média(a):
    soma=0
    for j in range(0,len(a),1):
        soma=soma+a[j]
    média=soma/len(a)
    return(média)

def desvio(a):
    soma=0
    for j in range(0,len(a),1):
        soma=soma+a[j]
    média=soma/len(a)
    sdq=0
    for k in range(0,len(a),1):
      dq=(a[k]-média)**2
      sdq=sdq+dq
    var=sdq/(len(a)-1)
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
