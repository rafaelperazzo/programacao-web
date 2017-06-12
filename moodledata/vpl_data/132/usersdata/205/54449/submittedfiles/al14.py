# -*- coding: utf-8 -*-
n=int(input('digite o valor de n:'))
soma=0
for i in range (0, n,1):
    idade=int(input('digite a idade:'))
    soma=soma+idade
média=soma//n
print(média)