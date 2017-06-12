# -*- coding: utf-8 -*-
N=float(input('digite o valor de N:'))
P=float(input('digite o valor de P:'))
N=int(N)
cont=0
soma=0
while cont<N:
    X=int(input('digite 1:'))
    Y=int(input('digite 2:'))
    if (X+Y)>=P:
        soma=soma+1
    cont=cont+1
print(soma)    
    
    