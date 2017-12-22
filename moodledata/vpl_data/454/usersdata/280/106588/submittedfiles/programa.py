# -*- coding: utf-8 -*-
c=int(input("Digite c: "))

ped=[]
unico=[]
estoque=[]
produz=0

for i in range (0,c,1):
    ped.append(int(input("Digite um valor: ")))

for i in ped:
    if i not in unico:
        unico.append(i)
    
for i in range (0,len(unico),1):
    estoque.append(0)
    
for i in range (0,c,1):
    k=unico.index(ped[i])
    if estoque[k]==0:
        estoque[k]=estoque[k]+2
        produz=produz+2
    if estoque[k]!=0:
        estoque[k]=estoque[k]-1

print(produz)

    
    