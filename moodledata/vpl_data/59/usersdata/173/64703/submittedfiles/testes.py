# -*- coding: utf-8 -*-
#O script abaixo identifica se um determinado valor
#é um número feliz, números feliz são definidos
#pelo seguinte procedimento. Começando com qualquer
#número inteiro positivo, o número é substituido pela
#soma dos quadrados dos seus dígitos, e repete-se o
#processo até que o número seja igual a 1 ou até que
#ele entre num ciclo infinito.

n=int(input('Digite um número: '))
for j in range(0,200,1):
    s=str(n)
    soma=0
    for i in s:
        soma=soma+(int(i)*int(i))
    n=soma
if(n==1):
    print('É um Número Feliz =)')
else:
    ('Não é um Número Feliz =/')