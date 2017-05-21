# -*- coding: utf-8 -*-
soma=0
i=0
for n>0:
    resto=n%2
soma=soma+(2**i)*resto
n=n//2
i=i+i
print (soma)

