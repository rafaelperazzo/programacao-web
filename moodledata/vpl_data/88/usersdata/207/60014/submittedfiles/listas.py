# -*- coding: utf-8 -*-
def degrau(b)
    dif=0
    degrau=0
    for j in range (0,len(b)-1,1):
        dif=b[j]-b[j+1]
        if (dif<0):
            dif=dif*(-1)
        if (dif>degrau):
            degrau=dif
    return(degrau)
    
n=int(input('escreva o número dos elementos da lista:'))
a=[]
for i in range (1,n+1,1):
    valor=int(input('escreva os itens da lista:'))
    a.append(valor)
print(degrau(a))
