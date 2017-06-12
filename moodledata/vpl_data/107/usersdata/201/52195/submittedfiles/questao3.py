# -*- coding: utf-8 -*-
def primo(r):
    contador=0
    for j in range(1,r+1,1):
        if r%j==0:
            contador=contador+1
    if cont==2:
        return True
    else:
        return False
p=int(input('Digite um valor:'))
q=int(input('Digite um valor:'))
if primo(p) and primo(q):
    if q==p+2:
        print('S')
if primo(p)==False or primo(q)==False:
    print('N')