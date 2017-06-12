# -*- coding: utf-8 -*-
def primo(a):
    b=0
    for i in range(1,a+1,1):
        if a%i==0:
            b=b+1
    if b==2:
        return True
    else:
        return False
c=int(input('digite c:'))
d=int(input('digite d:'))
if primo(c) and primo(d):
    if d==c+2:
        print('S')
if primo(c)==False or primo(d)==False:
    print('N')
    

    
    
    