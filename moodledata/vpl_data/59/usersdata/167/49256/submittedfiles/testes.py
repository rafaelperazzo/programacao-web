# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite a:'))
b=int(input('digite b:'))
anterior=a 
hehe=b
resto=anterior%hehe
while resto!=0:
    anterior=hehe
    hehe=resto
    resto=anterior%hehe
print('mdc(%d,%d)=%d'%(a,b,hehe))