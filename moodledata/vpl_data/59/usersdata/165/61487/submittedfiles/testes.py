# -*- coding: utf-8 -*-

def numeromagico(a):
    l=[]
    while(a>0):
        l.append(int(a/10))
        a=a%10
    soma=0
    for i in range(0,len(l),1):
        soma=soma+l[i]
    return(soma)

dh=int(input('digite dh:'))
dm=int(input('digite dm:'))
h=numeromagico(dh)
m=numeromagico(dm)
while h>10 or m>10:
    h2=numeromagico(h)
    m2=numeromagico(m)
    h=h2
    m=m2

if h==m:
    print('Casal perfeito')
else:
    print('Nao')
    
