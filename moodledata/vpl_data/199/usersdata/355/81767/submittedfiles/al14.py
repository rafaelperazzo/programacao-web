# -*- coding: utf-8 -*-
pessoas=int(input('Digite a quantidade de pessoas: '))
i=1
soma=0
while(i<=pessoas):
    idade=int(input('Digite a idade: '))
    soma=soma+idade
    i=i+1

media=(soma)/(pessoas)
print(%2f.%media)