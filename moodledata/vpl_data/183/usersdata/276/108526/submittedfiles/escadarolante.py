# -*- coding: utf-8 -*-

N=int(input('Digite a quantidade de pessoas'))
x9=0
soma=0
a=[]
for i in range (0,N,1):
    T=int(input('Digite o tempo que cada pessoa passou pelo sensor'))
    if ( T-10 )> x9 and x9 != 0:
        soma= soma + T - x9 -10
    x9=T
    a.append(T)
    
resposta= a[N-1] + 10 - a[0] - soma
print(resposta)