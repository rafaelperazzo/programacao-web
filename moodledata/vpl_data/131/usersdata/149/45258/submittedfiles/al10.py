# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de termos:'))
produto=1
soma=0
for numerador in range(2,n+1,2):
    numerador=numerador/(numerador+1)
    produto=produto*numerador
for numerador in range(2,n+1,2):
    numerador=numerador/(numerador-1)
    produto=produto*numerador
soma=soma+produto
print(soma)