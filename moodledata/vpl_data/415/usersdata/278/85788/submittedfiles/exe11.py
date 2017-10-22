# -*- coding: utf-8 -*-
n = int(input("Digite um número inteiro de oito dígitos: "))
if n>=100000000 or n<10000000:
    print("NAO SEI")
else:
    s=0
    i=10**8
    while (n//1):
        x = n//i
        s=s+x
        i=i//10
    print("%.d" %(s))