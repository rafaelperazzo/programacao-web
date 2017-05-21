# -*- coding: utf-8 -*-
q=int(input('Digite a quantidade de pessoas: '))
soma=0
for i in range(1,q+1,1):
    idade=int(input('Digite a idade: '))
    soma=soma+idade
    media=(soma/q)
print('%.2f'%media)
    

