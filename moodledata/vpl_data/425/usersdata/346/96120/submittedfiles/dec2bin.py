# -*- coding: utf-8 -*-

p= int(input('Digite um numero p: '))
q= int(input('Digite um numero q: '))
TRUE=1
FALSE=0

pot10= 1
while (pot10<=p):
    pot10= pot10*10
    achou= FALSE
    quax= 1
    while (quax>= p or achou == FALSE):
        subnumero= quax%pot10
        quax= quax/10
        if(subnumero==p):
            achou= TRUE
if (achou==TRUE):
    print('S')
else:
    print('N')
    
