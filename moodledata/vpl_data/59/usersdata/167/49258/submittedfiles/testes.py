# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite a:'))
b=int(input('digite b:'))
anterior=a 
atual=b
resto=anterior%atual
while resto!=0:
    anterior=atual
    atual=resto
    resto=anterior%atual
print('mdc(%d,%d)=%d'%(a,b,atual))