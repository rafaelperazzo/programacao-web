# -*- coding: utf-8 -*-
q=int(input('digite a quantia de portas:'))
h=int(input('digite a porta de entrada:'))
m=int(input('digite a porta de saída:'))
s=[]
for i in range(0,q,1):
    j=int(input('digite a vida:'))
    s.append(j)
soma=0
for i in range(h,m+1,1):
    soma=soma+s[i]
    print(soma)

