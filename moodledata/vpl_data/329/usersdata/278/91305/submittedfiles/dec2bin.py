# -*- coding: utf-8 -*-
p = int(input("Digite um inteiro: "))
q = int(input("Digite um inteiro maior que o anterior: "))
i=10
x=0
while (p>0):
    p=p//10
    i=i*10
while (q>0):
    q=q%i
    if p==q:
        print("S")
        break
    x+=1
if x>0:
    print("N")
    

