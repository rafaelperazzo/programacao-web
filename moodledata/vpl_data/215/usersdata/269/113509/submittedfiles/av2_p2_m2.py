# -*- coding: utf-8 -*-
n=int(input('digite quantidade de salas: '))
a=[]
for i in range(0,n,1):
    x=int(input('digite valor da vida: '))
    a.append(x)
    
entrada= int(input('digite entrada: ')) 
saida= int(input('digite saida: '))
soma=0
for i in range(entrada,saida+1,1):
    soma=soma+a[i]
print(soma)    

