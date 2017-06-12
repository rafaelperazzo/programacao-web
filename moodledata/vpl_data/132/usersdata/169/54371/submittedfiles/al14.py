# -*- coding: utf-8 -*-
n=int(input('Digite a Quantidade de Pessoas:'))
soma=0
for i in range(0,n,1):
    id=int(input('Digite a Idade das Pessoas:'))
    soma=soma+id
média=soma/n
print(média)

    