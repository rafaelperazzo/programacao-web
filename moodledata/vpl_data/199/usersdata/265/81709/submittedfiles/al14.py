# -*- coding: utf-8 -*-
n = int(input('digite os valores de n: '))
contador=1
soma=0
while (cont<=n):
    idade=int(input('digite a idade: '))
    cont=cont+1
    soma=soma + idade
media=soma/cont
print('%.2f' %media)
