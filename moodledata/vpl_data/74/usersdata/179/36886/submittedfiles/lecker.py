# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a>b and b>c and c<d:
    print('N')
elif a>b and b<c and c>d:
    print('N')
elif a>b and c<d:
    print('N')
elif b>a and b>c or c>b and c>d:
    print('S')
elif a>b or c<d:
    print('S')
    
    

            
        
    
    