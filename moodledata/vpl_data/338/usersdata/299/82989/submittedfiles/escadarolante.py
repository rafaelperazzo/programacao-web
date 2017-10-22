# -*- coding: utf-8 -*-
n=int(input(''))
for i in range(n):
    t=int(input(''))
    for t in range(t,10,1):
          t2=int(input(''))
          if t2-t<10:
              continue
          
print(t+t2+10)    