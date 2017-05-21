# -*- coding: utf-8 -*-
cv=int(input('Digite o valor d1: '))
ce=int(input('Digite o valor m1: '))  
cs=int(input('Digite o valor a1: '))  
fv=int(input('Digite o valor d2: '))
fe=int(input('Digite o valor m2: '))  
fs=int(input('Digite o valor a2: '))  
pc=(cv*3)+ce
pf=(f*3)+fe
if pc>pf:
    print('C')
elif pf>pc:
    print('F')
else:
    if cs>fs:
        print('C')
    elif cs>fs:
        print('F')
    else:
        print('si')