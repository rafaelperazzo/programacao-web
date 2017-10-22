# -*- coding: utf-8 -*-
import math
n=float(input("Digite um número:")) 
m=float(input("Digite um número:")) 
o=float(input("Digite um número:")) 
p=float(input("Digite um número:")) 
if n>m:
    print('s')
    break
elif m>n and m>o:
    print('s')
    break
elif o>m and o>p:
    print('s')
    break
elif p>o:
    print('s')
    break
else:
    print('n')