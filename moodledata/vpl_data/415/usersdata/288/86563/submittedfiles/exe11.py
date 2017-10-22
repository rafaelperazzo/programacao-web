# -*- coding: utf-8 -*-
n=int(input("Digite um numero de oito digitos "))
if 10000000<=n<=99999999:
    i=0
    for i in range(0,n,1):
        print (i)
else:
    print ("NAO SEI")