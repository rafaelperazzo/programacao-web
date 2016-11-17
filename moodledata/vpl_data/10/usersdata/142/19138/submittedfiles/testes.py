# -*- coding: utf-8 -*-
from __future__ import division

def primo(x):
    cont=0
    for i in range(2,x,1):
        if x%i==0:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

x=1
n=input('Digite um valor:')
cont=0
while cont<=n:
    if primo(x) and primo(x+2):
        cont=cont+1
    x=x+1
print (x-1)
print (x+1)