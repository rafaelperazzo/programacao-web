# -*- coding: utf-8 -*-
def degrais(a):
    soma=0
    degrau=0
    for i in range(0,len(a)-1,1):
        soma=(a[i]-a[i+1])
        if soma<0:
            soma=soma*(-1)
        if soma>degrau:
            degrau=soma
    return degrau
l=int(input('escreva o valor de l:'))
s=[]
for i in range(0,l,1):
    numero=int(input('escreva o numero:'))
    s.append(numero)
x=degrais(s)
print(x)