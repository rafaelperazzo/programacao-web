# -*- coding: utf-8 -*-
salas=[]
n=int(input('digite n: '))
for i in range(0,n,1):
    vida=int(input('digite vida: '))
    salas.append(vida)
entrada=int(input('digite entrada: '))
saida=int(input('digite saida: '))
soma=0
for i in range(entrada,saida+1,1):
    soma=soma+salas[i]
print(soma)