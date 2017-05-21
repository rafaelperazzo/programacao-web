# -*- coding: utf-8 -*-
p=int(input('Digite p:'))
q=int(input('Digite q:'))

termo=p
con=0
con1=0

while termo>0:
    con=con+1
    p=temp//10
    
cont2=0
while q>0:
    n=9%(10**cont)
    if n==p:
        cont2=cont2+1
        
    q=q//10
    print('s')
else:
    print('n')
