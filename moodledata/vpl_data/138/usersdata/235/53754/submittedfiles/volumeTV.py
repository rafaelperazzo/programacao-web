#-*- coding: utf-8 -*- 
vi=int(input('qual o volume inicial:'))
vf=int(input('qual o volume final:'))
s=n
for i in range (1,vf+1,1):
    v=int(input('mudança de volume da tv:'))
    s=s+v
    if s>100:
        s=100
    elif s<0:
        s=o
print(s)