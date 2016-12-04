# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
m=input('Digite o numero m de termos da formula de pi:')
e=input('Digite o epsilon para o calculo da razao aurea:')
So=3
a=2
for i in range(1,m+1,1):
    if (a//2)%2==0:
        So=So-4/(a*(a+1)*(a+2))
    else:
        So=So+4/(a*(a+1)*(a+2))
    a=a+2
pi=So
x=pi/5
S=1
i=2
while True:
    n=i
    M=1
    for i in range(1,n+1,1):
       M=M*i
    if((i//2)%2)==0:
        S=S+((x**i)/M)
    else:
        S=S-((x**i)/M)
    i=i+2
    if absoluto(S)>=e:
        break
Ra=2*S
print('O valor aproximado de pi %.15f é:'%pi(m))
print('o valor aproximado da razao aurea %.15f é:'% R(e))

