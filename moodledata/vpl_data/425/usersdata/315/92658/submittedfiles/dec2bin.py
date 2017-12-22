# -*- coding: utf-8 -*-
p = int(input('Digite valor de P: '))
q = int(input('Digite valor de Q: '))
p = str(p)
q = str(q)

def sn(a,b):
    return a in b
    
if sn(p,q):
    print('S')
else:
    print ('N')


"""

p = input('Digite valor de P: ')
q = input('Digite valor de Q: ')

if q.find(p)== -1:
    print('N')
else:
    print('S')

"""