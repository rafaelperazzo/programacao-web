# -*- coding: utf-8 -*-
p = int(input("Digite um inteiro: "))
q = int(input("Digite um inteiro maior que o anterior: "))
i=0
while (q>0):
    q=q//10
    if p==q:
        print("S")
        break
    i+=1
if i>0:
    print("N")
    

