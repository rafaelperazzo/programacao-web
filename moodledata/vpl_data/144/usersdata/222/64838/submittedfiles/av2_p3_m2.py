# -*- coding: utf-8 -*-
def vezes(x,l):
    cont=0
    for i in range(0,len(l),1):
        if l[]==x:
            cont=cont+1
    return (cont)
def magica(l):
    for i in range(0,len(l),1):
        if vezes(i,l)!=l[i]:
            return False
    return True
n=int(input('n:'))
l=[]
for i in range(1,n+1,1):
    numero=float(input('num:'))
    l.append(numero)
if magica(l):
    print('S')
else:
    print('N')
    


        