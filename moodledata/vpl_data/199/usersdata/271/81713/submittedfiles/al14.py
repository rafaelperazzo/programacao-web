# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite o numero de pessoas : '))
cont= 1
soma = 0
#PROCESSAMENTO
while(cont<=n) :
    idade = int(input('Digite a idade : '))
    soma = soma+idade
    cont= cont+ 1
#SAIDA
media = soma/n
print('%.2f ' % media)
