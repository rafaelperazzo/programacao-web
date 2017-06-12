# -*- coding: utf-8 -*-
def primo(p,q):
    contador=0
    for i in range(2,(p,q),1):
        if (p,q)%i==0:
            contador=contador+1
        i=i+1
    if contador==0:
        return true
    else:
        return false
p=int(input('digite o numero p:'))
q=int(input('digite o numero q:'))
