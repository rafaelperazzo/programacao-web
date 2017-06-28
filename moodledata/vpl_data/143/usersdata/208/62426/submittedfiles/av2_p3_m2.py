# -*- coding: utf-8 -*-
def degrais(a):
    soma=0
    degrau=0
    for i in range(o,len(a)-1,1):
        soma=(a[i]-a[i+1])
        if soma<0:
            soma=soma*(-1)
        if soma>degrau:
            degrau=soma
    return degrau 
h=int(input('VALOR DE H:'))
j=[]
for i in range(0,h,1):
    numero=int(input('NUMERO:'))
    j.append(numero)
x=degrais(j)
print(x)