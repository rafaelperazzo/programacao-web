# -*- coding: utf-8 -*-

a=int(input('Digite o número de portas: '))
b=[]

for i in range (0,a,1):
    b.append(int(input('Digite o número de vidas por sala: ')))

ent=int(input('Digite a porta de entrada: '))
sai=int(input('Digite a porta de saída: '))

soma=0
for i in range (ent,sai+1,1):
    soma=soma+b[i]

print(soma)
