 -*- coding: utf-8 -*-
 v=int(input('volume inicial:'))
 t=int(input('numero de trocas:'))
 soma=0
 for i in range(1,t+1,1):
     x=int(input('digite o novo valor:'))
     soma=v+x
     if soma>=100:
         soma=100
    if soma<=0:
        soma=0
    else:
        soma=soma
    v=soma
print(soma)