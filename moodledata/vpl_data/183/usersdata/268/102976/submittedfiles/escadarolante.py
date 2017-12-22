# -*- coding: utf-8 -*-
N=int(input('pessoas: '))
sub=0
cont=0
x9=0
a=[]

for i in range(0,N,1):
    
    T=int(input('Termo'))
    if (T-10)<= x9:
        cont=cont+1
    if (T-10)> x9:
        sub= T - (x9*10) + sub
    x9=T
    a.append(T)
    
if cont==len(a):
     resposta1 = a[N-1] + 10 - a[0]
     print(resposta1)
if cont==0:
     resposta2 =  a[N-1] + 10 - a[0] - sub
     print(resposta2)
    
    
