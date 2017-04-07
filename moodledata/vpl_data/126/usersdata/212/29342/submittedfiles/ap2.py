# -*- coding: utf-8 -*-
a=float(input('digite o primeiro valor:'))
b=float(input('digite o segundo valor:'))
c=float(input('digite o terceiro valor:'))
d=float(input('digite o quarto valor:'))
if a>=b and a>=c and a>=d:
    print('%d'%a)
elif b>=a and b>=c and b>=d:
    print('%d'%b)    
elif c>=a and c>=b and c>=d:
    print('%d'%c)    
else:
    print('%d'%d)
if a<=b and a<=c and a<=d:
    print('%d'%a)
elif b<=a and b<=c and b<=d:
    print('%d'%b)    
elif c<=a and c<=b and c<=d:
    print('%d'%c)    
else:
    print('%d'%d)    