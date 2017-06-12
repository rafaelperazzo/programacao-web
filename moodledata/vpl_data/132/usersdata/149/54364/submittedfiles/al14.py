# -*- coding: utf-8 -*-
q=int(input('digite quantas pessoas: '))
cont=0
soma=0
for i in range(0,q,1):
    idade=int(input('digite a idade desta pessoa:'))
    soma=soma+idade
    cont=cont+1
print(soma)
print(cont)
