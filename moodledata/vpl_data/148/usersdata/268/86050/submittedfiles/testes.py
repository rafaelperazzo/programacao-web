# -*- coding: utf-8 -*-

a= int(input('Digite a : '))
b= int(input('Digite b : '))
c= int(input('Digite c : '))
d= int(input('Digite d : '))
e= int(input('Digite e : '))

X1=10**(-5555555555555)
X2=-10**(5555555555555)
cont=0
while (cont<5):
      if a>b and a>c and a >d  and a>e:
             print(a)
             if a> 0:
                  a=X1
             if a<=0:
                   a=X2
             cont=cont+ 1
      if b>a and b>c and b>d  and b>e:
              print(b)
              if b> 0:
                  b=X1
              if b<=0:
                   b=X2
              
              cont=cont+1
      if c>a and c>b and c>d  and c>e:
              print(c)
              if c> 0:
                  a=X1
              if c<=0:
                   c=X2
              
              cont=cont+1
      if d>a and d>b and d>c  and d>e:
             print(d)
             if d> 0:
                  e=X1
             if d<=0:
                   d=X2
             
             cont=cont+1
      if e>a and e>b and e>d  and e>d:
             print(e)
             if e> 0:
                  e=X1
             if e<=0:
                  e=X2
             
             cont=cont+1

