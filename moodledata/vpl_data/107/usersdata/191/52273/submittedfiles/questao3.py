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
m=int(input('digite o número:'))
n=int(input('digite o número:'))
if primo(m) and primo(n):
    if m==n+2:
        print('S')
if primo(m)==False or primo(n)==False:
    print('N')


