# -*- coding: utf-8 -*-
a = float (input('Digite um número a : '))
b = float (input('Digite um número b : '))
c = float (input('Digite um número c : '))
if a<b and b<c and a<c:
    print('%2.f'%a)
    print('%2.f'%b)
    print('%2.f'%c)

elif a<b and c<b and a<c:
    print('%2.f'%a)
    print('%2.f'%c)
    print('%2.f'%b)

elif b<a and a<c and b<c:
    print('%2.f'%b)
    print('%2.f'%a)
    print('%2.f'%c)
    
elif b<a and c<a and b<c:
    print('%2.f'%a)
    print('%2.f'%c)
    print('%2.f'%b)
    
elif c<a and a<b and c<b:
    print('%2.f'%c)
    print('%2.f'%a)
    print('%2.f'%b)
    
elif c<a and b<a and c<b:
    print('%2.f'%c)
    print('%2.f'%b)
    print('%2.f'%a)
    