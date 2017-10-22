# -*- coding: utf-8 -*-
n = int(input("Digite um número inteiro de oito dígitos: "))
if n>=100000000 and n<10000000:
    print("NAO SEI")
else:
    s=o
    i=10**8
    while (n//1):
        n//i=s
        s=+s
        i=i//10
    print("%.d" %(s))