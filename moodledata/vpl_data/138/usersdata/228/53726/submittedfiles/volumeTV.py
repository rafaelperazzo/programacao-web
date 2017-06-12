# -*- coding: utf-8 -*-
v=int(input('digite o volume inicial:'))
t=int(input('digite o numero de troca de volume:'))

for i in range(',t+1,'):
    n=int(input('digite quantas vezes o botão foi apertado:'))
    if (n+v)>100:
        v=100
    elif(n+v)<0:
        v=0
    else:
        v=v+n
print(v)        






