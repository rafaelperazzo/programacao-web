# -*- coding: utf-8 -*-
p = int(input("Digite um inteiro: "))
q = int(input("Digite um inteiro maior que o anterior: "))
i=1
x=0
while (p>0):
    i=i*10
    if p<i:
        break
    resto=p%i
    p=p//i
    if p==0:
        break
    p=p*i+resto
while (q>0):
    resto1=q%i
    p=p*i
    if p==resto1:
        print("S")
        x+=1
        break
    q=q//i
if x==0:
    print("N")
    

