# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA

n=int(input('Digite a quantidade de termos:'))

numerador=2
denominador=1
s=0
while n>0:
    esquerda=numerador/denominador
    direita=numerador/(denominador+2)
    s=s*esquerda*direita
    numerador=numerador+2
    denominador=denominador+2
    n=n-1
pi=2*s
print('%.5f'%pi)