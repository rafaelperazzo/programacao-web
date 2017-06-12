 -*- coding: utf-8 -*-
 v=int(input('Digite o volume inicial da tv: '))
 t=int(input('Digite o número de trocas de volume: '))
 a=[ ]
 for i in range (1,t+1,1):
    p=int(input('Digite quantas vezes foi apertado a tecla de volume: '))
    a.append(p)
for i in range (0,len(a)-1,1):
    v=v+a[i]
    
    if v>=100:
        v=100
        if a[i]<0:
            v=v+a[i]
print(v)
    
    
