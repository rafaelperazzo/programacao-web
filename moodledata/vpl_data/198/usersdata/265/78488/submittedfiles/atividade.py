# -*- coding: utf-8 -*-
n=int(input('digite o vaor de n: '))
q=0
while 10**q<n:
    q=q+1
i=q
f=0
nf=ni=n
pi=pf=0
while i>f:
    pi=int(ni/(10**(i-1)))
    pf=nf%10
    if pi!=pf:
        break
    f=f+1
    i=i-1
    ni=ni-(pi*(10**1))
    nf=int(nf/10)
if pi=pf:
    print(n)
else :
    print(n)

