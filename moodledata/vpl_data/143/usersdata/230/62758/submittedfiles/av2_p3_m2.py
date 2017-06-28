# -*- coding: utf-8 -*-
def degrau(a):
    soma=0
    a=[]
    for i in range(0,len(a)-1,1):
        soma=soma+(a[i]-a[i+1])
        a.append(soma)
    return (a)  

a=[]
n=int(input('Digite quantidade de termos:'))
for i in range(0,n,1):
    valor=int(input('Digite valor:'))
    a.append(valor)
print(degrau(a))
    