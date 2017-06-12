# -*- coding: utf-8 -*-
 
n=int(input('digite o volume inicial da tv:'))
t=int(input('digite o numero de trocas de volume:'))
 
i=0
soma=0
for i in range(1,t+1,1):
     p=int(input('digite quantas vezes o botao de controle do volume foi apertado:'))
     soma=soma+p
     i=i+1
soma=soma+n
print(soma)