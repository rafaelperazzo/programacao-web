# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de pessoas:'))
menor=0
idoso=0
soma=0

for i in range(1,n+1,1):
    idade=int(input('digite a idade i: '))
    if idade<18:
        menor=menor+1
    if idade>=60:
        idoso=idoso+1
    soma=soma+idade
pmenores=(menor/n)*100
pidoso=(idoso/n)*100
media=(soma/n)
print(pmenores)
print(pidoso)
print(media)