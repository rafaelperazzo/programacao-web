# -*- coding: utf-8 -*-
def primo (x):
    cont=0
    for i in range (1,x-1,1):
        if x%i==0:
            cont=cont+1
    if cont==2:
        return True
    else:
        return False
p=int(input('digite p:'))
q=int(input('digote q:'))
if primo (p) and primo (q):
    if q==p+2:
        print ('S')
if primo (p)==False or primo (q)==False:
    print ('N')

