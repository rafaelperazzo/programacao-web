# -*- coding: utf- -*-
V=int(input("Digite V: "))
T=int(input("Digite T: "))
o=[]
for i in range (0,T,1):
   o.append(int(input("Digite os valores: ")))
vi=V
for i in range (0,len(o),1):
   vi=vi+o[i]
print(vi)