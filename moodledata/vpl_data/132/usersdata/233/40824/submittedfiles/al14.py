# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de pessoas: '))
for i in range(1,n+1,1):
    idade=int(input('Digite a idade: '))
    total=idade+idade
m=total/n    
print('%.2f'%m)
    