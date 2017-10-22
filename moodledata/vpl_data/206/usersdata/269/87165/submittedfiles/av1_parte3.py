# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('digite n: '))

if n%2==0:
    sp=0
    si=0
    for i in range(0,n/2,1):
        if i%2==0:
            sp=sp+ (1/(1*(3**i)))
        if i%2==1:
            si=si- (1/(1*(3**i)))
    soma=sp+si
    pi=(12**0.5)*soma
    print('valor de pi é %.6f' %pi)