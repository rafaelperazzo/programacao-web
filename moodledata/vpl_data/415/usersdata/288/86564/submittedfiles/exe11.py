# -*- coding: utf-8 -*-
n=int(input("Digite um numero de oito digitos "))
if 10000000<=n<=99999999:
    i=0
    N=0
    for i in range(0,n,1):
        N=N+i
        print (N)
else:
    print ("NAO SEI")