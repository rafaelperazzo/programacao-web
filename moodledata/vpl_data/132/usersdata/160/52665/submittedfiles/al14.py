# -*- coding: utf-8 -*-


n=int(input('Digite a quantidade de pessoas:'))
i=0
soma=0
for i in range(0,n+1,1):
    idade=int(input('Digite a idade da pessoa:'))
    soma=soma+i
    media=idade/n
print(media)
    