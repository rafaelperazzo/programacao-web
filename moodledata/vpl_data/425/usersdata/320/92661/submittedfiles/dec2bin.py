# -*- coding: utf-8 -*-
p = int(input('Digite o valor de P: '))
q = int(input('Digite o valor de Q: '))
p = str(p)
q = str(q)
if q.find(p) == -1:
    print ('N')
else:
    print ('S')
