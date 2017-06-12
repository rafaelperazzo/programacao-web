# -*- coding: utf-8 -*-
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
d=int(input('d:'))
e=int(input('e:'))
f=int(input('f:'))
s1=int(input('s1:'))
s2=int(input('s2:'))
s3=int(input('s3:'))
s4=int(input('s4:'))
s5=int(input('s5:'))
s6=int(input('s6:'))
cont=0
if a==s1 or a==s2 or a==s3 or a==s4 or a==s5 or a==s6: 
    if b==s1 or b==s2 or b==s3 or b==s4 or b==s5 or b==s6:
        if c==s1 or c==s2 or c==s3 or c==s4 or c==s5 or c==s6: 
            if d==s1 or d==s2 or d==s3 or d==s4 or d==s5 or d==s6: 
                if e==s1 or e==s2 or e==s3 or e==s4 or e==s5 or e==s6:
                    if f==s1 or f==s2 or f==s3 or f==s4 or f==s5 or f==s6:
                        print('sena')
while cont>0:
    if a==s1 or a==s2 or a==s3 or a==s4 or a==s5 or a==s6:
        cont=cont+1
    elif a!=s1 or a!=s2 or a!=s3 or a!=s4 or a!=s5 or a!=s6:
        cont=cont
    if b==s1 or b==s2 or b==s3 or b==s4 or b==s5 or b==s6:
        cont=cont+1
    elif b!=s1 or b!=s2 or b!=s3 or b!=s4 or b!=s5 or b!=s6:
        cont=cont
    if c==s1 or c==s2 or c==s3 or c==s4 or c==s5 or c==s6: 
        cont=cont+1
    elif c!=s1 or c!=s2 or c!=s3 or c!=s4 or c!=s5 or c!=s6:
        cont=cont
    if d==s1 or d==s2 or d==s3 or d==s4 or d==s5 or d==s6: 
        cont=cont+1
    elif d!=s1 or d!=s2 or d!=s3 or d!=s4 or d!=s5 or d!=s6:
        cont=cont
    if e==s1 or e==s2 or e==s3 or e==s4 or e==s5 or e==s6: 
        cont=cont+1
    elif e!=s1 or e!=s2 or e!=s3 or e!=s4 or e!=s5 or e!=s6:
        cont=cont
    if f==s1 or f==s2 or f==s3 or f==s4 or f==s5 or f==s6: 
        cont=cont+1
    elif f!=s1 or f!=s2 or f!=s3 or f!=s4 or f!=s5 or f!=s6:
        cont=cont
if cont==5:
    print('quina')
if cont==4:
    print('quadra')
if cont==3:
    print('terno')
if cont<3:
    print('azar')
                                                    
                                                    
                                                    
                                                    
                                                    
                                                
                                                    
    

