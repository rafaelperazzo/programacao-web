# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de termos:'))
produto=1
soma=0
for numerador in range(2,n+1,2):
    if numerador%2==0:
        numerador=numerador/(numerador+1)
        produto=produto*numerador
    else:
        numerador=numerador/(numerador-1)
        produto=produto*numerador
pi=soma+(2*produto)
print(pi)