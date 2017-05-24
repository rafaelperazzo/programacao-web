# -*- coding: utf-8 -*-
p=int(input('Digite p:'))
q=int(input('Digite q:'))

termo=p
con=0
con1=0

while termo>0:
    termo=termo//10
    con=con+1
    
while q>0:
    n=q%(10**con)
    if n==p:
        con1=con1+1
    q=q//10
if con1>0:
    print('S')

else:
    print('N')


