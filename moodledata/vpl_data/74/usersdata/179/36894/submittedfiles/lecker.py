# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if b>a and b>c and c<d:
    print('N')
elif c>d and c>b and a>b:
    print('N')
elif b>a and b>c or c>b and c>d:
    print('S')
elif a>b and c<d:
    print('S')
elif a>b or d>c:
    print('S')
else:
    print('N')
    

            
        
    
    