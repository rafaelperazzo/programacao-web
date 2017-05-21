# -*- coding: utf-8 -*-
n=int(input('Informe o número de pessoas: '))
denominadorMedia=n
somaIdades=0

while n>0:
    idade=int(input('Informe a idade: '))
    somaIdades=somaIdades+idade
    n=n-1
    
print('%.2f'%(somaIdades/denominadorMedia))