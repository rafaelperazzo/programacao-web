# -*- coding: utf-8 -*-
n=int(input('Digite o número de portas:'))
E=int(input('Digite a porta de entrada:'))
S=int(input('Digite a porta de saída:'))
a=[]

for i in range(0,n,1):
      l=int(input('Digite a vida:'))
      a.append(l)
soma=0
for i in range(E,S+1,1):
    soma=soma+a[i]
    print(soma)
    
    
    

