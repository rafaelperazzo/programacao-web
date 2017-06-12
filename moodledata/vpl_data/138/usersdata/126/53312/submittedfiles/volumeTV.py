# -*- coding: utf-8 -*-
 
n=int(input('digite o volume inicial da tv:'))
t=int(input('digite o numero de trocas de volume:'))
 
i=0
soma=n
a=[]
for i in range(1,t+1,1):
     p=int(input('digite quantas vezes o botao de controle do volume foi apertado:'))
     a.append(p)
     i=i+1
for i in range (0,len(a),1):
    soma=soma+a[i]
    if 0<=soma<=100:
        print(soma)
    i=i+1


