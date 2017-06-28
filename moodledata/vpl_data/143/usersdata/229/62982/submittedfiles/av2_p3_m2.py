# -*- coding: utf-8 -*-
def degrau(d):
    nova=[]
    b=0
    for i in range (o,len(a)-1,1):
        b=d[i]-d[i+1]
        if b<0:
            b=b*(-1)
            nova.append(b)
    return(nova)
    
    n=int(input('digiteo tamanho da sequência:'))
    a=[]
    for i in range (0,n,1):
     valor=int(input('digite os elementos da lista' :'))
    
      a.append(valor)
print(degrau(a))