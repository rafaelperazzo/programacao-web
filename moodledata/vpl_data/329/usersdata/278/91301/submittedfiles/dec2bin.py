# -*- coding: utf-8 -*-
p = int(input("Digite um inteiro: "))
q = int(input("Digite um inteiro maior que o anterior: "))
i=0
while (q>0):
    resto=q%10
    if p==resto:
        print("S")
        break
    i+=1
    q=resto
if i>0:
    print("N")
    

