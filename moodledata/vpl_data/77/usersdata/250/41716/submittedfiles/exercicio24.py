# -*- coding: utf-8 -*-
import math
n1=int(input('digite n1:'))
n2=int(input('digite n2:'))
anterior=n1
atual=n2
resto=anterior%atual
while resto!=0:
    anterior=atual
    atual=resto
    resto=anterior%atual
print('mdc %d,%d'%(n1,n2,atual))
    

