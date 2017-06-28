# -*- coding: utf-8 -*-

q=int(input('digite a quantidade de portas:'))
e=int(input('digite a porta de entrada:'))
s=int(input('digite a porta de saída:'))
a=[]
for i in range(0,q,1):
    l=int(input('digite a vida dessa porta :'))
    a.append(l)
    
soma=0
for i in range(e,s+1,1):
    soma=soma+a[i]
print(soma)
    

    

