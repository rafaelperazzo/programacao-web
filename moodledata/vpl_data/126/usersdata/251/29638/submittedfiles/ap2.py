# -*- coding: utf-8 -*-
a = float (input('Digite um valor "a" qualquer: '))
b = float (input('Digite um valor "b" qualquer: '))
c = float (input('Digite um valor "c" qualquer: '))
d = float (input('Digite um valor "d" qualquer: '))

if a>=b and a>=c and a>=d: 
    print('O maior valor é: %1.f'%a)
    
elif b>=a and b>=c and b>=d:
    print('O maior valor é: %1.f'%b)
    
elif c>=a and c>=b and c>=d:
    print('O maior valor é: %1.f'%c)    
    
elif d>=a and d>=b and d>=c:
    print('O maior valor é: %1.f'%d) 
    
if a<=b and a<=c and a<=d: 
    print('O menor valor é: %1.f'%a)
    
elif b<=a and b<=c and b<=d:
    print('O menor valor é: %1.f'%b)
    
elif c<=a and c<=b and c<=d:
    print('O menor valor é: %1.f'%c)    
    
elif d<=a and d<=b and d<=c:
    print('O menor valor é: %1.f'%d)     