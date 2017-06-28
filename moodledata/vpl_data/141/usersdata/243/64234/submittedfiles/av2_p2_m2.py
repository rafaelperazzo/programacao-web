# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de portas:'))
a=[]
for i in range(0,n,1):
    v=int(input('digite a vida:'))
    a.append(v)
    
entrada=int(input('digite a porta de entrada:'))
saida=int(input('digite a saida:'))


soma=0
for i in range(entrada,saida+1,1):
    soma=soma+a[i]
print(soma)    
