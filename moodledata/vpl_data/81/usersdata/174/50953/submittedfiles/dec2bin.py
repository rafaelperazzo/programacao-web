# -*- coding: utf-8 -*-
p=int(input('Digite p:'))
q=int(input('Digite q:'))
t=p
cont=0
contb=0
while t>0:
    t=t//10
    cont=cont+1
while q>0:
    n=q%(10**cont)
    if n==p:
        contb=contb+1
    q=q//10
if contb>0:
    print 'S'
else:
    print 'N'

