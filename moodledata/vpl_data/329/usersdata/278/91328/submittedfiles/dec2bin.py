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
resto1=q%i
if p==resto1:
    print("S")
    x+=1
    break
else:
    while (q>0):
        q=q//10
        resto2=q%i
        if p==resto2:
            print("S")
            x+=1
            break
if x==0:
    print("N")
    

