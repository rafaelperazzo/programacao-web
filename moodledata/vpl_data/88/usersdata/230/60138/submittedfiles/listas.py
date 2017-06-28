# -*- coding: utf-8 -*-
def degrau(a):
    degrau=0
    modulo=0
    for i in range(0,len(a)-1,1):
        modulo=a[i]-a[i+1]
            if modulo<0:
                modulo=modulo*(-1)
            if modulo>degrau:
                degrau=modulo
        return(degrau)
    
a=[]
n=int(input('Digite quantidade de números: '))
for i in range (0,n,1):
    valor=int(input('Digite valor: '))
    a.append(valor)
print(degrau(a))
