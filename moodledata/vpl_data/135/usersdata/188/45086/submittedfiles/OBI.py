# -*- coding: utf-8 -*-
N=float(input('Digite o valor de N:'))
N=int(N)
P=float(input('Digite o valor de P:'))
cont=0
SOMA=0
while cont<N:
    X=int(input('Digite o valor da Nota 1:'))
    Y=int(input('Digite o valor da Nota 2:'))
    if (X+Y)>=P:
      SOMA=SOMA+1
    cont=cont+1
print(SOMA)