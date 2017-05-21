# -*- coding: utf-8 -*-
cv=int(input('Digite o valor cv: '))
ce=int(input('Digite o valor ce: '))  
cs=int(input('Digite o valor cs: '))  
fv=int(input('Digite o valor fv: '))
fe=int(input('Digite o valor fe: '))  
fs=int(input('Digite o valor fs: '))  
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
        
        
        