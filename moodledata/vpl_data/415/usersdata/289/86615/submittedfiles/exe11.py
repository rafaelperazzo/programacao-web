# -*- coding: utf-8 -*-
n = int(input("Digite um número inteiro de oito dígitos: "))
if n>=100000000 or n<10000000:
    print("NAO SEI")
else:
    s=0
    i=10000000
    while (n//1):
        a = n//i
        s = s+a
        n = n%i
        i = i//10
    print("%.d" %(s))