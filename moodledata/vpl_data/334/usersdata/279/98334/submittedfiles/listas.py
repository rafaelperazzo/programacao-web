# -*- coding: utf-8 -*-

n=(int(input()))
d=0
lista=[]
for i in range(0,n,1) :
    lista.append(int(input()))
for i in range(0,n,1) :
  if ((lista[i]-lista[i+1])>=0) :
      s=(lista[i]-lista[i+1])
      if s>d :
         d=s
print(d)      