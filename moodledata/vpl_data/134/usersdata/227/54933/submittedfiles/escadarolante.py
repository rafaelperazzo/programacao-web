# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de pessoas detectadas:'))
i=0
for i in range(1,n+1,1):
    t=int(input('Digite o instante em que a I-esima pessoa passou pelo sistema:'))
    if(i==1):
        t1=t
    elif(i==n):
        t2=t
tempo=t2-t1+10
print(tempo)
