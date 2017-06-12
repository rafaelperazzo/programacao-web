# -*- coding: utf-8 -*-
p=int(input('digite o valor p:'))
q=int(input('digite o valor q'))
i=2
while i<p and i<q and q>p:
    if p%i!=0 and q%i!=0:
        if q==p+2:
            print('S')
else:
    print('N')
        

