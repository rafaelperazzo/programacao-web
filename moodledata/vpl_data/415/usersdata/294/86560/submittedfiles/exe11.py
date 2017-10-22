# -*- coding: utf-8 -*-
n = int(input('Digite um inteiro de exatamente oito digitos: '))
if n>=100000000 or n<10000000:
    print('NAO SEI')
else:
    c=0
    i=10000000
    while(n//1):
        a = n//i
        c+=a
        n=n%i
        i=i//10
    print('%.d' %(c))