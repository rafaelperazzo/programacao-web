# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))
d=int(input('digite d: '))
e=int(input('digite e: '))
f=int(input('digite f: '))

s1=int(input('digite s1: '))
s2=int(input('digite s2: '))
s3=int(input('digite s3: '))
s4=int(input('digite s4: '))
s5=int(input('digite s5: '))
s6=int(input('digite s6: '))

if a==s1:
    as1=1
else:
    as1=0
if a==s2:
    as2=1
else:
    as2=0
if a==s3:
    as3=1
else:
    as3=0
if a==s4:
    as4=1
else:
    as4=0
if a==s5:
    as5=1
else:
    as5=0
if a==s6:
    as6=1
else:
    as6=0
    
    
    
if b==s1:
    bs1=1
else:
    bs1=0
if b==s2:
    bs2=1
else:
    bs2=0
if b==s3:
    bs3=1
else:
    bs3=0
if b==s4:
    bs4=1
else:
    bs4=0
if b==s5:
    bs5=1
else:
    bs5=0
if b==s6:
    bs6=1
else:
    bs6=0
    
    
if c==s1:
    cs1=1
else:
    cs1=0
if c==s2:
    cs2=1
else:
    cs2=0
if c==s3:
    cs3=1
else:
    cs3=0
if c==s4:
    cs4=1
else:
    cs4=0
if c==s5:
    cs5=1
else:
    cs5=0
if c==s6:
    cs6=1
else:
    cs6=0
    
    
if d==s1:
    ds1=1
else:
    ds1=0
if d==s2:
    ds2=1
else:
    ds2=0
if d==s3:
    ds3=1
else:
    ds3=0
if d==s4:
    ds4=1
else:
    ds4=0
if d==s5:
    ds5=1
else:
    ds5=0
if d==s6:
    ds6=1
else:
    ds6=0    
    
    
if e==s1:
    es1=1
else:
    es1=0
if e==s2:
    es2=1
else:
    es2=0
if e==s3:
    es3=1
else:
    es3=0
if e==s4:
    es4=1
else:
    es4=0
if e==s5:
    es5=1
else:
    es5=0
if e==s6:
    es6=1
else:
    es6=0    
    
    
if f==s1:
    fs1=1
else:
    fs1=0
if f==s2:
    fs2=1
else:
    fs2=0
if f==s3:
    fs3=1
else:
    fs3=0
if f==s4:
    fs4=1
else:
    fs4=0
if f==s5:
    fs5=1
else:
    fs5=0
if f==s6:
    fs6=1
else:
    fs6=0    
  
  
acertos= as1+as2+as3+as4+as5+as6+bs1+bs2+bs3+bs4+bs5+bs6+cs1+cs2+cs3+cs4+cs5+cs6+ds1+ds2+ds3+ds4+ds5+ds6+es1+es2+es3+es4+es5+es6+fs1+fs2+fs3+fs4+fs5+fs6

if acertos==3:
    print('terno')
if acertos==4:
    print('quadra')
if acertos==5:
    print('quina')
if acertos==6:
    print('sena')
if acertos<3:
    print('azar')
    