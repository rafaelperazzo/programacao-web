# -*- coding: utf-8 -*-
p=int(input('Digite o P aqui: '))
q=int(input('Digite o Q aqui: '))
while p>q:
    p=int(input('Digite seu numero aqui: '))
    q=int(input('Digite seu numero aqui: '))
if str(p) in str(q):
    print ('S')
else:
    print ('N')

