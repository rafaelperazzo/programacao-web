# -*- coding: utf-8 -*-
n=int(input('Informe o número de pessoas: '))
denominadorMedia=n
somaIdades=0

while n>0:
    idade=int(input('Informe a idade: '))
    somaIdades=somaIdades+idade
print('%.2f'%(somaIdades/denominadorMedia))