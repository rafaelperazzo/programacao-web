# -*- coding: utf-8 -*-
q=int(input('digite a quantidade de pessoas: '))

soma=0
for i in range(0,q,1):
    idade=int(input('digite a idade destas pessoas:'))
    soma=soma+idade
media=soma/q
print(media)
