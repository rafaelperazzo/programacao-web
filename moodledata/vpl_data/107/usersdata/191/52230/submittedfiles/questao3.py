# -*- coding: utf-8 -*-
def primo(x):
    cont=0
    for i in range (1,x+1,1):
        if x%i==0:
            cont=cont+1
    if cont==2:
        return True
    else:
        return False
a=int(input('digite o valor:')
b=int(input('digite o valor:')
if primo(a) and primo(b):
    if b==a+2:
        print('S')
if primo(a)==False or primo(b)==False:
    print('N')


