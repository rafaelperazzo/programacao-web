# -*- coding: utf-8 -*-
N=int(input('Digite o numero de pessoas detectadas: ' ))
v=int(input('Digite o primeiro tempo: '))
cont=10
for i in range(2,N+1,1):
    t=int(input('Tempo de funcionamento: '))
    x=t-a
    cont=cont+x
    a=t
print(cont)
