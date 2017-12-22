# -*- coding: utf-8 -*-

p= int(input('Digite um numero p: '))
q= int(input('Digite um numero q: '))

pot10= 1
while (pot10<=p):
    pot10= pot10**10
    achou= 0
    quax= 1
    while (quax>= p or achou == 0):
        subnumero= quax%pot10
        quax= quax/10
        if(subnumero==p):
            achou= 1
if (achou==1):
    print('S')
else:
    print('N')
    
