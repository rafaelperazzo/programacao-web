 -*- coding: utf-8 -*-
v=int(input('digite v:'))
t=int(input('digite t:'))
for i in range(1,t+1,1):
    a=int(input('digite a:))
    if v+a<=0:
        v=v-v
    elif v+a>=100:
        b=v-100
        v=v-b
    else:
        v=v+b
print(v)