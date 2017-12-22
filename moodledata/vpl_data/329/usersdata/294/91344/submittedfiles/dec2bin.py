# -*- coding: utf-8 -*-
p= int(input('digite o primeiro valor: '))
q= int(input('digite o segundo valor: '))
cont=0
c=0
p1=p
while (p>0):
    cont+=1
    p= p//10
while (q>0):
    if p1==q%(10**cont):
        c+=1
    q=q//10
if c>=1:
    print ('S')
else:
    print ('N')