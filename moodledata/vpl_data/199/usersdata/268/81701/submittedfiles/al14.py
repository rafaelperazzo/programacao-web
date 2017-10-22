# -*- coding: utf-8 -*-
n=int(input('Digite n : '))
cont=0
soma=0
while(cont<n):
    idade=int(input('Digite a idade: '))
    cont=cont+1
    soma=idade+soma
media= soma/n
print(media)
