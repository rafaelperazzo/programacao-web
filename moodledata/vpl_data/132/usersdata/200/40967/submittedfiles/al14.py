# -*- coding: utf-8 -*-
n=int(input('digite o numero de pesooas:'))
cont=0
for i in range(1,n-1,1):
    idade=int(input('digite a idade da pessoa:'))
    cont=cont+idade
    
media=(cont/i)
print('%.2f'%media)
