# -*- coding: utf-8 -*-
#COMECE AQUI
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
if (a<b+c):
    print('S')
    if a**2==b**2+c**2:
        print('Re')
    elif a**2>b**2+c**2:
        print('Ob')
    elif a**2<b**2+c**2:
        print('Ac')
        if a==b==c:
            print('Eq')
        elif a==b!=c:
            print('Is')
        elif a!=b!=c:
            print('Esc')
else:
    print('N')
    

        

       