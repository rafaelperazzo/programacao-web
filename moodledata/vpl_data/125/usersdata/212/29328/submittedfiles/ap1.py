# -*- coding: utf-8 -*-
n1=float(input('digite um do primeiro número:'))
n2=float(input('digite um do segundo número:'))
n3=float(input('digite um do terceiro número:'))
if n3<=n2 and n3<=n1:
    print('%d'%n3)    
    if n2<=n1:
     print('%d'n2)
     print('%d'n1)
    else 
     print('%d'n1)
     print('%d'n2)
elif n2<=n1 and n2<=n3:
    print('%d'%n2)    
    if n3<=n1:
     print('%d'n3)
     print('%d'n1)
    else 
     print('%d'n1)
     print('%d'n3)
else
    print('%d'%n1)    
    if n2<=n3:
     print('%d'n2)
     print('%d'n3)
    else 
     print('%d'n3)
     print('%d'n2)     