# -*- coding: utf-8 -*-
def degrau(b):
    dif=0
    degrau=0
    for j in range (0,len(b)-1,1):
        dif=b[j]-b[j+1]
        if (dif<0):
            dif=dif*(-1)
        if (dif>degrau):
            degrau=dif
    return(degrau)
    
A=int(input('Digite o numero de elementos da lista:'))
b=[]
for i in range (1, A+1, 1):
    valor=int(input('Digite os elementos da lista;'))
    b.append(valor)
print(degrau(b))

















