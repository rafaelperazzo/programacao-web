# -*- coding: utf-8 -*-
A=int(input('digite o valor dos itens:'))
i=0
numerador=2
denominador=1
produto=1
while i<=A:
    produto=produto*numerador/denominador
    if i%2==1:
        numerador=numerador+2
    else:
        denominador=denominador+2
    i=i+1
    produto=produto*2
print(produto)

    
    


























