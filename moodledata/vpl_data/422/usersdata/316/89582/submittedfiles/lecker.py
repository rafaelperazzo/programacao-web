# -*- coding: utf-8 -*-
import math
n=float(input("Digite um número:")) 
m=float(input("Digite um número:")) 
o=float(input("Digite um número:")) 
p=float(input("Digite um número:")) 
print(n,m,o,p)
if n>m:
    print('s')
elif m>n and m>o:
    print('s')
elif o>m and o>p:
    print('s')
elif p>o:
    print('s')
else:
    print('n')